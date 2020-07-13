import re
import threading 
request_cfg = threading.local()

from oauth2_provider.models import AccessToken

from django.contrib.auth import authenticate


class RouterMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        print("XXX")
        print(request.body)
        print(request.method)

        print("A")
        print(hasattr(request,'user'))
        print("X")
        print(request.user)
        print("B")

        print(request.META.get('HTTP_AUTHORIZATION'))

        if hasattr(request,'user'):
            if request.user and request.user.id:
                request_cfg.cfg='db'+str(request.user.username)

                pass
                # pass

        print(request.META.get('HTTP_AUTHORIZATION'))

        print("ZZ")
        print(request.user)

        response = self.get_response(request)
        return response


class DatabaseRouter(object):
    def _default_db( self ):
        print("SSS")
        print(request_cfg)
        if hasattr( request_cfg, 'cfg' ):

            print("what")
            print(request_cfg.cfg)
            return request_cfg.cfg
        else:
            return 'default'

    def db_for_read( self, model, **hints ):
        print("YYY")
        return self._default_db()

    def db_for_write( self, model, **hints ):
        return self._default_db()
