from .serializers import UserSerializer , ProfileSerializer , AdminUserSerializer , StaffUserSerializer
from .models import CustomUser , Profile
from .permissions import NoCreateDeletePermission , IsStaffOrAdmin
from .pagination import PaginationNumber
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated , AllowAny , IsAdminUser
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

# Create your views here.

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(id=user.id)
    
class StaffUserView(ModelViewSet):
    serializer_class = StaffUserSerializer
    permission_classes = [IsStaffOrAdmin]
    filter_backends = [SearchFilter]
    search_fields = ["username"]
    pagination_class = PaginationNumber

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(
                (Q(is_staff=False) & Q(is_superuser=False)) | Q(id=user.id)
            )
    
class AdminUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]
    pagination_class = PaginationNumber
    filter_backends = [SearchFilter]
    search_fields = ["email","username"]
    
class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [NoCreateDeletePermission]
    filter_backends = [SearchFilter,DjangoFilterBackend]
    search_fields = ["name"]
    filterset_fields = ["user"]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Profile.objects.select_related("user").all()
        return Profile.objects.select_related("user").filter(user=user)