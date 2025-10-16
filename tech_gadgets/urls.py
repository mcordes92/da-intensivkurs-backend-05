from django.urls import path
from .views import start_page_view, single_gadget_view, single_gadget_slug_view, single_gadget_post_view

urlpatterns = [
    path('', start_page_view),
    path('gadget/<int:gadget_id>/', single_gadget_view),
    path('gadget/<slug:gadget_slug>/', single_gadget_slug_view, name="gadget_slug_url"),
    path("gadget/send_gadget/", single_gadget_post_view),
]