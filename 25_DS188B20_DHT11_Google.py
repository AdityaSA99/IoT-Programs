import json
import sys
import time
from datetime import datetime
import Adafruit_DHT
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from w1thermsensor import W1ThermSensor

DHT_TYPE = Adafruit_DHT.DHT11
sensor = W1ThermSensor()
DHT_PIN  = 17
GDOCS_OAUTH_JSON       = 'Stark3000.json'
GDOCS_SPREADSHEET_NAME = 'Stark3000'
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
    humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
    temp_c = str(sensor.get_temperature())
    temp_f = str(float(temp_c) * 9.0 / 5.0 + 32.0)
    temp1= str(temp)
#    print (temp1) 
    hum1= str(humidity)
#    print (hum1)
    nowx=datetime.now()
    xp=nowx.strftime("20%y-%m-%d %X")
    time1= str(xp)
#    print(time1)
    #if worksheet is None:
    #    worksheet = gc.open(GDOCS_SPREADSHEET_NAME).sheet1
    #humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
    if humidity is None or temp is None:
        time.sleep(2)
        continue
    print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    print(temp_c)
    print(temp_f)
    print(temp1)
    print(hum1)
    print(time1)
    try:
      worksheet.append_row((time1,temp1,hum1,temp_c,temp_f))
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
