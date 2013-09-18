# The Grinder 3.11
# HTTP script recorded by TCPProxy at Sep 18, 2013 9:59:02 PM

from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()

# Imports for Fresto
import time
from java.util import UUID

def timestr():
	return str(int(round(time.time() * 1000)))

appHost = 'beta.owlab.com'
appPort = '8080'
frestoHost = 'fresto1.owlab.com'
frestoPort = '9999'
clientIp = '180.229.124.46' #This IP Addres should be of load generator

# UUID bucket for each thread to create and reuse UUID
uuidList = []
def addUUID(index) :
	uuidList.insert(index, UUID.randomUUID().toString())
	return uuidList[index]

def getUUID(index) :
	return uuidList[index]

# To use a proxy server, uncomment the next line and set the host and port.
# connectionDefaults.setProxyServer("localhost", 8001)

def createRequest(test, url, headers=None):
    """Create an instrumented HTTPRequest."""
    request = HTTPRequest(url=url)
    if headers: request.headers=headers
    test.record(request, HTTPRequest.getHttpMethodFilter())
    return request

# These definitions at the top level of the file are evaluated once,
# when the worker process is started.

connectionDefaults.defaultHeaders = \
  [ NVPair('Accept-Encoding', 'gzip, deflate'),
    NVPair('Accept-Language', 'en-US,en;q=0.5'),
    NVPair('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0 FirePHP/0.7.4'), ]

headers0= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/'), ]

headers1= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/'), ]

headers2= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/'),
    NVPair('Cache-Control', 'no-cache'), ]

headers3= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'), ]

headers4= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'), ]

headers5= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'), ]

headers6= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'),
    NVPair('Cache-Control', 'no-cache'), ]

headers7= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=BIRDS'), ]

headers8= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=BIRDS'),
    NVPair('Cache-Control', 'no-cache'), ]

headers9= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=AV-SB-02'), ]

headers10= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=AV-SB-02'),
    NVPair('Cache-Control', 'no-cache'), ]

headers11= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-19'), ]

headers12= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-19'),
    NVPair('Cache-Control', 'no-cache'), ]

headers13= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=REPTILES'), ]

headers14= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=REPTILES'),
    NVPair('Cache-Control', 'no-cache'), ]

headers15= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=RP-SN-01'), ]

headers16= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=RP-SN-01'),
    NVPair('Cache-Control', 'no-cache'), ]

headers17= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-12'), ]

headers18= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-12'),
    NVPair('Cache-Control', 'no-cache'), ]

headers19= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=CATS'), ]

headers20= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=CATS'), ]

headers21= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=CATS'),
    NVPair('Cache-Control', 'no-cache'), ]

headers22= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DLH-02'), ]

headers23= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DLH-02'),
    NVPair('Cache-Control', 'no-cache'), ]

headers24= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-17'), ]

headers25= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-17'),
    NVPair('Cache-Control', 'no-cache'), ]

headers26= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/checkout.do'), ]

headers27= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/checkout.do'),
    NVPair('Cache-Control', 'no-cache'), ]

headers28= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do'), ]

headers29= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do'), ]

headers30= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do'), ]

headers31= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do'), ]

headers32= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do'),
    NVPair('Cache-Control', 'no-cache'), ]

headers33= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do?_finish=true'), ]

headers34= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do?_finish=true'),
    NVPair('Cache-Control', 'no-cache'), ]

headers35= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DSH-01'), ]

headers36= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DSH-01'),
    NVPair('Cache-Control', 'no-cache'), ]

headers37= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-15'), ]

headers38= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-15'),
    NVPair('Cache-Control', 'no-cache'), ]

headers39= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCart.do?page=next'), ]

headers40= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCart.do?page=next'),
    NVPair('Cache-Control', 'no-cache'), ]

headers41= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'),
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/signoff.do'), ]

# Setting tartget host and port
url0 = 'http://' + appHost + ':' + appPort
url1 = 'http://' + frestoHost + ':' + frestoPort

request101 = createRequest(Test(101, 'GET /'), url0)

request102 = createRequest(Test(102, 'GET fresto_getip.js'), url0, headers0)

request103 = createRequest(Test(103, 'GET jquery-1.10.2.js'), url0, headers0)

request104 = createRequest(Test(104, 'GET randomUUID.js'), url0, headers0)

request105 = createRequest(Test(105, 'GET fresto_link.js'), url0, headers0)

request201 = createRequest(Test(201, 'GET whatIsMyIPAddress'), url1, headers0)

request301 = createRequest(Test(301, 'GET sign-in.gif'), url0, headers1)

request302 = createRequest(Test(302, 'GET cart.gif'), url0, headers1)

request303 = createRequest(Test(303, 'GET separator.gif'), url0, headers1)

request304 = createRequest(Test(304, 'GET search.gif'), url0, headers1)

request305 = createRequest(Test(305, 'GET help.gif'), url0, headers1)

request306 = createRequest(Test(306, 'GET logo-topbar.gif'), url0, headers1)

request307 = createRequest(Test(307, 'GET poweredby.gif'), url0, headers1)

request308 = createRequest(Test(308, 'GET poweredBySpring.gif'), url0, headers1)

request309 = createRequest(Test(309, 'GET bkg-topbar.gif'), url0, headers1)

request401 = createRequest(Test(401, 'GET index.do'), url0)

request501 = createRequest(Test(501, 'POST feedUIEvent'), url1, headers2)

request601 = createRequest(Test(601, 'POST feedUIEvent'), url1, headers2)

request701 = createRequest(Test(701, 'GET fish_icon.gif'), url0, headers3)

request702 = createRequest(Test(702, 'GET dogs_icon.gif'), url0, headers3)

request703 = createRequest(Test(703, 'GET cats_icon.gif'), url0, headers3)

request704 = createRequest(Test(704, 'GET sm_dogs.gif'), url0, headers3)

request705 = createRequest(Test(705, 'GET sm_reptiles.gif'), url0, headers3)

request706 = createRequest(Test(706, 'GET sm_cats.gif'), url0, headers3)

request707 = createRequest(Test(707, 'GET sm_birds.gif'), url0, headers3)

request708 = createRequest(Test(708, 'GET sm_fish.gif'), url0, headers3)

request709 = createRequest(Test(709, 'GET reptiles_icon.gif'), url0, headers3)

request710 = createRequest(Test(710, 'GET birds_icon.gif'), url0, headers3)

request711 = createRequest(Test(711, 'GET splash.gif'), url0, headers3)

request712 = createRequest(Test(712, 'GET fresto_getip.js'), url0, headers4)

request801 = createRequest(Test(801, 'GET whatIsMyIPAddress'), url1, headers5)

request901 = createRequest(Test(901, 'GET jquery-1.10.2.js'), url0, headers4)

request902 = createRequest(Test(902, 'GET randomUUID.js'), url0, headers4)

request903 = createRequest(Test(903, 'GET fresto_link.js'), url0, headers4)

request1001 = createRequest(Test(1001, 'POST feedUIEvent'), url1, headers6)

request1101 = createRequest(Test(1101, 'GET viewCategory.do'), url0)

request1201 = createRequest(Test(1201, 'POST feedUIEvent'), url1, headers6)

request1301 = createRequest(Test(1301, 'GET fresto_getip.js'), url0, headers7)

request1302 = createRequest(Test(1302, 'GET jquery-1.10.2.js'), url0, headers7)

request1401 = createRequest(Test(1401, 'GET whatIsMyIPAddress'), url1)

request1501 = createRequest(Test(1501, 'GET randomUUID.js'), url0, headers7)

request1502 = createRequest(Test(1502, 'GET fresto_link.js'), url0, headers7)

request1601 = createRequest(Test(1601, 'POST feedUIEvent'), url1, headers8)

request1701 = createRequest(Test(1701, 'GET viewProduct.do'), url0)

request1801 = createRequest(Test(1801, 'POST feedUIEvent'), url1, headers8)

request1901 = createRequest(Test(1901, 'GET button_add_to_cart.gif'), url0)

request1902 = createRequest(Test(1902, 'GET fresto_getip.js'), url0, headers9)

request2001 = createRequest(Test(2001, 'GET whatIsMyIPAddress'), url1)

request2101 = createRequest(Test(2101, 'GET jquery-1.10.2.js'), url0, headers9)

request2102 = createRequest(Test(2102, 'GET randomUUID.js'), url0, headers9)

request2103 = createRequest(Test(2103, 'GET fresto_link.js'), url0, headers9)

request2201 = createRequest(Test(2201, 'POST feedUIEvent'), url1, headers10)

request2301 = createRequest(Test(2301, 'GET addItemToCart.do'), url0)

request2401 = createRequest(Test(2401, 'POST feedUIEvent'), url1, headers10)

request2501 = createRequest(Test(2501, 'GET fresto_getip.js'), url0, headers11)

request2601 = createRequest(Test(2601, 'GET whatIsMyIPAddress'), url1)

request2701 = createRequest(Test(2701, 'GET jquery-1.10.2.js'), url0, headers11)

request2702 = createRequest(Test(2702, 'GET randomUUID.js'), url0, headers11)

request2703 = createRequest(Test(2703, 'GET fresto_link.js'), url0, headers11)

request2801 = createRequest(Test(2801, 'POST feedUIEvent'), url1, headers12)

