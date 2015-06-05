from django.views.generic import ListView, CreateView
# from django.contrib.auth.models import User
# from django.conf import settings as s
from .models import Cliente


class UserListView(ListView):
    model = User
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        print s.MEDIAFILE_DIRS
        return super(UserListView, self).get(request, *args, **kwargs)


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "new_client.html"
    fields = Cliente.MY_FIELDS

    def dispatch(self, request, *args, **kwargs):
        self.success_url = request.path.replace("new", "list")
        return super(ClienteCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.success_url = request.path.replace("new", "list")
        return super(ClienteCreateView, self).post(request, *args, **kwargs)


class ClienteListView(ListView):
    model = Cliente
    template_name = "list_clientes.html"
