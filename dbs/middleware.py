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


        # print(request.user)

        # if request.META.get("HTTP_AUTHORIZATION", "").startswith("Bearer"):
        #     if not hasattr(request, "user") or request.user.is_anonymous:
        #         print("ww")
        #         user = authenticate(request=request)
        #         print("J")
        #         print(user)
        #         if user:
        #             request.user = request._cached_user = user

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



        # if request.user and request.user.id:


        # print(request.META.get('HTTP_AUTHORIZATION'))
        # token=request.META.get('HTTP_AUTHORIZATION').replace('Bearer ','')

        # AccessToken.objects.get(token=token)

        # print("X")
        # print(AccessToken)

        # print(AccessToken.user_id)
        # print("Y")


        # print("SDf")
        # print(args)
        # print(request.META)
        # return None

        # print(request.build_absolute_uri())

        # request_cfg.cfg = 'db9815'
        # try:
        #     x=request.user
        #     if request.user and request.user.username:
        #         request_cfg.cfg='db'+str(request.user.username)
        # except:
        #     pass

        response = self.get_response(request)
        return response

    
    # def process_response( self, request, response ):
    #     if hasattr( request_cfg, 'cfg' ):
    #         del request_cfg.cfg
    #     return response

# def process_request(self, request):
#         # do something only if request contains a Bearer token
#         if request.META.get("HTTP_AUTHORIZATION", "").startswith("Bearer"):
#             if not hasattr(request, "user") or request.user.is_anonymous:
#                 user = authenticate(request=request)
#                 if user:
#                     request.user = request._cached_user = user
#                 print(user)

# def process_response(self, request, response):
#     patch_vary_headers(response, ("Authorization",))
#     return response





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