# calendar_integration.py
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'ai-voice/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def create_event(service, summary, start_time_str, end_time_str):
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time_str,
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': end_time_str,
            'timeZone': 'America/New_York',
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    return event

def schedule_meeting(summary, start_time, duration_minutes=30):
    creds = authenticate_google()
    service = build('calendar', 'v3', credentials=creds)
    
    start_time_str = start_time.isoformat()
    end_time = start_time + datetime.timedelta(minutes=duration_minutes)
    end_time_str = end_time.isoformat()
    
    event = create_event(service, summary, start_time_str, end_time_str)
    speak(f"Meeting scheduled: {event.get('htmlLink')}")
