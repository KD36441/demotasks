from django.urls import path
from .import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('products/', views.product, name='products'),
    path('products/', views.getproduct, name='get_products'),
    path('create_order/<str:pk>/', views.createproduct, name="create_order"),
    path('update_order/<str:pk>/', views.updateproduct, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteproduct, name="delete_order"),


]