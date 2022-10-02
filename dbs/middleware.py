import re
import threading 
request_cfg = threading.local()

from oauth2_provider.models import AccessToken

from django.contrib.auth import authenticate


class RouterMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if hasattr(request,'user'):
            if request.user and request.user.id:
                request_cfg.cfg='db'+str(request.user.username)
                pass

        response = self.get_response(request)
        return response


class DatabaseRouter(object):
    def _default_db( self ):
        
        if hasattr( request_cfg, 'cfg' ):
            return request_cfg.cfg
        else:
            return 'default'

    def db_for_read( self, model, **hints ):
        return self._default_db()

    def db_for_write( self, model, **hints ):
        return self._default_db()
