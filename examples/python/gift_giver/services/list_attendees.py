from stories import story, Success, Failure, Result
from models.attendee import Attendee


class ListAttendees:
    @story
    def list(I):
        I.sucess
        I.finish

    def sucess(self, ctx):
        attendees_name = lambda attendee: {'name': attendee.name}
        attendees = list(Attendee.all().map(attendees_name))
        return Success(result=attendees)

    def finish(self, ctx):
        return Result(ctx)
