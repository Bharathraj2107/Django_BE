from django.urls import path
from .import views

app_name='my_library'

urlpatterns=[
    # path('demo_page/',views.demo)
    # path('<topic>/',views.lib_news),#which is a parameter to the function in the views
    # path('<int:n1>/<int:n2>/',views.add_views),
    # path('<int:num_page>/',views.page_num_view),
    # path('oprtns/',views.oprtns_view),
    path('calculator/',views.add_numbers),
]