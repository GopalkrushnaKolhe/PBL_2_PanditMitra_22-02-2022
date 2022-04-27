from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("reviews/", views.reviews, name="reviews"),
    path("choosePujaForReview/", views.choosePujaForReview,
         name="choosePujaForReview"),
    path("seeReviews/", views.seeReviews, name="seeReviews"),
    path("sign-up/", views.signUp, name="sign_Up"),
    path("book/", views.book, name="book"),
    path("pandit/", views.pandit, name="pandit"),
    # path("puja/", views.puja, name="puja"),
    path("puja/<int:id>/", views.puja, name="puja"),
    path("puja/<int:id>/order/", views.order, name="order"),
    path("myOrders/", views.myOrders, name="myOrders"),
    path("updateOrders/<int:pk>/", views.updateOrders, name="updateOrders"),
    path("deleteOrders/<int:pk>/", views.deleteOrders, name="deleteOrders"),
    path("aboutUs/", views.aboutUs, name="aboutUs"),
    path("logout/", views.logout, name="logout"),
]
