import urllib.request
webUrl  = urllib.request.urlopen('https://www.google.com.sa/')
data = webUrl.read()
print (data)