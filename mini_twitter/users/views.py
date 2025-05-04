from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from .serializers import RegisterSerializer, FollowSerializer
from .models import Follow
from django.contrib.auth.models import User

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return User.objects.none()
    
    def perform_create(self, serializer):
        serializer.save()

class FollowViewSet (viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(seguidor=user)
    
    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        try:
            followed_user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        if followed_user == request.user:
            return Response({"detail": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        if Follow.objects.filter(follower=request.user, followed=followed_user).exists():
            return Response({"detail": "You are already following this user"}, status=status.HTTP_400_BAD_REQUEST)
        
        Follow.objects.create(follower=request.user, followed=followed_user)
        return Response({"detail": f"Now following {followed_user.username}"}, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['delete'])
    def unfollow(self, request, pk=None):
        try:
            followed_user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        follow_instance = Follow.objects.filter(follower=request.user, followed=followed_user).first()
        if not follow_instance:
            return Response ({"detail": "You are not following this user"}, status=status.HTTP_400_BAD_REQUEST)
        
        follow_instance.delete()
        return Response({"detail": f"Unfollowed {followed_user.username}"}, status=status.HTTP_204_NO_CONTENT)
        