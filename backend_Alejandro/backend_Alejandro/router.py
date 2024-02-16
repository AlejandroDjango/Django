from rest_framework import routers

import usuarios.views as views

router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/groups', views.GroupViewSet)
router.register(r'api/register', views.RegisterViewSet, basename='register')