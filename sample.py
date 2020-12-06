from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from restautomatepm.models import Projects, Phases, Log
from restautomatepm.serializers import ProjectsSerializer, PhasesSerializer, LogSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny


# Returning lists endpoints
class ProjectList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        user = self.request.user
        return Projects.objects.filter(owner=user)


class LogList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LogSerializer

    def get_queryset(self):
        user = self.request.user
        users_projs_logs = Projects.objects.filter(
            owner=user).values_list('id', flat=True)
        return Log.objects.filter(projectId__in=users_projs_logs).order_by('-id')


class PhasesList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PhasesSerializer

    def get_queryset(self):
        user = self.request.user
        projects_ids = Projects.objects.filter(
            owner=user).values_list('id', flat=True)
        return Phases.objects.filter(projectId__in=projects_ids).order_by('-id')

# Editing/Deleting/Creating projects endpoints


class CreateProject(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    # overriding create field to add user as owner

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UpdateProject(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class DeleteProject(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

# Editing/Deleting/Creating phases endpoints


class CreatePhase(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Phases.objects.all()
    serializer_class = PhasesSerializer


class UpdatePhase(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Phases.objects.all()
    serializer_class = PhasesSerializer


class DeletePhase(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Phases.objects.all()
    serializer_class = PhasesSerializer

#  Creating log entry


class CreateLogEntry(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Log.objects.all()
    serializer_class = LogSerializer

# User info and management


class UserList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUser(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