request2901 = createRequest(Test(2901, 'GET index.do'), url0)

request3001 = createRequest(Test(3001, 'POST feedUIEvent'), url1, headers12)

request3101 = createRequest(Test(3101, 'GET fresto_getip.js'), url0, headers4)

request3201 = createRequest(Test(3201, 'GET whatIsMyIPAddress'), url1, headers5)

request3301 = createRequest(Test(3301, 'GET jquery-1.10.2.js'), url0, headers4)

request3302 = createRequest(Test(3302, 'GET randomUUID.js'), url0, headers4)

request3303 = createRequest(Test(3303, 'GET fresto_link.js'), url0, headers4)

request3401 = createRequest(Test(3401, 'POST feedUIEvent'), url1, headers6)

request3501 = createRequest(Test(3501, 'GET viewCategory.do'), url0)

request3601 = createRequest(Test(3601, 'POST feedUIEvent'), url1, headers6)

request3701 = createRequest(Test(3701, 'GET fresto_getip.js'), url0, headers13)

request3801 = createRequest(Test(3801, 'GET whatIsMyIPAddress'), url1)

request3901 = createRequest(Test(3901, 'GET jquery-1.10.2.js'), url0, headers13)

request3902 = createRequest(Test(3902, 'GET randomUUID.js'), url0, headers13)

request3903 = createRequest(Test(3903, 'GET fresto_link.js'), url0, headers13)

request4001 = createRequest(Test(4001, 'POST feedUIEvent'), url1, headers14)

request4101 = createRequest(Test(4101, 'GET viewProduct.do'), url0)

request4201 = createRequest(Test(4201, 'POST feedUIEvent'), url1, headers14)

request4301 = createRequest(Test(4301, 'GET fresto_getip.js'), url0, headers15)

request4302 = createRequest(Test(4302, 'GET jquery-1.10.2.js'), url0, headers15)

request4401 = createRequest(Test(4401, 'GET whatIsMyIPAddress'), url1)

request4501 = createRequest(Test(4501, 'GET randomUUID.js'), url0, headers15)

request4502 = createRequest(Test(4502, 'GET fresto_link.js'), url0, headers15)

request4601 = createRequest(Test(4601, 'POST feedUIEvent'), url1, headers16)

request4701 = createRequest(Test(4701, 'GET addItemToCart.do'), url0)

request4801 = createRequest(Test(4801, 'POST feedUIEvent'), url1, headers16)

request4901 = createRequest(Test(4901, 'GET fresto_getip.js'), url0, headers17)

request5001 = createRequest(Test(5001, 'GET whatIsMyIPAddress'), url1)

request5101 = createRequest(Test(5101, 'GET jquery-1.10.2.js'), url0, headers17)

request5102 = createRequest(Test(5102, 'GET randomUUID.js'), url0, headers17)

request5103 = createRequest(Test(5103, 'GET fresto_link.js'), url0, headers17)

request5201 = createRequest(Test(5201, 'POST feedUIEvent'), url1, headers18)

request5301 = createRequest(Test(5301, 'GET index.do'), url0)

request5401 = createRequest(Test(5401, 'POST feedUIEvent'), url1, headers18)

request5501 = createRequest(Test(5501, 'GET fresto_getip.js'), url0, headers4)

request5601 = createRequest(Test(5601, 'GET whatIsMyIPAddress'), url1, headers5)

request5701 = createRequest(Test(5701, 'GET jquery-1.10.2.js'), url0, headers4)

request5702 = createRequest(Test(5702, 'GET randomUUID.js'), url0, headers4)

request5703 = createRequest(Test(5703, 'GET fresto_link.js'), url0, headers4)

request5801 = createRequest(Test(5801, 'POST feedUIEvent'), url1, headers6)

request5901 = createRequest(Test(5901, 'GET viewCategory.do'), url0)

request6001 = createRequest(Test(6001, 'POST feedUIEvent'), url1, headers6)

request6101 = createRequest(Test(6101, 'GET fresto_getip.js'), url0, headers19)

request6201 = createRequest(Test(6201, 'GET whatIsMyIPAddress'), url1, headers20)

request6301 = createRequest(Test(6301, 'GET jquery-1.10.2.js'), url0, headers19)

request6302 = createRequest(Test(6302, 'GET randomUUID.js'), url0, headers19)

request6303 = createRequest(Test(6303, 'GET fresto_link.js'), url0, headers19)

request6401 = createRequest(Test(6401, 'POST feedUIEvent'), url1, headers21)

request6501 = createRequest(Test(6501, 'GET viewProduct.do'), url0)

request6601 = createRequest(Test(6601, 'POST feedUIEvent'), url1, headers21)

request6701 = createRequest(Test(6701, 'GET fresto_getip.js'), url0, headers22)

request6702 = createRequest(Test(6702, 'GET jquery-1.10.2.js'), url0, headers22)

request6801 = createRequest(Test(6801, 'GET whatIsMyIPAddress'), url1)

request6901 = createRequest(Test(6901, 'GET randomUUID.js'), url0, headers22)

request6902 = createRequest(Test(6902, 'GET fresto_link.js'), url0, headers22)

request7001 = createRequest(Test(7001, 'POST feedUIEvent'), url1, headers23)

request7101 = createRequest(Test(7101, 'GET addItemToCart.do'), url0)

request7201 = createRequest(Test(7201, 'POST feedUIEvent'), url1, headers23)

request7301 = createRequest(Test(7301, 'GET fresto_getip.js'), url0, headers24)

request7401 = createRequest(Test(7401, 'GET whatIsMyIPAddress'), url1)

request7501 = createRequest(Test(7501, 'GET jquery-1.10.2.js'), url0, headers24)

request7502 = createRequest(Test(7502, 'GET randomUUID.js'), url0, headers24)

request7503 = createRequest(Test(7503, 'GET fresto_link.js'), url0, headers24)

request7601 = createRequest(Test(7601, 'POST feedUIEvent'), url1, headers25)

request7701 = createRequest(Test(7701, 'GET checkout.do'), url0)

request7801 = createRequest(Test(7801, 'POST feedUIEvent'), url1, headers25)

request7901 = createRequest(Test(7901, 'GET button_continue.gif'), url0)

request7902 = createRequest(Test(7902, 'GET fresto_getip.js'), url0, headers26)

request8001 = createRequest(Test(8001, 'GET whatIsMyIPAddress'), url1)

request8101 = createRequest(Test(8101, 'GET jquery-1.10.2.js'), url0, headers26)

request8102 = createRequest(Test(8102, 'GET randomUUID.js'), url0, headers26)

request8103 = createRequest(Test(8103, 'GET fresto_link.js'), url0, headers26)

request8201 = createRequest(Test(8201, 'POST feedUIEvent'), url1, headers27)

request8301 = createRequest(Test(8301, 'GET newOrder.do'), url0)

request8401 = createRequest(Test(8401, 'POST feedUIEvent'), url1, headers27)

request8501 = createRequest(Test(8501, 'GET button_submit.gif'), url0, headers28)

request8502 = createRequest(Test(8502, 'GET fresto_getip.js'), url0, headers29)

request8503 = createRequest(Test(8503, 'GET button_register_now.gif'), url0, headers28)

request8504 = createRequest(Test(8504, 'GET jquery-1.10.2.js'), url0, headers29)

request8601 = createRequest(Test(8601, 'GET whatIsMyIPAddress'), url1, headers30)

request8701 = createRequest(Test(8701, 'GET randomUUID.js'), url0, headers29)

request8702 = createRequest(Test(8702, 'GET fresto_link.js'), url0, headers29)

request8801 = createRequest(Test(8801, 'POST signon.do'), url0, headers31)

request8802 = createRequest(Test(8802, 'GET newOrder.do'), url0, headers31)

request8901 = createRequest(Test(8901, 'GET whatIsMyIPAddress'), url1, headers30)

request9001 = createRequest(Test(9001, 'GET my_account.gif'), url0, headers28)

request9002 = createRequest(Test(9002, 'GET sign-out.gif'), url0, headers28)

request9003 = createRequest(Test(9003, 'GET button_submit.gif'), url0, headers28)

request9101 = createRequest(Test(9101, 'POST newOrder.do'), url0, headers31)

request9201 = createRequest(Test(9201, 'GET whatIsMyIPAddress'), url1, headers30)

request9301 = createRequest(Test(9301, 'POST feedUIEvent'), url1, headers32)

request9401 = createRequest(Test(9401, 'GET newOrder.do'), url0)

request9501 = createRequest(Test(9501, 'POST feedUIEvent'), url1, headers32)

request9601 = createRequest(Test(9601, 'GET fresto_getip.js'), url0, headers33)

request9701 = createRequest(Test(9701, 'GET whatIsMyIPAddress'), url1)

request9801 = createRequest(Test(9801, 'GET jquery-1.10.2.js'), url0, headers33)

request9802 = createRequest(Test(9802, 'GET randomUUID.js'), url0, headers33)

request9803 = createRequest(Test(9803, 'GET fresto_link.js'), url0, headers33)

request9901 = createRequest(Test(9901, 'POST feedUIEvent'), url1, headers34)

request10001 = createRequest(Test(10001, 'GET viewCategory.do'), url0)

