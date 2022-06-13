from django.urls import path

import core.views as views
urlpatterns = [
    path('home/', views.HomeView.as_view()),
    path('videos/', views.VideosView.as_view(), name="videos"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('trust/', views.TrustView.as_view(), name="trust"),
]