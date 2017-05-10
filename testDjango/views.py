# Create your views here.
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets

from testDjango.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Create your views here.

# Function that receive a request and create our dashboard.
#
# @date [06/04/2017]
#
# @author [Chiseng Ng]
#
# @param [request] request Request of the page.
#
# @returns [NONE]
def dashboard(request):
    user = request.user
    return render(request, 'testView/dashboard.html', {'user': user})