request10101 = createRequest(Test(10101, 'POST feedUIEvent'), url1, headers34)

request10201 = createRequest(Test(10201, 'GET fresto_getip.js'), url0, headers19)

request10301 = createRequest(Test(10301, 'GET whatIsMyIPAddress'), url1, headers20)

request10401 = createRequest(Test(10401, 'GET jquery-1.10.2.js'), url0, headers19)

request10402 = createRequest(Test(10402, 'GET randomUUID.js'), url0, headers19)

request10403 = createRequest(Test(10403, 'GET fresto_link.js'), url0, headers19)

request10501 = createRequest(Test(10501, 'POST feedUIEvent'), url1, headers21)

request10601 = createRequest(Test(10601, 'GET viewProduct.do'), url0)

request10701 = createRequest(Test(10701, 'POST feedUIEvent'), url1, headers21)

request10801 = createRequest(Test(10801, 'GET fresto_getip.js'), url0, headers35)

request10901 = createRequest(Test(10901, 'GET whatIsMyIPAddress'), url1)

request11001 = createRequest(Test(11001, 'GET jquery-1.10.2.js'), url0, headers35)

request11002 = createRequest(Test(11002, 'GET randomUUID.js'), url0, headers35)

request11003 = createRequest(Test(11003, 'GET fresto_link.js'), url0, headers35)

request11101 = createRequest(Test(11101, 'POST feedUIEvent'), url1, headers36)

request11201 = createRequest(Test(11201, 'GET addItemToCart.do'), url0)

request11301 = createRequest(Test(11301, 'POST feedUIEvent'), url1, headers36)

request11401 = createRequest(Test(11401, 'GET banner_dogs.gif'), url0)

request11402 = createRequest(Test(11402, 'GET fresto_getip.js'), url0, headers37)

request11501 = createRequest(Test(11501, 'GET whatIsMyIPAddress'), url1)

request11601 = createRequest(Test(11601, 'GET jquery-1.10.2.js'), url0, headers37)

request11602 = createRequest(Test(11602, 'GET randomUUID.js'), url0, headers37)

request11603 = createRequest(Test(11603, 'GET fresto_link.js'), url0, headers37)

request11701 = createRequest(Test(11701, 'POST feedUIEvent'), url1, headers38)

request11801 = createRequest(Test(11801, 'GET viewCart.do'), url0)

request11901 = createRequest(Test(11901, 'POST feedUIEvent'), url1, headers38)

request12001 = createRequest(Test(12001, 'GET fresto_getip.js'), url0, headers39)

request12002 = createRequest(Test(12002, 'GET jquery-1.10.2.js'), url0, headers39)

request12101 = createRequest(Test(12101, 'GET whatIsMyIPAddress'), url1)

request12201 = createRequest(Test(12201, 'GET randomUUID.js'), url0, headers39)

request12202 = createRequest(Test(12202, 'GET fresto_link.js'), url0, headers39)

request12301 = createRequest(Test(12301, 'POST feedUIEvent'), url1, headers40)

request12401 = createRequest(Test(12401, 'GET signoff.do'), url0)

request12501 = createRequest(Test(12501, 'POST feedUIEvent'), url1, headers40)

request12601 = createRequest(Test(12601, 'GET fresto_getip.js'), url0, headers41)

request12701 = createRequest(Test(12701, 'GET whatIsMyIPAddress'), url1)

request12801 = createRequest(Test(12801, 'GET jquery-1.10.2.js'), url0, headers41)

request12802 = createRequest(Test(12802, 'GET randomUUID.js'), url0, headers41)

