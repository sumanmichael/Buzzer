import requests

def shorten_url(long_url):
	login = '' 											#LoginID here
	apikey = ''											#API_Key here
	bitly_url = "http://api.bit.ly/v3/shorten?login={0}&apiKey={1}&longUrl={2}&format=txt".format(login,apikey,long_url)
	short_url = requests.get(bitly_url)
	if short_url.status_code==200:
		return short_url.text
	else:
		return False

def get_news(txt_log):
	try:
		new_api_key = ''  #NewsAPI API_Key
		r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey={0}'.format(new_api_key))
		news = r.json()
		if news['status']=='ok':
			txt_log.AppendText("Connection Established with NEWS Server...\n")
			title = news['articles'][0]['title']
			# if len(title)>120:
			# 	title = title[:120]+"..."
			link = shorten_url(news['articles'][0]['url'])
			msg_news = "News:\n{}. {} ".format(title,link)
			txt_log.AppendText("NEWS Retrieved from Server:\n"+msg_news+"\n")
			return msg_news
		else:
			txt_log.AppendText("Connection Failed with NEWS Server...\n\n")
	except:
		txt_log.AppendText("Connection Failed with NEWS Server...\n\n")
