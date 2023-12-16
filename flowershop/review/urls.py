from django.urls import path

from review.views import reviewAPIView, reviewCreate_view, replyCreate_view, reviewFullAPIView


urlpatterns = [
    path('', reviewAPIView.as_view()),
    path('<int:pk>/reply', replyCreate_view),
    path('post', reviewCreate_view),
    path('<int:pk>', reviewFullAPIView.as_view()),
   ]