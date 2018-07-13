from . import views
from django.urls import path, include
from blog.views import PostViews
from property.views import PropertyView
app_name = 'home'
urlpatterns = [
    path('', views.home, name='home_page'),
    path('about-us', views.about_us_view, name='about_us'),
    path('property/<id>', PropertyView.property_view, name='property'),
    path('blog', PostViews.post_view, name='blog'),
    path('listing', PropertyView.property_list, name='listing'),
    path('blog-post/<id>', PostViews.post_detail, name='post_detail'),
    path('contact-us', views.contact_view, name='contact'),
    path('career', views.career_view, name='career')
]