from orator import Model


class Attendee(Model):
    __table__ = 'attendees'
    __fillable__ = ['name']

    pass
