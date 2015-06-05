import threading
from django.conf import settings
from django.http import Http404
import re
request_cfg = threading.local()


class RouterMiddleware(object):
    def process_request(self, request):
        db_aliases = getattr(settings, "DATABASES", None)
        domain = request.META.get('HTTP_HOST', None)
        if None in [db_aliases, domain] or not "." in domain:
            raise Http404
        else:
            split_domain = domain.split(".")
            if len(split_domain) in [2, 3]:
                if re.match(r'^[a-z0-9]{3,14}$', split_domain[0]) and split_domain[0] in db_aliases:
                    request_cfg.cfg = split_domain[0]
                else:
                    raise Http404
            else:
                raise Http404
        return

    def process_response(self, request, response):
        if hasattr(request_cfg, 'cfg'):
            del request_cfg.cfg
        return response


# class RouterMiddleware(object):
#     """docstring for RouterMiddleware"""
#     def process_request(self, request):
#         db_aliases = getattr(settings, "DATABASES", None)
#         file_location = "/home/debian/django/multiple/multiple/requests.log"
#         my_log = open(file_location, "a+")
#         log = "%s\n" % (request.META.get('HTTP_HOST', "NO HOST: IMPOSIBLE"))
#         my_log.write(log)
#         my_log.close()
#         if db_aliases is None:
#             # If database setting does not exist
#             print "database setting does not exist"
#             raise Http404
#         else:
#             alias_name = request.path.split("/")[1]

#             if db_aliases.get(alias_name, None) is None:
#                 # if the given database_alias does not exist
#                 print "database_alias %s does not exist" % alias_name
#                 raise Http404
#             request_cfg.cfg = alias_name
#         return None

    # def process_response(self, request, response):
    #     if hasattr(request_cfg, 'cfg'):
    #         del request_cfg.cfg
    #     return response


class DatabaseRouter(object):
    """docstring for DatabaseRouter"""
    def _default_db(self):
        return request_cfg.cfg if hasattr(request_cfg, 'cfg') else 'default'

    def db_for_read(self, model, **hints):
        return self._default_db()

    def db_for_write(self, model, **hints):
        return self._default_db()
