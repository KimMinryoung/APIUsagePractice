from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import xml.dom.minidom
from config import APIKEY

baseurl = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'

queryParams = '?' + urlencode({quote_plus('serviceKey'):APIKEY, quote_plus('numOfRows'):'10', quote_plus('pageNo'):'1', quote_plus('base_date'):'20230422', quote_plus('base_time'):'0600', quote_plus('nx'):'55', quote_plus('ny'):'127'})

print(queryParams)

request = Request(baseurl + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
decoded_response = response_body.decode('UTF-8')
dom = xml.dom.minidom.parseString(decoded_response)
pretty_response = dom.toprettyxml()
print(pretty_response)