from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm,MyPasswordResetForm,PasswordResetForm

urlpatterns = [
    # path('', views.home),
    path('',views.ProductView.as_view(),name="home"),
    path('product-detail/<int:pk>', views.ProductDetailview.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),

    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('accounts/login/', auth_views.LoginView.as_view (template_name="app/login.html",authentication_form=LoginForm), name='login'),
    path("logout/",auth_views.LogoutView.as_view(next_page="login"),name="logout"),
    path("passwordchange/",auth_views.PasswordChangeView.as_view(template_name="app/passwordchange.html",form_class=MyPasswordChangeForm,success_url="/passwordchangedone/"),name="passwordchange"),

    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name = "app/passwordchangedone.html"),name="passwordchangedone"),
    
    path("password_reset/",auth_views.PasswordResetView.as_view(template_name ="app/password_reset.html",form_class=MyPasswordResetForm),name="password_reset"),

    path("password_reset/done",auth_views.PasswordResetDoneView.as_view(template_name ="app/password_reset_done.html"),name="password_reset_done"),

    path("password_reset/confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name ="app/password_reset_confirm.html",form_class=PasswordResetForm),name="password_reset_confirm"),

    path("password_reset/complete",auth_views.PasswordResetCompleteView.as_view(template_name ="app/password_reset_complete.html"),name="password_reset_complete"),



    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
