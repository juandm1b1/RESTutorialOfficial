from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()), # Vistas basadas en clases
    path('snippets/<int:pk>', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),                    #(5)
    path('users/<int:pk>', views.UserDetail.as_view()),
    
    #path('snippets/', views.snippet_list), # Vistas basadas en fumciones
    #path('snippets/<int:pk>', views.snippet_detail),   
]

urlpatterns = format_suffix_patterns(urlpatterns)