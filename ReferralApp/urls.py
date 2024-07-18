from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name="home"),
    path('sub-page/', views.SubPageView.as_view(), name="sub-page"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('user-deletion/', views.UserDeletion.as_view(), name="user-deletion"),
    path('collaboration/', views.CollaborationView.as_view(), name="collaboration"),
    path('confirm-deletion/<str:pk>/', views.ConfirmDeletion.as_view(), name="confirm-deletion"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('privacy_policy/', views.PrivacyPolicy.as_view(), name="privacy-policy"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
