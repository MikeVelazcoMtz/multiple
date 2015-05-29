import threading
from django.conf import settings
from django.http import Http404

request_cfg = threading.local()


class RouterMiddleware(object):
    """docstring for RouterMiddleware"""
    def process_request(self, request):
        db_aliases = getattr(settings, "DATABASES", None)
        if db_aliases is None:
            # If database setting does not exist
            print "database setting does not exist"
            raise Http404
        else:
            alias_name = request.path.split("/")[1]

            if db_aliases.get(alias_name, None) is None:
                # if the given database_alias does not exist
                print "database_alias %s does not exist" % alias_name
                raise Http404
            request_cfg.cfg = alias_name
        return None

    def process_response(self, request, response):
        if hasattr(request_cfg, 'cfg'):
            del request_cfg.cfg
        return response


class DatabaseRouter(object):
    """docstring for DatabaseRouter"""
    def _default_db(self):
        return request_cfg.cfg if hasattr(request_cfg, 'cfg') else 'default'

    def db_for_read(self, model, **hints):
        return self._default_db()

    def db_for_write(self, model, **hints):
        return self._default_db()
