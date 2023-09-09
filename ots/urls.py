from django.urls import path
from ots.views import *
app_name = 'ots'

urlpatterns = [
    path('',welcome),
    path('new-candidate',candidateRegistrationform,name='Registrationform'),
    path('store-candidate',candidateRegistration,name='storecandidate'),
    path('login',loginView,name='login'),
    path('home',candidateHome,name='home'),
    path('test-paper',testpaper,name='testpaper'),
    path('calculate-result',candidateTestResult,name='calculatetest'),
    path('test-history',testResultHistory,name='testHistory'),
    path('result',showTestResult,name='result'),
    path('logout',logoutView,name='logout'),
    
]







