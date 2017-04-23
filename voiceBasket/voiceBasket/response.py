from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
import re


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, search=None, **kwargs):

        # In case of search we don't need to json render
        if search:
            content = data
        else:
            data = JSONResponse.convert_json(data, JSONResponse.underscore_to_camel)
            print(data)
            content = JSONRenderer().render(data)

        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

    @staticmethod
    def convert_json(d, convert):
        new_d = {}
        for k, v in d.iteritems():
            if isinstance(v, dict):
                new_d[convert(k)] = JSONResponse.convert_json(v, convert)
            elif isinstance(v, list):
                new_d[convert(k)] = [JSONResponse.convert_json(element, convert) for element in v]
            else:
                new_d[convert(k)] = v
        return new_d

    @staticmethod
    def underscore_to_camel(name):
        return re.compile(r'_([a-z])').sub(lambda x: x.group(1).upper(), name)


GENERAL_MESSAGE = {'status': True}

AUTHENTICATION_ERROR = {'message': 'Provided Credentials are wrong', 'status': False}

CANT_FIND_LOANS = {'message': 'No loans pending', 'status': False}

ALREADY_REGISTERED = {'message': 'User Already Registered', 'status': False}