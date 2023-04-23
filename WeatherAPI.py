from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import xml.dom.minidom
import xml.etree.ElementTree as ET
import datetime

from config import APIKEY

'''
초단기실황 VilageFcstInfoService_2.0/getUltraSrtNcst
초단기예보 VilageFcstInfoService_2.0/getUltraSrtFcst
단기예보조회 VilageFcstInfoService_2.0/getVilageFcst
예보버전조회 VilageFcstInfoService_2.0/getFcstVersion
'''
operation_name={'초단기실황':'getUltraSrtNcst', '초단기예보':'getUltraSrtFcst', '단기예보':'getVilageFcst', '예보버전':'getFcstVersion'}
now = datetime.datetime.now()
base_date = now.strftime('%Y%m%d')
if now.minute >= 40:
    base_time = now.strftime('%H00')
else:
    base_time = (now - datetime.timedelta(hours=1)).strftime('%H00')

baseurl = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/'
queryParams = operation_name['초단기실황'] + '?' + urlencode({quote_plus('serviceKey'): APIKEY, quote_plus('numOfRows'): '10', quote_plus('pageNo'): '1', quote_plus('base_date'): base_date, quote_plus('base_time'): base_time, quote_plus('nx'): '61', quote_plus('ny'): '125'})

request = Request(baseurl + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
decoded_response = response_body.decode('UTF-8')

dom = xml.dom.minidom.parseString(decoded_response)
pretty_response = dom.toprettyxml()

# Parse the XML response
root = ET.fromstring(decoded_response)

# Initialize an empty dictionary to store the results
weather_data = {}

# Iterate through the 'item' elements in the XML response
for item in root.iter('item'):
    category = item.find('category').text
    obsr_value = float(item.find('obsrValue').text)
    weather_data[category] = obsr_value

# Print the resulting dictionary
print(weather_data)