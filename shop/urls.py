from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create-checkout-session/", views.create_checkout_session, name="create_checkout_session"),
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel"),
    path("mock-checkout/<int:order_id>/", views.mock_checkout, name="mock_checkout"),
    path("mock-pay/<int:order_id>/", views.mock_pay, name="mock_pay"),
    path("mock-cancel/<int:order_id>/", views.mock_cancel, name="mock_cancel"),

]