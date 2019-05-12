# BUZZER v1.0


### Description:
Buzzer is a simple python GUI which enables us to send News, Weather Report, Horoscope, Words, Quotes, etc. This project covers the concepts like GUI, API Handling, Web-Scrapping.
  
### Prerequisites:

 - Python 3 
 - wxPython 
 - twilio 
 - pyowm 
 - beautysoup4 
 - Accounts along with API_Keys for OpenWeatherMap, Twilio, NewsAPI

### Installation:

**1. Installation of python in Windows (Ignore If installed):**
 - You can download Python for Windows from the website
   https://www.python.org/downloads/windows/.
 - Click on the "Latest Python 3 Release - Python x.x.x" link.
 - If your computer is running a 64-bit version of Windows, download the Windows x86-64 executable installer.
 - Otherwise, download the Windows x86 executable installer.
 - After downloading the installer, you should run it (double-click on it) and follow the instructions there.
  
  

>  Note: Add Python PATH to system environment variables.

  
**2.	Installing Dependencies:**
  -	 Open Command Prompt (CMD) with Administrator Privileges.
  - Enter the following lines in CMD
    ```python
         > python –m pip install wxPython
         > python –m pip install twilio
         > python –m pip install pyowm
         > python –m pip install beautysoup4
    ```


### Source Code:
Source code contains following files:
1.	buzzer.py
	  This file contains all the GUI (Graphical User Interface) code which is written using wxPython. It also Rest of the files is imported and accessed from here. It contains the object of wxPython like Frame, Panels, Notebook, Pages, Buttons, TextCtrl, Labels, etc.
2.	news.py
	It gathers the information from http://newsapi.org through API Key. It also includes the URL Shorter with the help of http://bit.ly through Login and API Keys. The response from newsapi.org is of JSON format. Thus, the information is extracted and sends to buzzer.py
3.	weather.py
  The functions in this module are written in such a way that it gathers the nearby locations and weather report of a given place at current time.
4.	webscrap.py
  The functions in this module are written in such a way that it gathers from various sites regarding Word Of The Day, Quote Of The Day And Horoscope. It uses the Web scrapping strategy to extract the information from websites.
5.	sms.py
  This module helps us in sending a given text as SMS to a given twilio registered number.

### Instructions:
  1.	Run the file buzzer.py to launch the Buzzer application.
  2.	After the launching of application, just go through the different pages.
  3.	Enter the mobile number and hit Send button to send the message.
  4.	The SMSs received in mobile can be seen in Preview directory.
   
### License:
  The project is not licensed yet.
  
### Contributor(s):
This project is developed by **Suman Michael** [(@sumanmichael)](www.github.com/sumanmichael/), B151537, Dept. of CSE, Rajiv Gandhi University of Knowledge technologies, Basar.
