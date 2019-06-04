import json
import sys
import time
import Netmaxiot
from datetime import datetime
# import Adafruit_DHT
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#DHT_TYPE = Adafruit_DHT.DHT11
#DHT_PIN  = 17
GDOCS_OAUTH_JSON       = 'myiot.json'
GDOCS_SPREADSHEET_NAME = 'Google Iot Netmaxiot CLoud'
FREQUENCY_SECONDS      = 5
############################################################
def login_open_sheet(oauth_key_file, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    try:
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1
        return worksheet
    except Exception as ex:
        print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        sys.exit(1)

#scope = ['https://spreadsheets.google.com/feeds',
#         'https://www.googleapis.com/auth/drive']
#credentials = ServiceAccountCredentials.from_json_keyfile_name(GDOCS_OAUTH_JSON, scope)
#gc = gspread.authorize(credentials)
print('Logging sensor measurements to {0} every {1} seconds.'.format(GDOCS_SPREADSHEET_NAME, FREQUENCY_SECONDS))
print('Press Ctrl-C to quit.')
worksheet = None
while True:
        # Login if necessary.
    if worksheet is None:
        worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)
        print "login to google sheet with login details"
    print "---------------------------------------------"
    PIN0 = Netmaxiot.analogRead(0)
    PIN1 = Netmaxiot.analogRead(1)
    PIN2= Netmaxiot.analogRead(2)
    PIN3= Netmaxiot.analogRead(3)
    #volt0=(PIN*4.89)
    #volt1=(PIN1*4.89)
    #volt2=(PIN2*4.89)
    #0volt3=(PIN3*4.89)
    pin0=str(PIN0)
    pin1=str(PIN1)
    pin2=str(PIN2)
    pin3=str(PIN3)
#    print (hum1)
    nowx=datetime.now()
    xp=nowx.strftime("20%y-%m-%d %X")
    time1= str(xp)
#    print(time1)
    #if worksheet is None:
    #    worksheet = gc.open(GDOCS_SPREADSHEET_NAME).sheet1
    #humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
    
    print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    print " "
    print PIN0,"      ",PIN1,"     ",PIN2,"     ",PIN3
    
    #print "%0.1fmv"%(volt0),"  ""%0.1fmv"%(volt1),"  ""%0.1fmv"%(volt2),"  ""%0.1fmv"%(volt3)
    try:
      worksheet.append_row((time1,pin0,pin1,pin2,pin3))
      print "***************************************************"
      
    except:
      print('Append error, logging in again')
      worksheet = None
      time.sleep(FREQUENCY_SECONDS)
      continue

    print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
    time.sleep(FREQUENCY_SECONDS)
    print (FREQUENCY_SECONDS) 
    print "***************************************************"