request12803 = createRequest(Test(12803, 'GET fresto_link.js'), url0, headers41)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET / (requests 101-105)."""
    result = request101.GET('/jpetstoreLA/', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"2814-1379501484000\"'), ))

    grinder.sleep(76)
    request102.GET('/jpetstoreLA/js/fresto_getip.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"655-1379501484000\"'), ))

    request103.GET('/jpetstoreLA/js/jquery-1.10.2.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"273199-1379501484000\"'), ))

    request104.GET('/jpetstoreLA/js/randomUUID.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"1128-1379501484000\"'), ))

    request105.GET('/jpetstoreLA/js/fresto_link.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"1331-1379501484000\"'), ))

    return result

  def page2(self):
    """GET whatIsMyIPAddress (request 201)."""
    result = request201.GET('/whatIsMyIPAddress')

    return result

  def page3(self):
    """GET sign-in.gif (requests 301-309)."""
    result = request301.GET('/jpetstoreLA/images/sign-in.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"257-1379501484000\"'), ))

    grinder.sleep(68)
    request302.GET('/jpetstoreLA/images/cart.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"96-1379501484000\"'), ))

    request303.GET('/jpetstoreLA/images/separator.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"46-1379501484000\"'), ))

    request304.GET('/jpetstoreLA/images/search.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"323-1379501484000\"'), ))

    request305.GET('/jpetstoreLA/images/help.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"134-1379501484000\"'), ))

    request306.GET('/jpetstoreLA/images/logo-topbar.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"3808-1379501484000\"'), ))

    request307.GET('/jpetstoreLA/images/poweredby.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"2722-1379501484000\"'), ))

    request308.GET('/jpetstoreLA/images/poweredBySpring.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"2251-1379501484000\"'), ))

    request309.GET('/jpetstoreLA/images/bkg-topbar.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"959-1379501484000\"'), ))

    return result

  def page4(self):
    """GET index.do (request 401)."""
    result = request401.GET('/jpetstoreLA/shop/index.do', None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/'), ))
    # 14 different values for token_categoryId found in response, using the first one.
    self.token_categoryId = \
      httpUtilities.valueFromBodyURI('categoryId') # 'FISH'
    self.token_search = \
      httpUtilities.valueFromHiddenInput('search') # 'true'

    return result

  def page5(self):
    """POST feedUIEvent (request 501)."""
    result = request501.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page6(self):
    """POST feedUIEvent (request 601)."""
    result = request601.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '73'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page7(self):
    """GET fish_icon.gif (requests 701-712)."""
    result = request701.GET('/jpetstoreLA/images/fish_icon.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"439-1379501484000\"'), ))

    request702.GET('/jpetstoreLA/images/dogs_icon.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"468-1379501484000\"'), ))

    request703.GET('/jpetstoreLA/images/cats_icon.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"408-1379501484000\"'), ))

    request704.GET('/jpetstoreLA/images/sm_dogs.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"306-1379501484000\"'), ))

    request705.GET('/jpetstoreLA/images/sm_reptiles.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"398-1379501484000\"'), ))

    request706.GET('/jpetstoreLA/images/sm_cats.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"289-1379501484000\"'), ))

    request707.GET('/jpetstoreLA/images/sm_birds.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"251-1379501484000\"'), ))

    request708.GET('/jpetstoreLA/images/sm_fish.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"271-1379501484000\"'), ))

    grinder.sleep(13)
    request709.GET('/jpetstoreLA/images/reptiles_icon.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"669-1379501484000\"'), ))

    request710.GET('/jpetstoreLA/images/birds_icon.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"471-1379501484000\"'), ))

    request711.GET('/jpetstoreLA/images/splash.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"36097-1379501484000\"'), ))

    self.token__ = \
      '1379509162304'
    request712.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    return result

  def page8(self):
    """GET whatIsMyIPAddress (request 801)."""
    self.token__ = \
      '1379509162305'
    result = request801.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)

    return result

  def page9(self):
    """GET jquery-1.10.2.js (requests 901-903)."""
    self.token__ = \
      '1379509162306'
    result = request901.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    grinder.sleep(165)
    self.token__ = \
      '1379509162307'
    request902.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1379509162308'
    request903.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page10(self):
    """POST feedUIEvent (request 1001)."""
    result = request1001.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=BIRDS'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page11(self):
    """GET viewCategory.do (request 1101)."""
    self.token_categoryId = \
      'BIRDS'
    result = request1101.GET('/jpetstoreLA/shop/viewCategory.do' +
      '?categoryId=' +
      self.token_categoryId, None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'), ))
    # 5 different values for token_categoryId found in response, using the first one.
    self.token_categoryId = \
      httpUtilities.valueFromBodyURI('categoryId') # 'FISH'
    # 2 different values for token_productId found in response, using the first one.
    self.token_productId = \
      httpUtilities.valueFromBodyURI('productId') # 'AV-CB-01'

    return result

  def page12(self):
    """POST feedUIEvent (request 1201)."""
    result = request1201.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=BIRDS'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '155'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page13(self):
    """GET fresto_getip.js (requests 1301-1302)."""
    self.token__ = \
      '1379509164508'
    result = request1301.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    grinder.sleep(12)
    self.token__ = \
      '1379509164510'
    request1302.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    return result

  def page14(self):
    """GET whatIsMyIPAddress (request 1401)."""
    self.token__ = \
      '1379509164509'
    result = request1401.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__, None,
      ( NVPair('Accept', '*/*'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=BIRDS'), ))

    return result

  def page15(self):
    """GET randomUUID.js (requests 1501-1502)."""
    self.token__ = \
      '1379509164511'
    result = request1501.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(16)
    self.token__ = \
      '1379509164512'
    request1502.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page16(self):
    """POST feedUIEvent (request 1601)."""
    result = request1601.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=BIRDS'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=AV-SB-02'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page17(self):
    """GET viewProduct.do (request 1701)."""
    self.token_productId = \
      'AV-SB-02'
    result = request1701.GET('/jpetstoreLA/shop/viewProduct.do' +
      '?productId=' +
      self.token_productId, None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=BIRDS'), ))
    # 5 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.
    self.token_itemId = \
      httpUtilities.valueFromBodyURI('itemId') # 'EST-19'
    self.token_workingItemId = \
      httpUtilities.valueFromBodyURI('workingItemId') # 'EST-19'

    return result

  def page18(self):
    """POST feedUIEvent (request 1801)."""
    result = request1801.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=BIRDS'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=AV-SB-02'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '129'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page19(self):
    """GET button_add_to_cart.gif (requests 1901-1902)."""
    result = request1901.GET('/jpetstoreLA/images/button_add_to_cart.gif', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=AV-SB-02'),
        NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"481-1379501484000\"'), ))

    self.token__ = \
      '1379509167476'
    request1902.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    return result

  def page20(self):
    """GET whatIsMyIPAddress (request 2001)."""
    self.token__ = \
      '1379509167477'
    result = request2001.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__, None,
      ( NVPair('Accept', '*/*'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=AV-SB-02'), ))

    return result

  def page21(self):
    """GET jquery-1.10.2.js (requests 2101-2103)."""
    self.token__ = \
      '1379509167478'
    result = request2101.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    grinder.sleep(146)
    self.token__ = \
      '1379509167479'
    request2102.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(15)
    self.token__ = \
      '1379509167480'
    request2103.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page22(self):
    """POST feedUIEvent (request 2201)."""
    result = request2201.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=AV-SB-02'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-19'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page23(self):
    """GET addItemToCart.do (request 2301)."""
    result = request2301.GET('/jpetstoreLA/shop/addItemToCart.do' +
      '?workingItemId=' +
      self.token_workingItemId, None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=AV-SB-02'), ))
    # 4 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.

    return result

  def page24(self):
    """POST feedUIEvent (request 2401)."""
    result = request2401.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=AV-SB-02'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-19'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '77'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page25(self):
    """GET fresto_getip.js (request 2501)."""
    self.token__ = \
      '1379509168872'
    result = request2501.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    return result

  def page26(self):
    """GET whatIsMyIPAddress (request 2601)."""
    self.token__ = \
      '1379509168873'
    result = request2601.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__, None,
      ( NVPair('Accept', '*/*'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-19'), ))

    return result

  def page27(self):
    """GET jquery-1.10.2.js (requests 2701-2703)."""
    self.token__ = \
      '1379509168874'
    result = request2701.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    grinder.sleep(156)
    self.token__ = \
      '1379509168875'
    request2702.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(16)
    self.token__ = \
      '1379509168876'
    request2703.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page28(self):
    """POST feedUIEvent (request 2801)."""
    result = request2801.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-19'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page29(self):
    """GET index.do (request 2901)."""
    result = request2901.GET('/jpetstoreLA/shop/index.do', None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-19'), ))
    # 13 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.

    return result

  def page30(self):
    """POST feedUIEvent (request 3001)."""
    result = request3001.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-19'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '447'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page31(self):
    """GET fresto_getip.js (request 3101)."""
    self.token__ = \
      '1379509170506'
    result = request3101.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    return result

  def page32(self):
    """GET whatIsMyIPAddress (request 3201)."""
    self.token__ = \
      '1379509170507'
    result = request3201.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)

    return result

  def page33(self):
    """GET jquery-1.10.2.js (requests 3301-3303)."""
    self.token__ = \
      '1379509170508'
    result = request3301.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    grinder.sleep(231)
    self.token__ = \
      '1379509170509'
    request3302.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(16)
    self.token__ = \
      '1379509170510'
    request3303.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page34(self):
    """POST feedUIEvent (request 3401)."""
    result = request3401.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=REPTILES'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page35(self):
    """GET viewCategory.do (request 3501)."""
    self.token_categoryId = \
      'REPTILES'
    result = request3501.GET('/jpetstoreLA/shop/viewCategory.do' +
      '?categoryId=' +
      self.token_categoryId, None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'), ))
    # 5 different values for token_categoryId found in response, using the first one.
    self.token_categoryId = \
      httpUtilities.valueFromBodyURI('categoryId') # 'FISH'
    # 2 different values for token_productId found in response, using the first one.
    self.token_productId = \
      httpUtilities.valueFromBodyURI('productId') # 'RP-LI-02'

    return result

  def page36(self):
    """POST feedUIEvent (request 3601)."""
    result = request3601.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=REPTILES'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '326'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page37(self):
    """GET fresto_getip.js (request 3701)."""
    self.token__ = \
      '1379509178726'
    result = request3701.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    return result

  def page38(self):
    """GET whatIsMyIPAddress (request 3801)."""
    self.token__ = \
      '1379509178727'
    result = request3801.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__, None,
      ( NVPair('Accept', '*/*'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=REPTILES'), ))

    return result

  def page39(self):
    """GET jquery-1.10.2.js (requests 3901-3903)."""
    self.token__ = \
      '1379509178728'
    result = request3901.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    grinder.sleep(685)
    self.token__ = \
      '1379509178729'
    request3902.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(30)
    self.token__ = \
      '1379509178730'
    request3903.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page40(self):
    """POST feedUIEvent (request 4001)."""
    result = request4001.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=REPTILES'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=RP-SN-01'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page41(self):
    """GET viewProduct.do (request 4101)."""
    self.token_productId = \
      'RP-SN-01'
    result = request4101.GET('/jpetstoreLA/shop/viewProduct.do' +
      '?productId=' +
      self.token_productId, None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=REPTILES'), ))
    # 5 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.
    # 2 different values for token_itemId found in response, using the first one.
    self.token_itemId = \
      httpUtilities.valueFromBodyURI('itemId') # 'EST-11'
    # 2 different values for token_workingItemId found in response, using the first one.
    self.token_workingItemId = \
      httpUtilities.valueFromBodyURI('workingItemId') # 'EST-11'

    return result

  def page42(self):
    """POST feedUIEvent (request 4201)."""
    result = request4201.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=REPTILES'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=RP-SN-01'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '78'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page43(self):
    """GET fresto_getip.js (requests 4301-4302)."""
    self.token__ = \
      '1379509181121'
    result = request4301.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1379509181123'
    request4302.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    return result

  def page44(self):
    """GET whatIsMyIPAddress (request 4401)."""
    self.token__ = \
      '1379509181122'
    result = request4401.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__, None,
      ( NVPair('Accept', '*/*'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=RP-SN-01'), ))

    return result

  def page45(self):
    """GET randomUUID.js (requests 4501-4502)."""
    self.token__ = \
      '1379509181124'
    result = request4501.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(17)
    self.token__ = \
      '1379509181125'
    request4502.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page46(self):
    """POST feedUIEvent (request 4601)."""
    result = request4601.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=RP-SN-01'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-12'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page47(self):
    """GET addItemToCart.do (request 4701)."""
    self.token_workingItemId = \
      'EST-12'
    result = request4701.GET('/jpetstoreLA/shop/addItemToCart.do' +
      '?workingItemId=' +
      self.token_workingItemId, None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=RP-SN-01'), ))
    # 4 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.
    # 2 different values for token_itemId found in response, using the first one.
    self.token_itemId = \
      httpUtilities.valueFromBodyURI('itemId') # 'EST-19'
    # 2 different values for token_workingItemId found in response, using the first one.
    self.token_workingItemId = \
      httpUtilities.valueFromBodyURI('workingItemId') # 'EST-19'

    return result

  def page48(self):
    """POST feedUIEvent (request 4801)."""
    result = request4801.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=RP-SN-01'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-12'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '132'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page49(self):
    """GET fresto_getip.js (request 4901)."""
    self.token__ = \
      '1379509200288'
    result = request4901.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    return result

  def page50(self):
    """GET whatIsMyIPAddress (request 5001)."""
    self.token__ = \
      '1379509200289'
    result = request5001.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__, None,
      ( NVPair('Accept', '*/*'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-12'), ))

    return result

  def page51(self):
    """GET jquery-1.10.2.js (requests 5101-5103)."""
    self.token__ = \
      '1379509200290'
    result = request5101.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    grinder.sleep(144)
    self.token__ = \
      '1379509200291'
    request5102.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(16)
    self.token__ = \
      '1379509200292'
    request5103.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page52(self):
    """POST feedUIEvent (request 5201)."""
    result = request5201.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-12'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page53(self):
    """GET index.do (request 5301)."""
    result = request5301.GET('/jpetstoreLA/shop/index.do', None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-12'), ))
    # 13 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.

    return result

  def page54(self):
    """POST feedUIEvent (request 5401)."""
    result = request5401.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-12'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '88'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page55(self):
    """GET fresto_getip.js (request 5501)."""
    self.token__ = \
      '1379509203275'
    result = request5501.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    return result

  def page56(self):
    """GET whatIsMyIPAddress (request 5601)."""
    self.token__ = \
      '1379509203276'
    result = request5601.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)

    return result

  def page57(self):
    """GET jquery-1.10.2.js (requests 5701-5703)."""
    self.token__ = \
      '1379509203277'
    result = request5701.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    grinder.sleep(145)
    self.token__ = \
      '1379509203278'
    request5702.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(22)
    self.token__ = \
      '1379509203279'
    request5703.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page58(self):
    """POST feedUIEvent (request 5801)."""
    result = request5801.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=CATS'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page59(self):
    """GET viewCategory.do (request 5901)."""
    self.token_categoryId = \
      'CATS'
    result = request5901.GET('/jpetstoreLA/shop/viewCategory.do' +
      '?categoryId=' +
      self.token_categoryId, None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'), ))
    # 5 different values for token_categoryId found in response, using the first one.
    self.token_categoryId = \
      httpUtilities.valueFromBodyURI('categoryId') # 'FISH'
    # 2 different values for token_productId found in response, using the first one.
    self.token_productId = \
      httpUtilities.valueFromBodyURI('productId') # 'FL-DLH-02'

    return result

  def page60(self):
    """POST feedUIEvent (request 6001)."""
    result = request6001.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/index.do'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=CATS'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '184'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page61(self):
    """GET fresto_getip.js (request 6101)."""
    self.token__ = \
      '1379509205233'
    result = request6101.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    return result

  def page62(self):
    """GET whatIsMyIPAddress (request 6201)."""
    self.token__ = \
      '1379509205234'
    result = request6201.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)

    return result

  def page63(self):
    """GET jquery-1.10.2.js (requests 6301-6303)."""
    self.token__ = \
      '1379509205235'
    result = request6301.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    grinder.sleep(146)
    self.token__ = \
      '1379509205236'
    request6302.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(15)
    self.token__ = \
      '1379509205237'
    request6303.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page64(self):
    """POST feedUIEvent (request 6401)."""
    result = request6401.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=CATS'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DLH-02'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page65(self):
    """GET viewProduct.do (request 6501)."""
    result = request6501.GET('/jpetstoreLA/shop/viewProduct.do' +
      '?productId=' +
      self.token_productId, None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=CATS'), ))
    # 5 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.
    # 2 different values for token_itemId found in response, using the first one.
    self.token_itemId = \
      httpUtilities.valueFromBodyURI('itemId') # 'EST-16'
    # 2 different values for token_workingItemId found in response, using the first one.
    self.token_workingItemId = \
      httpUtilities.valueFromBodyURI('workingItemId') # 'EST-16'

    return result

  def page66(self):
    """POST feedUIEvent (request 6601)."""
    result = request6601.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=CATS'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DLH-02'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '52'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page67(self):
    """GET fresto_getip.js (requests 6701-6702)."""
    self.token__ = \
      '1379509206892'
    result = request6701.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    grinder.sleep(33)
    self.token__ = \
      '1379509206894'
    request6702.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    return result

  def page68(self):
    """GET whatIsMyIPAddress (request 6801)."""
    self.token__ = \
      '1379509206893'
    result = request6801.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__, None,
      ( NVPair('Accept', '*/*'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DLH-02'), ))

    return result

  def page69(self):
    """GET randomUUID.js (requests 6901-6902)."""
    self.token__ = \
      '1379509206895'
    result = request6901.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(15)
    self.token__ = \
      '1379509206896'
    request6902.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page70(self):
    """POST feedUIEvent (request 7001)."""
    result = request7001.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DLH-02'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-17'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page71(self):
    """GET addItemToCart.do (request 7101)."""
    self.token_workingItemId = \
      'EST-17'
    result = request7101.GET('/jpetstoreLA/shop/addItemToCart.do' +
      '?workingItemId=' +
      self.token_workingItemId, None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DLH-02'), ))
    # 4 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.
    # 3 different values for token_itemId found in response, using the first one.
    self.token_itemId = \
      httpUtilities.valueFromBodyURI('itemId') # 'EST-19'
    # 3 different values for token_workingItemId found in response, using the first one.
    self.token_workingItemId = \
      httpUtilities.valueFromBodyURI('workingItemId') # 'EST-19'

    return result

  def page72(self):
    """POST feedUIEvent (request 7201)."""
    result = request7201.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DLH-02'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-17'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '85'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page73(self):
    """GET fresto_getip.js (request 7301)."""
    self.token__ = \
      '1379509208619'
    result = request7301.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    return result

  def page74(self):
    """GET whatIsMyIPAddress (request 7401)."""
    self.token__ = \
      '1379509208620'
    result = request7401.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__, None,
      ( NVPair('Accept', '*/*'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-17'), ))

    return result

  def page75(self):
    """GET jquery-1.10.2.js (requests 7501-7503)."""
    self.token__ = \
      '1379509208621'
    result = request7501.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    grinder.sleep(141)
    self.token__ = \
      '1379509208622'
    request7502.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(15)
    self.token__ = \
      '1379509208623'
    request7503.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page76(self):
    """POST feedUIEvent (request 7601)."""
    result = request7601.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-17'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/checkout.do'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page77(self):
    """GET checkout.do (request 7701)."""
    result = request7701.GET('/jpetstoreLA/shop/checkout.do', None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-17'), ))
    # 4 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.
    # 2 different values for token_itemId found in response; the first matched
    # the last known value of token_itemId - don't update the variable.

    return result

  def page78(self):
    """POST feedUIEvent (request 7801)."""
    result = request7801.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-17'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/checkout.do'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '81'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page79(self):
    """GET button_continue.gif (requests 7901-7902)."""
    result = request7901.GET('/jpetstoreLA/images/button_continue.gif', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/checkout.do'),
        NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"1275-1379501484000\"'), ))

    self.token__ = \
      '1379509210325'
    request7902.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    return result

  def page80(self):
    """GET whatIsMyIPAddress (request 8001)."""
    self.token__ = \
      '1379509210326'
    result = request8001.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__, None,
      ( NVPair('Accept', '*/*'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/checkout.do'), ))

    return result

  def page81(self):
    """GET jquery-1.10.2.js (requests 8101-8103)."""
    self.token__ = \
      '1379509210327'
    result = request8101.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    grinder.sleep(146)
    self.token__ = \
      '1379509210328'
    request8102.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(15)
    self.token__ = \
      '1379509210329'
    request8103.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page82(self):
    """POST feedUIEvent (request 8201)."""
    result = request8201.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/checkout.do'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page83(self):
    """GET newOrder.do (request 8301)."""
    result = request8301.GET('/jpetstoreLA/shop/newOrder.do', None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/checkout.do'), ))
    # 4 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.
    self.token_forwardAction = \
      httpUtilities.valueFromHiddenInput('forwardAction') # '/jpetstoreLA/shop/newOrder.do'

    return result

  def page84(self):
    """POST feedUIEvent (request 8401)."""
    result = request8401.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/checkout.do'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '64'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page85(self):
    """GET button_submit.gif (requests 8501-8504)."""
    result = request8501.GET('/jpetstoreLA/images/button_submit.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"636-1379501484000\"'), ))

    self.token__ = \
      '1379509212022'
    request8502.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    request8503.GET('/jpetstoreLA/images/button_register_now.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"1115-1379501484000\"'), ))

    grinder.sleep(15)
    self.token__ = \
      '1379509212024'
    request8504.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    return result

  def page86(self):
    """GET whatIsMyIPAddress (request 8601)."""
    self.token__ = \
      '1379509212023'
    result = request8601.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)

    return result

  def page87(self):
    """GET randomUUID.js (requests 8701-8702)."""
    self.token__ = \
      '1379509212025'
    result = request8701.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(16)
    self.token__ = \
      '1379509212026'
    request8702.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page88(self):
    """POST signon.do (requests 8801-8802)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request8801.POST('/jpetstoreLA/shop/signon.do',
      ( NVPair('forwardAction', self.token_forwardAction),
        NVPair('username', 'j2ee'),
        NVPair('password', 'j2ee'),
        NVPair('update.x', '41'),
        NVPair('update.y', '4'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    grinder.sleep(12)
    request8802.GET('/jpetstoreLA/shop/newOrder.do')
    # 4 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.

    return result

  def page89(self):
    """GET whatIsMyIPAddress (request 8901)."""
    result = request8901.GET('/whatIsMyIPAddress')

    return result

  def page90(self):
    """GET my_account.gif (requests 9001-9003)."""
    result = request9001.GET('/jpetstoreLA/images/my_account.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"455-1379501484000\"'), ))

    request9002.GET('/jpetstoreLA/images/sign-out.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 18 Sep 2013 10:51:24 GMT'),
        NVPair('If-None-Match', 'W/\"290-1379501484000\"'), ))

    grinder.sleep(60)
    request9003.GET('/jpetstoreLA/shop/images/button_submit.gif')

    return result

  def page91(self):
    """POST newOrder.do (request 9101)."""
    result = request9101.POST('/jpetstoreLA/shop/newOrder.do',
      ( NVPair('order.cardType', 'Visa'),
        NVPair('order.creditCard', '999 9999 9999 9999'),
        NVPair('order.expiryDate', '12/03'),
        NVPair('order.billToFirstName', 'ABC'),
        NVPair('order.billToLastName', 'XYX'),
        NVPair('order.billAddress1', '901 San Antonio Road'),
        NVPair('order.billAddress2', 'MS UCUP02-206'),
        NVPair('order.billCity', 'Palo Alto'),
        NVPair('order.billState', 'CA'),
        NVPair('order.billZip', '94303'),
        NVPair('order.billCountry', 'USA'),
        NVPair('x', '0'),
        NVPair('y', '0'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))
    # 4 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.
    self.token__finish = \
      httpUtilities.valueFromBodyURI('_finish') # 'true'

    return result

  def page92(self):
    """GET whatIsMyIPAddress (request 9201)."""
    result = request9201.GET('/whatIsMyIPAddress')

    return result

  def page93(self):
    """POST feedUIEvent (request 9301)."""
    result = request9301.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do?_finish=true'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page94(self):
    """GET newOrder.do (request 9401)."""
    result = request9401.GET('/jpetstoreLA/shop/newOrder.do' +
      '?_finish=' +
      self.token__finish, None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do'), ))
    # 4 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.
    # 2 different values for token_itemId found in response; the first matched
    # the last known value of token_itemId - don't update the variable.

    return result

  def page95(self):
    """POST feedUIEvent (request 9501)."""
    result = request9501.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do?_finish=true'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '157'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page96(self):
    """GET fresto_getip.js (request 9601)."""
    self.token__ = \
      '1379509218768'
    result = request9601.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    return result

  def page97(self):
    """GET whatIsMyIPAddress (request 9701)."""
    self.token__ = \
      '1379509218769'
    result = request9701.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__, None,
      ( NVPair('Accept', '*/*'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do?_finish=true'), ))

    return result

  def page98(self):
    """GET jquery-1.10.2.js (requests 9801-9803)."""
    self.token__ = \
      '1379509218770'
    result = request9801.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    grinder.sleep(154)
    self.token__ = \
      '1379509218771'
    request9802.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(15)
    self.token__ = \
      '1379509218772'
    request9803.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page99(self):
    """POST feedUIEvent (request 9901)."""
    result = request9901.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do?_finish=true'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=CATS'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page100(self):
    """GET viewCategory.do (request 10001)."""
    self.token_categoryId = \
      'CATS'
    result = request10001.GET('/jpetstoreLA/shop/viewCategory.do' +
      '?categoryId=' +
      self.token_categoryId, None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do?_finish=true'), ))
    # 5 different values for token_categoryId found in response, using the first one.
    self.token_categoryId = \
      httpUtilities.valueFromBodyURI('categoryId') # 'FISH'
    # 1 different values for token_productId found in response; the first matched
    # the last known value of token_productId - don't update the variable.

    return result

  def page101(self):
    """POST feedUIEvent (request 10101)."""
    result = request10101.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/newOrder.do?_finish=true'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=CATS'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '129'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page102(self):
    """GET fresto_getip.js (request 10201)."""
    self.token__ = \
      '1379509221302'
    result = request10201.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    return result

  def page103(self):
    """GET whatIsMyIPAddress (request 10301)."""
    self.token__ = \
      '1379509221303'
    result = request10301.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)

    return result

  def page104(self):
    """GET jquery-1.10.2.js (requests 10401-10403)."""
    self.token__ = \
      '1379509221304'
    result = request10401.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    grinder.sleep(156)
    self.token__ = \
      '1379509221305'
    request10402.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(16)
    self.token__ = \
      '1379509221306'
    request10403.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page105(self):
    """POST feedUIEvent (request 10501)."""
    result = request10501.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=CATS'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DSH-01'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page106(self):
    """GET viewProduct.do (request 10601)."""
    self.token_productId = \
      'FL-DSH-01'
    result = request10601.GET('/jpetstoreLA/shop/viewProduct.do' +
      '?productId=' +
      self.token_productId, None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=CATS'), ))
    # 5 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.
    # 2 different values for token_itemId found in response, using the first one.
    self.token_itemId = \
      httpUtilities.valueFromBodyURI('itemId') # 'EST-14'
    # 2 different values for token_workingItemId found in response, using the first one.
    self.token_workingItemId = \
      httpUtilities.valueFromBodyURI('workingItemId') # 'EST-14'

    return result

  def page107(self):
    """POST feedUIEvent (request 10701)."""
    result = request10701.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCategory.do?categoryId=CATS'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DSH-01'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '162'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page108(self):
    """GET fresto_getip.js (request 10801)."""
    self.token__ = \
      '1379509232997'
    result = request10801.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    return result

  def page109(self):
    """GET whatIsMyIPAddress (request 10901)."""
    self.token__ = \
      '1379509232998'
    result = request10901.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__, None,
      ( NVPair('Accept', '*/*'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DSH-01'), ))

    return result

  def page110(self):
    """GET jquery-1.10.2.js (requests 11001-11003)."""
    self.token__ = \
      '1379509232999'
    result = request11001.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    grinder.sleep(147)
    self.token__ = \
      '1379509233000'
    request11002.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(38)
    self.token__ = \
      '1379509233001'
    request11003.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page111(self):
    """POST feedUIEvent (request 11101)."""
    result = request11101.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DSH-01'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-15'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page112(self):
    """GET addItemToCart.do (request 11201)."""
    self.token_workingItemId = \
      'EST-15'
    result = request11201.GET('/jpetstoreLA/shop/addItemToCart.do' +
      '?workingItemId=' +
      self.token_workingItemId, None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DSH-01'), ))
    # 4 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.
    self.token_itemId = \
      httpUtilities.valueFromBodyURI('itemId') # 'EST-15'
    # 4 different values for token_productId found in response, using the first one.
    self.token_productId = \
      httpUtilities.valueFromBodyURI('productId') # 'K9-BD-01'
    self.token_page = \
      httpUtilities.valueFromBodyURI('page') # 'next'

    return result

  def page113(self):
    """POST feedUIEvent (request 11301)."""
    result = request11301.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewProduct.do?productId=FL-DSH-01'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-15'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '178'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page114(self):
    """GET banner_dogs.gif (requests 11401-11402)."""
    result = request11401.GET('/jpetstoreLA/images/banner_dogs.gif', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-15'), ))

    self.token__ = \
      '1379509234937'
    request11402.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    return result

  def page115(self):
    """GET whatIsMyIPAddress (request 11501)."""
    self.token__ = \
      '1379509234938'
    result = request11501.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__, None,
      ( NVPair('Accept', '*/*'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-15'), ))

    return result

  def page116(self):
    """GET jquery-1.10.2.js (requests 11601-11603)."""
    self.token__ = \
      '1379509234939'
    result = request11601.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    grinder.sleep(145)
    self.token__ = \
      '1379509234940'
    request11602.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(15)
    self.token__ = \
      '1379509234941'
    request11603.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page117(self):
    """POST feedUIEvent (request 11701)."""
    result = request11701.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-15'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCart.do?page=next'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page118(self):
    """GET viewCart.do (request 11801)."""
    result = request11801.GET('/jpetstoreLA/shop/viewCart.do' +
      '?page=' +
      self.token_page, None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-15'), ))
    # 4 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.
    # 2 different values for token_productId found in response, using the first one.
    self.token_productId = \
      httpUtilities.valueFromBodyURI('productId') # 'K9-RT-01'
    self.token_page = \
      httpUtilities.valueFromBodyURI('page') # 'previous'

    return result

  def page119(self):
    """POST feedUIEvent (request 11901)."""
    result = request11901.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/addItemToCart.do?workingItemId=EST-15'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCart.do?page=next'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '192'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page120(self):
    """GET fresto_getip.js (requests 12001-12002)."""
    self.token__ = \
      '1379509236175'
    result = request12001.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1379509236177'
    request12002.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    return result

  def page121(self):
    """GET whatIsMyIPAddress (request 12101)."""
    self.token__ = \
      '1379509236176'
    result = request12101.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__, None,
      ( NVPair('Accept', '*/*'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCart.do?page=next'), ))

    return result

  def page122(self):
    """GET randomUUID.js (requests 12201-12202)."""
    self.token__ = \
      '1379509236178'
    result = request12201.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(14)
    self.token__ = \
      '1379509236179'
    request12202.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def page123(self):
    """POST feedUIEvent (request 12301)."""
    result = request12301.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCart.do?page=next'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/signoff.do'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page124(self):
    """GET signoff.do (request 12401)."""
    result = request12401.GET('/jpetstoreLA/shop/signoff.do', None,
      ( NVPair('Accept', '*/*'),
        NVPair('fresto-uuid', getUUID(grinder.threadNumber)),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCart.do?page=next'), ))
    # 13 different values for token_categoryId found in response; the first matched
    # the last known value of token_categoryId - don't update the variable.

    return result

  def page125(self):
    """POST feedUIEvent (request 12501)."""
    result = request12501.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', clientIp),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreLA/shop/viewCart.do?page=next'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreLA/shop/signoff.do'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '177'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page126(self):
    """GET fresto_getip.js (request 12601)."""
    self.token__ = \
      '1379509243679'
    result = request12601.GET('/jpetstoreLA/js/fresto_getip.js' +
      '?_=' +
      self.token__)

    return result

  def page127(self):
    """GET whatIsMyIPAddress (request 12701)."""
    self.token__ = \
      '1379509243680'
    result = request12701.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__, None,
      ( NVPair('Accept', '*/*'),
        NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreLA/shop/signoff.do'), ))

    return result

  def page128(self):
    """GET jquery-1.10.2.js (requests 12801-12803)."""
    self.token__ = \
      '1379509243681'
    result = request12801.GET('/jpetstoreLA/js/jquery-1.10.2.js' +
      '?_=' +
      self.token__)

    grinder.sleep(150)
    self.token__ = \
      '1379509243682'
    request12802.GET('/jpetstoreLA/js/randomUUID.js' +
      '?_=' +
      self.token__)

    grinder.sleep(15)
    self.token__ = \
      '1379509243683'
    request12803.GET('/jpetstoreLA/js/fresto_link.js' +
      '?_=' +
      self.token__)

    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    self.page1()      # GET / (requests 101-105)

    grinder.sleep(676)
    self.page2()      # GET whatIsMyIPAddress (request 201)
    self.page3()      # GET sign-in.gif (requests 301-309)

    grinder.sleep(1815)
    self.page5()      # POST feedUIEvent (request 501)
    self.page4()      # GET index.do (request 401)

    grinder.sleep(39)
    self.page6()      # POST feedUIEvent (request 601)
    self.page7()      # GET fish_icon.gif (requests 701-712)

    grinder.sleep(19)
    self.page8()      # GET whatIsMyIPAddress (request 801)
    self.page9()      # GET jquery-1.10.2.js (requests 901-903)

    grinder.sleep(2526)
    self.page10()     # POST feedUIEvent (request 1001)
    self.page11()     # GET viewCategory.do (request 1101)

    grinder.sleep(53)
    self.page12()     # POST feedUIEvent (request 1201)
    self.page13()     # GET fresto_getip.js (requests 1301-1302)
    self.page14()     # GET whatIsMyIPAddress (request 1401)

    grinder.sleep(172)
    self.page15()     # GET randomUUID.js (requests 1501-1502)

    grinder.sleep(1012)
    self.page16()     # POST feedUIEvent (request 1601)
    self.page17()     # GET viewProduct.do (request 1701)

    grinder.sleep(48)
    self.page18()     # POST feedUIEvent (request 1801)
    self.page19()     # GET button_add_to_cart.gif (requests 1901-1902)

    grinder.sleep(11)
    self.page20()     # GET whatIsMyIPAddress (request 2001)
    self.page21()     # GET jquery-1.10.2.js (requests 2101-2103)

    grinder.sleep(1308)
    self.page22()     # POST feedUIEvent (request 2201)
    self.page23()     # GET addItemToCart.do (request 2301)

    grinder.sleep(23)
    self.page24()     # POST feedUIEvent (request 2401)
    self.page25()     # GET fresto_getip.js (request 2501)

    grinder.sleep(17)
    self.page26()     # GET whatIsMyIPAddress (request 2601)
    self.page27()     # GET jquery-1.10.2.js (requests 2701-2703)

    grinder.sleep(7417)
    self.page28()     # POST feedUIEvent (request 2801)
    self.page29()     # GET index.do (request 2901)

    grinder.sleep(70)
    self.page30()     # POST feedUIEvent (request 3001)
    self.page31()     # GET fresto_getip.js (request 3101)

    grinder.sleep(29)
    self.page32()     # GET whatIsMyIPAddress (request 3201)
    self.page33()     # GET jquery-1.10.2.js (requests 3301-3303)

    grinder.sleep(790)
    self.page34()     # POST feedUIEvent (request 3401)
    self.page35()     # GET viewCategory.do (request 3501)

    grinder.sleep(38)
    self.page36()     # POST feedUIEvent (request 3601)
    self.page37()     # GET fresto_getip.js (request 3701)

    grinder.sleep(25)
    self.page38()     # GET whatIsMyIPAddress (request 3801)
    self.page39()     # GET jquery-1.10.2.js (requests 3901-3903)

    grinder.sleep(18816)
    self.page40()     # POST feedUIEvent (request 4001)
    self.page41()     # GET viewProduct.do (request 4101)

    grinder.sleep(22)
    self.page42()     # POST feedUIEvent (request 4201)
    self.page43()     # GET fresto_getip.js (requests 4301-4302)
    self.page44()     # GET whatIsMyIPAddress (request 4401)

    grinder.sleep(148)
    self.page45()     # GET randomUUID.js (requests 4501-4502)

    grinder.sleep(2604)
    self.page46()     # POST feedUIEvent (request 4601)
    self.page47()     # GET addItemToCart.do (request 4701)

    grinder.sleep(42)
    self.page48()     # POST feedUIEvent (request 4801)
    self.page49()     # GET fresto_getip.js (request 4901)
    self.page50()     # GET whatIsMyIPAddress (request 5001)
    self.page51()     # GET jquery-1.10.2.js (requests 5101-5103)

    grinder.sleep(1608)
    self.page52()     # POST feedUIEvent (request 5201)
    self.page53()     # GET index.do (request 5301)

    grinder.sleep(58)
    self.page54()     # POST feedUIEvent (request 5401)
    self.page55()     # GET fresto_getip.js (request 5501)
    self.page56()     # GET whatIsMyIPAddress (request 5601)
    self.page57()     # GET jquery-1.10.2.js (requests 5701-5703)

    grinder.sleep(1118)
    self.page58()     # POST feedUIEvent (request 5801)
    self.page59()     # GET viewCategory.do (request 5901)

    grinder.sleep(86)
    self.page60()     # POST feedUIEvent (request 6001)
    self.page61()     # GET fresto_getip.js (request 6101)

    grinder.sleep(20)
    self.page62()     # GET whatIsMyIPAddress (request 6201)
    self.page63()     # GET jquery-1.10.2.js (requests 6301-6303)

    grinder.sleep(1390)
    self.page64()     # POST feedUIEvent (request 6401)
    self.page65()     # GET viewProduct.do (request 6501)

    grinder.sleep(28)
    self.page66()     # POST feedUIEvent (request 6601)
    self.page67()     # GET fresto_getip.js (requests 6701-6702)
    self.page68()     # GET whatIsMyIPAddress (request 6801)

    grinder.sleep(150)
    self.page69()     # GET randomUUID.js (requests 6901-6902)

    grinder.sleep(1309)
    self.page70()     # POST feedUIEvent (request 7001)
    self.page71()     # GET addItemToCart.do (request 7101)

    grinder.sleep(23)
    self.page72()     # POST feedUIEvent (request 7201)
    self.page73()     # GET fresto_getip.js (request 7301)

    grinder.sleep(14)
    self.page74()     # GET whatIsMyIPAddress (request 7401)
    self.page75()     # GET jquery-1.10.2.js (requests 7501-7503)

    grinder.sleep(1321)
    self.page76()     # POST feedUIEvent (request 7601)
    self.page77()     # GET checkout.do (request 7701)

    grinder.sleep(45)
    self.page78()     # POST feedUIEvent (request 7801)
    self.page79()     # GET button_continue.gif (requests 7901-7902)
    self.page80()     # GET whatIsMyIPAddress (request 8001)

    grinder.sleep(45)
    self.page81()     # GET jquery-1.10.2.js (requests 8101-8103)

    grinder.sleep(1278)
    self.page82()     # POST feedUIEvent (request 8201)
    self.page83()     # GET newOrder.do (request 8301)

    grinder.sleep(46)
    self.page84()     # POST feedUIEvent (request 8401)
    self.page85()     # GET button_submit.gif (requests 8501-8504)
    self.page86()     # GET whatIsMyIPAddress (request 8601)

    grinder.sleep(142)
    self.page87()     # GET randomUUID.js (requests 8701-8702)

    grinder.sleep(1494)
    self.page88()     # POST signon.do (requests 8801-8802)

    grinder.sleep(166)
    self.page89()     # GET whatIsMyIPAddress (request 8901)
    self.page90()     # GET my_account.gif (requests 9001-9003)

    grinder.sleep(2967)
    self.page91()     # POST newOrder.do (request 9101)

    grinder.sleep(71)
    self.page92()     # GET whatIsMyIPAddress (request 9201)

    grinder.sleep(2199)
    self.page93()     # POST feedUIEvent (request 9301)
    self.page94()     # GET newOrder.do (request 9401)

    grinder.sleep(53)
    self.page95()     # POST feedUIEvent (request 9501)
    self.page96()     # GET fresto_getip.js (request 9601)
    self.page97()     # GET whatIsMyIPAddress (request 9701)
    self.page98()     # GET jquery-1.10.2.js (requests 9801-9803)

    grinder.sleep(11291)
    self.page99()     # POST feedUIEvent (request 9901)
    self.page100()    # GET viewCategory.do (request 10001)

    grinder.sleep(61)
    self.page101()    # POST feedUIEvent (request 10101)
    self.page102()    # GET fresto_getip.js (request 10201)
    self.page103()    # GET whatIsMyIPAddress (request 10301)
    self.page104()    # GET jquery-1.10.2.js (requests 10401-10403)

    grinder.sleep(1516)
    self.page105()    # POST feedUIEvent (request 10501)
    self.page106()    # GET viewProduct.do (request 10601)

    grinder.sleep(54)
    self.page107()    # POST feedUIEvent (request 10701)
    self.page108()    # GET fresto_getip.js (request 10801)
    self.page109()    # GET whatIsMyIPAddress (request 10901)
    self.page110()    # GET jquery-1.10.2.js (requests 11001-11003)

    grinder.sleep(779)
    self.page111()    # POST feedUIEvent (request 11101)
    self.page112()    # GET addItemToCart.do (request 11201)

    grinder.sleep(66)
    self.page113()    # POST feedUIEvent (request 11301)
    self.page114()    # GET banner_dogs.gif (requests 11401-11402)
    self.page115()    # GET whatIsMyIPAddress (request 11501)
    self.page116()    # GET jquery-1.10.2.js (requests 11601-11603)

    grinder.sleep(6964)
    self.page117()    # POST feedUIEvent (request 11701)
    self.page118()    # GET viewCart.do (request 11801)

    grinder.sleep(124)
    self.page119()    # POST feedUIEvent (request 11901)
    self.page120()    # GET fresto_getip.js (requests 12001-12002)

    grinder.sleep(34)
    self.page121()    # GET whatIsMyIPAddress (request 12101)

    grinder.sleep(156)
    self.page122()    # GET randomUUID.js (requests 12201-12202)

    grinder.sleep(5376)
    self.page123()    # POST feedUIEvent (request 12301)
    self.page124()    # GET signoff.do (request 12401)

    grinder.sleep(71)
    self.page125()    # POST feedUIEvent (request 12501)
    self.page126()    # GET fresto_getip.js (request 12601)
    self.page127()    # GET whatIsMyIPAddress (request 12701)
    self.page128()    # GET jquery-1.10.2.js (requests 12801-12803)


# Instrument page methods.
Test(100, 'Page 1').record(TestRunner.page1)
Test(200, 'Page 2').record(TestRunner.page2)
Test(300, 'Page 3').record(TestRunner.page3)
Test(400, 'Page 4').record(TestRunner.page4)
Test(500, 'Page 5').record(TestRunner.page5)
Test(600, 'Page 6').record(TestRunner.page6)
Test(700, 'Page 7').record(TestRunner.page7)
Test(800, 'Page 8').record(TestRunner.page8)
Test(900, 'Page 9').record(TestRunner.page9)
Test(1000, 'Page 10').record(TestRunner.page10)
Test(1100, 'Page 11').record(TestRunner.page11)
Test(1200, 'Page 12').record(TestRunner.page12)
Test(1300, 'Page 13').record(TestRunner.page13)
Test(1400, 'Page 14').record(TestRunner.page14)
Test(1500, 'Page 15').record(TestRunner.page15)
Test(1600, 'Page 16').record(TestRunner.page16)
Test(1700, 'Page 17').record(TestRunner.page17)
Test(1800, 'Page 18').record(TestRunner.page18)
Test(1900, 'Page 19').record(TestRunner.page19)
Test(2000, 'Page 20').record(TestRunner.page20)
Test(2100, 'Page 21').record(TestRunner.page21)
Test(2200, 'Page 22').record(TestRunner.page22)
Test(2300, 'Page 23').record(TestRunner.page23)
Test(2400, 'Page 24').record(TestRunner.page24)
Test(2500, 'Page 25').record(TestRunner.page25)
Test(2600, 'Page 26').record(TestRunner.page26)
Test(2700, 'Page 27').record(TestRunner.page27)
Test(2800, 'Page 28').record(TestRunner.page28)
Test(2900, 'Page 29').record(TestRunner.page29)
Test(3000, 'Page 30').record(TestRunner.page30)
Test(3100, 'Page 31').record(TestRunner.page31)
Test(3200, 'Page 32').record(TestRunner.page32)
Test(3300, 'Page 33').record(TestRunner.page33)
Test(3400, 'Page 34').record(TestRunner.page34)
Test(3500, 'Page 35').record(TestRunner.page35)
Test(3600, 'Page 36').record(TestRunner.page36)
Test(3700, 'Page 37').record(TestRunner.page37)
Test(3800, 'Page 38').record(TestRunner.page38)
Test(3900, 'Page 39').record(TestRunner.page39)
Test(4000, 'Page 40').record(TestRunner.page40)
Test(4100, 'Page 41').record(TestRunner.page41)
Test(4200, 'Page 42').record(TestRunner.page42)
Test(4300, 'Page 43').record(TestRunner.page43)
Test(4400, 'Page 44').record(TestRunner.page44)
Test(4500, 'Page 45').record(TestRunner.page45)
Test(4600, 'Page 46').record(TestRunner.page46)
Test(4700, 'Page 47').record(TestRunner.page47)
Test(4800, 'Page 48').record(TestRunner.page48)
Test(4900, 'Page 49').record(TestRunner.page49)
Test(5000, 'Page 50').record(TestRunner.page50)
Test(5100, 'Page 51').record(TestRunner.page51)
Test(5200, 'Page 52').record(TestRunner.page52)
Test(5300, 'Page 53').record(TestRunner.page53)
Test(5400, 'Page 54').record(TestRunner.page54)
Test(5500, 'Page 55').record(TestRunner.page55)
Test(5600, 'Page 56').record(TestRunner.page56)
Test(5700, 'Page 57').record(TestRunner.page57)
Test(5800, 'Page 58').record(TestRunner.page58)
Test(5900, 'Page 59').record(TestRunner.page59)
Test(6000, 'Page 60').record(TestRunner.page60)
Test(6100, 'Page 61').record(TestRunner.page61)
Test(6200, 'Page 62').record(TestRunner.page62)
Test(6300, 'Page 63').record(TestRunner.page63)
Test(6400, 'Page 64').record(TestRunner.page64)
Test(6500, 'Page 65').record(TestRunner.page65)
Test(6600, 'Page 66').record(TestRunner.page66)
Test(6700, 'Page 67').record(TestRunner.page67)
Test(6800, 'Page 68').record(TestRunner.page68)
Test(6900, 'Page 69').record(TestRunner.page69)
Test(7000, 'Page 70').record(TestRunner.page70)
Test(7100, 'Page 71').record(TestRunner.page71)
Test(7200, 'Page 72').record(TestRunner.page72)
Test(7300, 'Page 73').record(TestRunner.page73)
Test(7400, 'Page 74').record(TestRunner.page74)
Test(7500, 'Page 75').record(TestRunner.page75)
Test(7600, 'Page 76').record(TestRunner.page76)
Test(7700, 'Page 77').record(TestRunner.page77)
Test(7800, 'Page 78').record(TestRunner.page78)
Test(7900, 'Page 79').record(TestRunner.page79)
Test(8000, 'Page 80').record(TestRunner.page80)
Test(8100, 'Page 81').record(TestRunner.page81)
Test(8200, 'Page 82').record(TestRunner.page82)
Test(8300, 'Page 83').record(TestRunner.page83)
Test(8400, 'Page 84').record(TestRunner.page84)
Test(8500, 'Page 85').record(TestRunner.page85)
Test(8600, 'Page 86').record(TestRunner.page86)
Test(8700, 'Page 87').record(TestRunner.page87)
Test(8800, 'Page 88').record(TestRunner.page88)
Test(8900, 'Page 89').record(TestRunner.page89)
Test(9000, 'Page 90').record(TestRunner.page90)
Test(9100, 'Page 91').record(TestRunner.page91)
Test(9200, 'Page 92').record(TestRunner.page92)
Test(9300, 'Page 93').record(TestRunner.page93)
Test(9400, 'Page 94').record(TestRunner.page94)
Test(9500, 'Page 95').record(TestRunner.page95)
Test(9600, 'Page 96').record(TestRunner.page96)
Test(9700, 'Page 97').record(TestRunner.page97)
Test(9800, 'Page 98').record(TestRunner.page98)
Test(9900, 'Page 99').record(TestRunner.page99)
Test(10000, 'Page 100').record(TestRunner.page100)
Test(10100, 'Page 101').record(TestRunner.page101)
Test(10200, 'Page 102').record(TestRunner.page102)
Test(10300, 'Page 103').record(TestRunner.page103)
Test(10400, 'Page 104').record(TestRunner.page104)
Test(10500, 'Page 105').record(TestRunner.page105)
Test(10600, 'Page 106').record(TestRunner.page106)
Test(10700, 'Page 107').record(TestRunner.page107)
Test(10800, 'Page 108').record(TestRunner.page108)
Test(10900, 'Page 109').record(TestRunner.page109)
Test(11000, 'Page 110').record(TestRunner.page110)
Test(11100, 'Page 111').record(TestRunner.page111)
Test(11200, 'Page 112').record(TestRunner.page112)
Test(11300, 'Page 113').record(TestRunner.page113)
Test(11400, 'Page 114').record(TestRunner.page114)
Test(11500, 'Page 115').record(TestRunner.page115)
Test(11600, 'Page 116').record(TestRunner.page116)
Test(11700, 'Page 117').record(TestRunner.page117)
Test(11800, 'Page 118').record(TestRunner.page118)
Test(11900, 'Page 119').record(TestRunner.page119)
Test(12000, 'Page 120').record(TestRunner.page120)
Test(12100, 'Page 121').record(TestRunner.page121)
Test(12200, 'Page 122').record(TestRunner.page122)
Test(12300, 'Page 123').record(TestRunner.page123)
Test(12400, 'Page 124').record(TestRunner.page124)
Test(12500, 'Page 125').record(TestRunner.page125)
Test(12600, 'Page 126').record(TestRunner.page126)
Test(12700, 'Page 127').record(TestRunner.page127)
Test(12800, 'Page 128').record(TestRunner.page128)
