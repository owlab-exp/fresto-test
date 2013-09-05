# The Grinder 3.11
# HTTP script recorded by TCPProxy at Sep 3, 2013 12:56:41 AM
from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()
# My Imports
import time
from java.util import UUID

def timestr():
	return str(int(round(time.time() * 1000)))

appHost = 'beta.owlab.com'
appPort = '8080'
monitorHost = 'fresto1.owlab.com'
monitorPort = '9999'

#workerList = []
#def createWorker(workerIndex) :
#	uuidList = []
#	workerList.insert(index,uuidList)
#
#def addUUID(workerIndex, uuidIndex) :
#	uuidList = workerList[workerIndex]
#	uuidList.insert(uuidIndex, UUID.randomUUID().toString())
#	return uuidList[uuidIndex]
#
#def getUUID(workerIndex, uuidIndex) :
#	uuidList = workerList[workerIndex]
#	return uuidList[uuidIndex]
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
    NVPair('Referer', 'http://beta.owlab.com:8080/jpetstoreL/'),
    NVPair('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'), ]
headers0= \
  [ NVPair('Accept', '*/*'), ]
headers1= \
  [ NVPair('Accept', '*/*'),
    NVPair('Cache-Control', 'no-cache'), ]
headers2= \
  [ NVPair('Accept', 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'), ]

url0 = 'http://' + monitorHost + ':' + monitorPort

request101 = createRequest(Test(101, 'GET whatIsMyIPAddress'), url0, headers0)
request201 = createRequest(Test(201, 'POST feedUIEvent'), url0, headers1)
request401 = createRequest(Test(401, 'POST feedUIEvent'), url0, headers1)
request601 = createRequest(Test(601, 'GET whatIsMyIPAddress'), url0, headers0)
request801 = createRequest(Test(801, 'POST feedUIEvent'), url0, headers1)
request1001 = createRequest(Test(1001, 'POST feedUIEvent'), url0, headers1)
request1201 = createRequest(Test(1201, 'GET whatIsMyIPAddress'), url0, headers0)
request1401 = createRequest(Test(1401, 'POST feedUIEvent'), url0, headers1)
request1601 = createRequest(Test(1601, 'POST feedUIEvent'), url0, headers1)
request1801 = createRequest(Test(1801, 'GET whatIsMyIPAddress'), url0, headers0)
request2001 = createRequest(Test(2001, 'POST feedUIEvent'), url0, headers1)
request2201 = createRequest(Test(2201, 'POST feedUIEvent'), url0, headers1)
request2401 = createRequest(Test(2401, 'GET whatIsMyIPAddress'), url0, headers0)
request2601 = createRequest(Test(2601, 'POST feedUIEvent'), url0, headers1)
request2801 = createRequest(Test(2801, 'POST feedUIEvent'), url0, headers1)
request3001 = createRequest(Test(3001, 'GET whatIsMyIPAddress'), url0, headers0)
request3201 = createRequest(Test(3201, 'POST feedUIEvent'), url0, headers1)
request3401 = createRequest(Test(3401, 'POST feedUIEvent'), url0, headers1)
request3601 = createRequest(Test(3601, 'GET whatIsMyIPAddress'), url0, headers0)
request3801 = createRequest(Test(3801, 'POST feedUIEvent'), url0, headers1)
request4001 = createRequest(Test(4001, 'POST feedUIEvent'), url0, headers1)
request4201 = createRequest(Test(4201, 'GET whatIsMyIPAddress'), url0, headers0)
request4401 = createRequest(Test(4401, 'POST feedUIEvent'), url0, headers1)
request4601 = createRequest(Test(4601, 'POST feedUIEvent'), url0, headers1)
request4801 = createRequest(Test(4801, 'GET whatIsMyIPAddress'), url0, headers0)
request5001 = createRequest(Test(5001, 'POST feedUIEvent'), url0, headers1)
request5201 = createRequest(Test(5201, 'POST feedUIEvent'), url0, headers1)
request5401 = createRequest(Test(5401, 'GET whatIsMyIPAddress'), url0, headers0)
request5601 = createRequest(Test(5601, 'POST feedUIEvent'), url0, headers1)
request5801 = createRequest(Test(5801, 'POST feedUIEvent'), url0, headers1)
request6001 = createRequest(Test(6001, 'GET whatIsMyIPAddress'), url0, headers0)
request6201 = createRequest(Test(6201, 'POST feedUIEvent'), url0, headers1)
request6401 = createRequest(Test(6401, 'POST feedUIEvent'), url0, headers1)
request6601 = createRequest(Test(6601, 'GET whatIsMyIPAddress'), url0, headers0)

class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  def page1(self):
    """GET whatIsMyIPAddress (request 101)."""
    result = request101.GET('/whatIsMyIPAddress')
    return result

  def page2(self):
    """POST feedUIEvent (request 201)."""
    result = request201.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/index.do'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page4(self):
    """POST feedUIEvent (request 401)."""
    result = request401.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/index.do'),
        #NVPair('timestamp', timestr()),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '195'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page6(self):
    """GET whatIsMyIPAddress (request 601)."""
    self.token__ = \
      timestr()
    result = request601.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)
    return result

  def page8(self):
    """POST feedUIEvent (request 801)."""
    result = request801.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/viewCategory.do?categoryId=DOGS'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page10(self):
    """POST feedUIEvent (request 1001)."""
    result = request1001.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/viewCategory.do?categoryId=DOGS'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '157'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page12(self):
    """GET whatIsMyIPAddress (request 1201)."""
    self.token__ = \
      timestr()
    result = request1201.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)
    return result

  def page14(self):
    """POST feedUIEvent (request 1401)."""
    result = request1401.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/viewProduct.do?productId=K9-DL-01'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page16(self):
    """POST feedUIEvent (request 1601)."""
    result = request1601.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/viewProduct.do?productId=K9-DL-01'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '84'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page18(self):
    """GET whatIsMyIPAddress (request 1801)."""
    self.token__ = \
      timestr()
    result = request1801.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)
    return result

  def page20(self):
    """POST feedUIEvent (request 2001)."""
    result = request2001.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/addItemToCart.do?workingItemId=EST-10'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page22(self):
    """POST feedUIEvent (request 2201)."""
    result = request2201.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/addItemToCart.do?workingItemId=EST-10'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '118'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page24(self):
    """GET whatIsMyIPAddress (request 2401)."""
    self.token__ = \
      timestr()
    result = request2401.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)
    return result

  def page26(self):
    """POST feedUIEvent (request 2601)."""
    result = request2601.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/checkout.do'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page28(self):
    """POST feedUIEvent (request 2801)."""
    result = request2801.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/checkout.do'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '86'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page30(self):
    """GET whatIsMyIPAddress (request 3001)."""
    self.token__ = \
      timestr()
    result = request3001.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)
    return result

  def page32(self):
    """POST feedUIEvent (request 3201)."""
    result = request3201.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/viewCart.do'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page34(self):
    """POST feedUIEvent (request 3401)."""
    result = request3401.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/viewCart.do'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '74'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page36(self):
    """GET whatIsMyIPAddress (request 3601)."""
    self.token__ = \
      timestr()
    result = request3601.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)
    return result

  def page38(self):
    """POST feedUIEvent (request 3801)."""
    result = request3801.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/index.do'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page40(self):
    """POST feedUIEvent (request 4001)."""
    result = request4001.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/index.do'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '168'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page42(self):
    """GET whatIsMyIPAddress (request 4201)."""
    self.token__ = \
      timestr()
    result = request4201.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)
    return result

  def page44(self):
    """POST feedUIEvent (request 4401)."""
    result = request4401.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/viewCategory.do?categoryId=CATS'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page46(self):
    """POST feedUIEvent (request 4601)."""
    result = request4601.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/viewCategory.do?categoryId=CATS'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '79'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page48(self):
    """GET whatIsMyIPAddress (request 4801)."""
    self.token__ = \
      timestr()
    result = request4801.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)
    return result

  def page50(self):
    """POST feedUIEvent (request 5001)."""
    result = request5001.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/viewProduct.do?productId=FL-DLH-02'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page52(self):
    """POST feedUIEvent (request 5201)."""
    result = request5201.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/viewProduct.do?productId=FL-DLH-02'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '175'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page54(self):
    """GET whatIsMyIPAddress (request 5401)."""
    self.token__ = \
      timestr()
    result = request5401.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)
    return result

  def page56(self):
    """POST feedUIEvent (request 5601)."""
    result = request5601.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/addItemToCart.do?workingItemId=EST-17'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page58(self):
    """POST feedUIEvent (request 5801)."""
    result = request5801.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/addItemToCart.do?workingItemId=EST-17'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '105'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page60(self):
    """GET whatIsMyIPAddress (request 6001)."""
    self.token__ = \
      timestr()
    result = request6001.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)
    return result

  def page62(self):
    """POST feedUIEvent (request 6201)."""
    result = request6201.POST('/feedUIEvent',
      ( NVPair('stage', 'beforeCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', addUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/index.do'),
        NVPair('timestamp', timestr()), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page64(self):
    """POST feedUIEvent (request 6401)."""
    result = request6401.POST('/feedUIEvent',
      ( NVPair('stage', 'afterCall'),
        NVPair('clientId', '180.229.124.46'),
        NVPair('currentPlace', 'http://beta.owlab.com:8080/jpetstoreL/'),
        NVPair('uuid', getUUID(grinder.threadNumber)),
        NVPair('targetUrl', 'http://beta.owlab.com:8080/jpetstoreL/shop/index.do'),
        NVPair('timestamp', timestr()),
        NVPair('elapsedTime', '91'),
        NVPair('httpStatus', 'success'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    return result

  def page66(self):
    """GET whatIsMyIPAddress (request 6601)."""
    self.token__ = \
      timestr()
    result = request6601.GET('/whatIsMyIPAddress' +
      '?_=' +
      self.token__)
    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    grinder.sleep(167)
    self.page1()      # GET whatIsMyIPAddress (request 101)
    self.page2()      # POST feedUIEvent (request 201)
    self.page4()      # POST feedUIEvent (request 401)
    self.page6()      # GET whatIsMyIPAddress (request 601)
    self.page8()      # POST feedUIEvent (request 801)
    self.page10()     # POST feedUIEvent (request 1001)
    self.page12()     # GET whatIsMyIPAddress (request 1201)
    self.page14()     # POST feedUIEvent (request 1401)
    self.page16()     # POST feedUIEvent (request 1601)
    self.page18()     # GET whatIsMyIPAddress (request 1801)
    self.page20()     # POST feedUIEvent (request 2001)
    self.page22()     # POST feedUIEvent (request 2201)
    self.page24()     # GET whatIsMyIPAddress (request 2401)
    self.page26()     # POST feedUIEvent (request 2601)
    self.page28()     # POST feedUIEvent (request 2801)
    self.page30()     # GET whatIsMyIPAddress (request 3001)
    self.page32()     # POST feedUIEvent (request 3201)
    self.page34()     # POST feedUIEvent (request 3401)
    self.page36()     # GET whatIsMyIPAddress (request 3601)
    self.page38()     # POST feedUIEvent (request 3801)
    self.page40()     # POST feedUIEvent (request 4001)
    self.page42()     # GET whatIsMyIPAddress (request 4201)
    self.page44()     # POST feedUIEvent (request 4401)
    self.page46()     # POST feedUIEvent (request 4601)
    self.page48()     # GET whatIsMyIPAddress (request 4801)
    self.page50()     # POST feedUIEvent (request 5001)
    self.page52()     # POST feedUIEvent (request 5201)
    self.page54()     # GET whatIsMyIPAddress (request 5401)
    self.page56()     # POST feedUIEvent (request 5601)
    self.page58()     # POST feedUIEvent (request 5801)
    self.page60()     # GET whatIsMyIPAddress (request 6001)
    self.page62()     # POST feedUIEvent (request 6201)
    self.page64()     # POST feedUIEvent (request 6401)
    self.page66()     # GET whatIsMyIPAddress (request 6601)
# Instrument page methods.
Test(100, 'Page 1').record(TestRunner.page1)
Test(200, 'Page 2').record(TestRunner.page2)
Test(400, 'Page 4').record(TestRunner.page4)
Test(600, 'Page 6').record(TestRunner.page6)
Test(800, 'Page 8').record(TestRunner.page8)
Test(1000, 'Page 10').record(TestRunner.page10)
Test(1200, 'Page 12').record(TestRunner.page12)
Test(1400, 'Page 14').record(TestRunner.page14)
Test(1600, 'Page 16').record(TestRunner.page16)
Test(1800, 'Page 18').record(TestRunner.page18)
Test(2000, 'Page 20').record(TestRunner.page20)
Test(2200, 'Page 22').record(TestRunner.page22)
Test(2400, 'Page 24').record(TestRunner.page24)
Test(2600, 'Page 26').record(TestRunner.page26)
Test(2800, 'Page 28').record(TestRunner.page28)
Test(3000, 'Page 30').record(TestRunner.page30)
Test(3200, 'Page 32').record(TestRunner.page32)
Test(3400, 'Page 34').record(TestRunner.page34)
Test(3600, 'Page 36').record(TestRunner.page36)
Test(3800, 'Page 38').record(TestRunner.page38)
Test(4000, 'Page 40').record(TestRunner.page40)
Test(4200, 'Page 42').record(TestRunner.page42)
Test(4400, 'Page 44').record(TestRunner.page44)
Test(4600, 'Page 46').record(TestRunner.page46)
Test(4800, 'Page 48').record(TestRunner.page48)
Test(5000, 'Page 50').record(TestRunner.page50)
Test(5200, 'Page 52').record(TestRunner.page52)
Test(5400, 'Page 54').record(TestRunner.page54)
Test(5600, 'Page 56').record(TestRunner.page56)
Test(5800, 'Page 58').record(TestRunner.page58)
Test(6000, 'Page 60').record(TestRunner.page60)
Test(6200, 'Page 62').record(TestRunner.page62)
Test(6400, 'Page 64').record(TestRunner.page64)
Test(6600, 'Page 66').record(TestRunner.page66)
