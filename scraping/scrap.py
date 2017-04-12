import urllib,re
urls = ["http://google.com","http://youtube.com"]
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)
for i in range(0,len(urls)):
	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read()
	title= re.findall(pattern,htmltext)
	#print title 							#fetching titles from websites.
	#print htmltext[0:100]					#printing 1st 100 words. 



htmlfile2 = urllib.urlopen("https://in.finance.yahoo.com/quote/	AAPL?p=AAPL")
htmltext = htmlfile2.read()
regex = '<span id="yfs_l84_AAPL">(.+?)</span>'
pattern = 	re.compile(regex)
price = re.findall(pattern,htmltext)
print price 


