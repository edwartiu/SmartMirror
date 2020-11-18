# Install google api client
# run command 'pip install google-api-python-client'
# run command 'pip install google-auth-oauthlib'

from __future__ import print_function
import datetime
import pickle
import os.path
import pytz
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request



# Call the Calendar API
def get_todays_events():
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    creds = None

    # Checks if user credentials are already saved in pkl file. If so assigns thme to creds
    if os.path.exists('token.pkl'):
        with open('token.pkl', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
    
        # Save credentials for next run
        with open('token.pkl', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    PST = pytz.timezone('US/Pacific')
    utc_dt = datetime.datetime.now(datetime.timezone.utc)

    now = utc_dt.astimezone(PST).isoformat()
    end_date = utc_dt.astimezone(PST).replace(hour=23, minute=59).isoformat()
    events_result = service.events().list(calendarId='primary', timeMin=now, timeMax=end_date, maxResults=5, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    user_events = []


    if not events:
        print('No upcoming events found.')
    for event in events:
        event_info = {}
        #Retrieve title
        event_info['title'] = event['summary']

        #Retrieve and format start time
        startTime = event['start'].get('dateTime')
        startTime = startTime[:19].replace('T', ' ')
        date_time_obj = datetime.datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')
        try: 
            event_info['start'] = date_time_obj.strftime("%#I:%M %p")
        except:
            event_info['start'] = date_time_obj.strftime("%-I:%M %p")

        #Retrieve and format end time
        endTime = event['end'].get('dateTime')
        endTime = endTime[:19].replace('T', ' ')
        date_time_obj = datetime.datetime.strptime(endTime, '%Y-%m-%d %H:%M:%S')
        try:
            event_info['end'] = date_time_obj.strftime("%#I:%M %p")
        except:
            event_info['end'] = date_time_obj.strftime("%-I:%M %p")
        user_events.append(event_info)
    
    return user_events

