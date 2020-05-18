from django.urls import path
from ksm_app import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'ksm_app'

urlpatterns = [
    path('', views.base, name = 'base'),
    path('choose_register/',views.ChooseRegister, name = 'choose'),
    path('debatants_register/', views.DebatantsRegister, name = 'debatants'),
    path('judges_register/', views.JudgesRegister, name = 'judges'),
    path('login/', views.user_login, name = 'user_login'),
    path('judges_list/', views.judges_list, name = 'judges_list'),
    path('judges_detail/<int:pk>/',views.judges_detail, name = 'detail'),
    path('debatants_list/', views.debatants_list, name = 'debatants_list'),
    path('debatants_detail/<int:pk>/', views.debatants_detail, name = 'debatants_detail'),
    path('live/', views.ShowBattle, name = 'live'),
    path('battle/', views.createBattle, name = 'battle'),
    path('battle_update/<int:pk>/',views.updateBattle, name = 'updateBattle'),
    path('delete_update/<int:pk>/',views.deleteBattle, name = 'deleteBattle'),
    path('judgesauth/', views.judgesAuth, name = 'password'),
    path('phone/', views.phone, name = 'phone'),
    path('debatants_profile/', views.debatantsProfilePage, name = 'debatants_profile'),
    path('judges_profile/', views.judgesProfilePage, name = 'judges_profile'),
    path('judges_update/', views.edit_judges_profile, name = 'judges_update'),
    path('debatants_update/', views.edit_debatants_profile, name = 'debatants_update'),
    path('instruction/', views.instruction, name = 'instruction'),
    path('clock/',views.index, name = 'clock')

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
