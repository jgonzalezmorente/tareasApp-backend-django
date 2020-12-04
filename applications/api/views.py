from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_auth.views import LoginView

from .models import Task
from .serializers import UserRoleSerializer, TaskSerializer


class Login(LoginView):
    def get_response(self):
        response = super().get_response()
        if response.status_code == status.HTTP_200_OK and 'user' in response.data.keys():
            response.data.pop('user')
        return response



class UserViewSet(ViewSet):

    @action(detail=False)
    def roles(self, request):
        queryset = request.user.get_role.all()
        serializer = UserRoleSerializer(queryset, many=True)
        return Response(serializer.data)



class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request):
        return super().create(request)

    def get_queryset(self):
        print(self.request.user)
        return super().get_queryset()

