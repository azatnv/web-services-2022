# from django.shortcuts import render
from django.http import (
    HttpResponse,
    JsonResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from typing import Optional
from django.shortcuts import render
from django import forms

"""
    Responses for "http://localhost:8000/diffusion/" requests
"""


class SentenceForm(forms.Form):
    sentence = forms.CharField(label="Enter any sentence", max_length=100)

    def clean(self):
        cleaned_data = super(forms.Form, self).clean()
        sentence = cleaned_data.get("sentence")
        if not sentence:
            raise forms.ValidationError("You have to write something!")


def index(request):
    """
    url:
        http://localhost:8000/diffusion/
    """
    return HttpResponse("Hello, world. You're at the diffusion index.")


def read_user(request, user_id: str):
    """
    url:
        http://localhost:8000/diffusion/1/?q=123
    """
    q = request.GET.get("q", "")
    if q:
        return JsonResponse({"user_id": user_id, "q": q})
    else:
        return JsonResponse({"user_id": user_id})


def read_user_item(request, user_id: str, item_id: str):
    """
    url:
        http://localhost:8000/diffusion/user/1/item/634/?q=some_text&short=True
    """
    q = request.GET.get("q", "")
    short = request.GET.get("short", "False").lower() == "true"

    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )

    return JsonResponse(item)


def get_form(request):
    """
    url: http://localhost:8000/diffusion/form
    """
    form = SentenceForm()

    return render(request, "form.html", {"form": form})


def we_got_a_sentence(request):
    """
    Getting a sentence from POST request
    """
    if request.method == "POST":
        sentence = request.POST.get("sentence", "")
        return HttpResponse(f"You have entered a sentence: {sentence}")
    else:
        return HttpResponseNotFound("Page not found :(")
