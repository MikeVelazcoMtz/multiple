from django.utils.decorators import method_decorator
from dynamic_db_router import in_database

DB_ROUTING_INSTANCE = None


class DBRoutingMixin(object):
    """docstring for DBRoutingMixin"""
    def __init__(self, arg):
        super(DBRoutingMixin, self).__init__()
        DB_ROUTING_INSTANCE = self.request.path.split("/")


    @method_decorator(in_database(DB_ROUTING_INSTANCE))
    def dispatch(self, request, *args, **kwargs):
        return super(DBRoutingMixin, self).dispatch(request, *args, **kwargs)


class DataBaseChange(object):
    """docstring for DataBaseChange"""
    def dispatch(self, request, *args, **kwargs):
        url = request.path
        url = url.split("/")
        print request.path, url
        return super(DataBaseChange, self).dispatch(request, *args, **kwargs)
