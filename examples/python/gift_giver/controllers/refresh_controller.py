from services.refresh_attendees import RefreshAttendees
from flask_api import status
from flask import jsonify


class RefreshController:
    def index(self):
        response = RefreshAttendees().list.run()
        if response.is_success:
            return {'status': 'The attendess list was refreshed'}
        else:
            content = {'status': 'not found'}
            return content, status.HTTP_404_NOT_FOUND
