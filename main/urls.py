from main.views import register
from main.views import edit_mood
from django.urls import path
from main.views import login_user
from main.views import logout_user
from main.views import show_main, create_mood_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import delete_mood
app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
    path('delete/<uuid:id>', delete_mood, name='delete_mood'),
    path('edit-mood/<uuid:id>', edit_mood, name='edit_mood'),
    path('create-mood-entry', create_mood_entry, name='create_mood_entry'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]