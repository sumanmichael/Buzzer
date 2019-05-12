import requests
from bs4 import BeautifulSoup


def wordofday(txt_log):
	try:
		page = requests.get('http://www.wordthink.com/')
		soup = BeautifulSoup(page.text,'html.parser')
		word = "Word:\n"+soup.find('div',{'class':'singlemeta'}).find('p').text
		txt_log.AppendText(word+"\n")
		return word
	except:
		txt_log.AppendText("Connection Failed with Word Of The Day\'s Server...\n\n")

def quoteofday(txt_log):
	try:
		page = requests.get('http://www.eduro.com/')
		soup = BeautifulSoup(page.text,'html.parser')
		quote = "Quote:\n"+soup.find('div',{'class':'singlemeta'}).find('p').text+soup.find('div',{'class':'singlemeta'}).find('p',{'class':'author'}).text[:-10]
		txt_log.AppendText(quote+"\n")
		return quote
	except:
		txt_log.AppendText("Connection Failed with Quote Of The Day\'s Server...\n\n")

def horoscope(txt_log,z):
	try:
		page = requests.get('http://www.starlightastrology.com/daily.htm')
		soup = BeautifulSoup(page.text,'html.parser')
		horo_txt = soup.find_all('p',{'align':'left'})[z].text
		txt_log.AppendText(horo_txt+"\n")
		return horo_txt
	except:
		txt_log.AppendText("Connection Failed with Horoscope\'s Server...\n\n")