from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    path('',views.Bloglist.as_view(),name='index'),
    path('blog/<int:pk>', views.Blogviews.as_view(), name="blogt"),
    path('add/', views.add_data, name="insdata"),
    path("add/post_new", views.post_new, name="postnew"),
]
