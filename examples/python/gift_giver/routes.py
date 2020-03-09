from controllers.attendees_controller import AttendeesController
from controllers.refresh_controller import RefreshController

def routes(app):
    app.add_url_rule('/attendees', 'attendees', AttendeesController().index, methods=['GET'])
    app.add_url_rule('/refresh', 'refresh', RefreshController().index, methods=['POST'])
    return app
