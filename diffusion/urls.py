from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:user_id>/", views.read_user, name="read_user"),
    path(
        "user/<int:user_id>/item/<int:item_id>/",
        views.read_user_item,
        name="read_user_item",
    ),
    path("form/", views.get_form, name="get_form"),
    path(
        "form/we_got_a_sentence",
        views.we_got_a_sentence,
        name="we_got_a_sentence",
    ),
]
