import requests
from models.attendee import Attendee
from stories import story, Success, Failure, Result


class RefreshAttendees:
    url = 'https://api.meetup.com/valetechtalks/events/268854460/rsvps?&sign=true&photo-host=public&fields=answers'

    @story
    def list(I):
        I.sucess
        I.finish

    def sucess(self, ctx):
        response = requests.get(self.url)
        attendee_name = lambda attendee: attendee['member']['name']
        attendees = list(map(attendee_name, response.json()))
        for attendee in attendees:
            Attendee.first_or_create(name=attendee)
        return Success(result=attendees)

    def finish(self, ctx):
        return Result(ctx)
