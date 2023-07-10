from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # path('', views.populate_db, name='populate_db'),
    path('', views.home, name='home'),
    path('connexion/', views.login_page, name='login'),
    path('deconnexion/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('details_dashboard/<str:choice_pi>/<str:type_pi>/<int:annee_pi>/', views.details_dashboard, name='details_dashboard'),

    path('check_file_brevets/', views.check_file_brevets, name='check_file_brevets'),
    path('check_file_dmi/', views.check_file_dmi, name='check_file_dmi'),
    path('check_file_marques/', views.check_file_marques, name='check_file_marques'),
    path('check_file_pays/', views.check_file_pays, name='check_file_pays'),
    path('export_file_oapi/', views.export_file_oapi, name='export_file_oapi'),
    path('export_file_ompi/', views.export_file_ompi, name='export_file_ompi'),

    path('load_brevets/', views.load_brevets, name='load_brevets'),
    path('load_dmi/', views.load_dmi, name='load_dmi'),
    path('load_marques/', views.load_marques, name='load_marques'),
    path('load_pays/', views.load_pays, name='load_pays'),

    path('listing_users/', views.listing_users, name='listing_users'),
    path('listing_pays/', views.listing_pays, name="listing_pays"),
    path('listing_brevets/', views.listing_brevets, name='listing_brevets'),
    path('listing_marques/', views.listing_marques, name='listing_marques'),
    path('listing_dmi/', views.listing_dmi, name='listing_dmi'),

    path('add_brevets/', views.add_brevets, name='add_brevets'),
    path('add_dmi/', views.add_dmi, name='add_dmi'),
    path('add_marques/', views.add_marques, name='add_marques'),
    path('add_pays/', views.add_pays, name="add_pays"),

    path('edit_user/<str:username>/', views.edit_user, name='edit_user'),
    path('edit_password/<str:username>/', views.edit_password, name='edit_password'),
    path('edit_group/<str:old_group>/<str:new_group>/<str:username>/', views.edit_group, name='edit_group'),
    path('edit_brevets/<int:pk>/', views.edit_brevets, name='edit_brevets'),
    path('edit_dmi/<int:pk>/', views.edit_dmi, name='edit_dmi'),
    path('edit_marques/<int:pk>/', views.edit_marques, name='edit_marques'),
    path('edit_pays/<int:pk>/', views.edit_pays, name='edit_pays'),
    path('edit_status/<str:action>/<str:username>/', views.edit_status, name='edit_status'),

    path('details_brevets/<int:pk>/', views.details_brevets, name='details_brevets'),
    path('details_marques/<int:pk>/', views.details_marques, name='details_marques'),
    path('details_dmi/<int:pk>/', views.details_dmi, name='details_dmi'),
    path('delete_marques/<int:pk>/', views.delete_marques, name='delete_marques'),

    path('confirm_delete_pays/<int:pk>/', views.confirm_delete_pays, name='confirm_delete_pays'),
    path('confirm_delete_marque/<int:pk>/', views.confirm_delete_marques, name='confirm_delete_marques'),
    path('confirm_delete_brevets/<int:pk>/', views.confirm_delete_brevets, name='confirm_delete_brevets'),
    path('confirm_delete_dmi/<int:pk>/', views.confirm_delete_dmi, name='confirm_delete_dmi'),

    path('delete_dmi/<int:pk>/', views.delete_dmi, name='delete_dmi'),
    path('delete_pays/<int:pk>/', views.delete_pays, name='delete_pays'),
    path('delete_brevets/<int:pk>/', views.delete_brevets, name='delete_brevets'),
    path('suppression_brevets/', views.suppression_brevets, name='suppression_brevets'),
    path('suppression_dmi/', views.suppression_dmi, name='suppression_dmi'),
    path('suppression_marques/', views.suppression_marques, name='suppression_marques'),
]
