from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, search=None, **kwargs):

        # In case of search we don't need to json render
        if search:
            content = data
        else:
            content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

GENERAL_MESSAGE = {'status': True}

AUTHENTICATION_ERROR = {'message': 'Provided Credentials are wrong', 'status': False}

CANT_FIND_LOANS = {'message': 'No loans pending', 'status': False}

ALREADY_REGISTERED = {'message': 'User Already Registered', 'status': False}