from django.urls import path,include
from . import views
from rest_framework import routers
from .views import *
from django.contrib import admin

router= routers.DefaultRouter()
router.register(r'sikapay',TableViewSet)


urlpatterns=[
    path("send_otp",views.send_otp,name="send otp"),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.login, name='login'),
    path('signup.html', views.signup, name='signup'),
    path('dashboard.html', views.dashboard, name='dashboard'),
    path('about-us.html', views.aboutus, name='about-us'),
    path('add-wallet.html', views.add_wallet, name='add-wallet'),
    path('business reg form.html', views.businessregform, name='business reg form'),
    path('choosewallet.html', views.choose_wallet, name='choosewallet'),
    path('client_profile.html', views.client_profile, name='client_profile'),
    path('client_update_profile.html', views.client_update_profile, name='client_update_profile'),
    path('demo.html', views.demo, name='demo'),
    path('faqs.html', views.faqs, name='faqs'),
    path('features.html', views.features, name='features'),
    path('forgot_password.html', views.forgot_password, name='forgot_password'),
    path('helpcenter.html', views.helpcenter, name='helpcenter'),
    path('HELPLINE.html', views.HELPLINE, name='HELPLINE'),
    path('history.html', views.history, name='history'),
    path('index.html', views.index, name='index'),
    path('nav.html', views.nav, name='nav'),
    path('pay.html', views.pay, name='pay'),
    path('rateus.html', views.rateus, name='rateus'),
    path('remove-wallet.html', views.remove_wallet, name='remove-wallet'),
    path('services.html', views.services, name='services'),
    path('shop varification page.html', views.shopvarificationpage, name='shop varification page'),
    path('side.html', views.side, name='side'),
    path('transaction.html', views.shop_ver_page, name='transaction'),
    path('update profile shop.html', views.update_shop_profile, name='update profile shop'),
    path('verification_page.html', views.verification_page, name='verification_page'),
    path('tables/', views.table_list, name='table_list'),
    path('tables/<int:id>', views.table_list2, name='table_list2')
    
]