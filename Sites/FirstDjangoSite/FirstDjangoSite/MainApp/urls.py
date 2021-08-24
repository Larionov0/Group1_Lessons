from django.urls import path, include
from .views import *


urlpatterns = [
    path('first', first_view),
    path('all_cities', show_cities),
    path('all_reviews', all_reviews),
    path('edit_review/<int:rev_id>', edit_review),
    path('create_review', create_review),
    path('delete_review/<int:rev_id>', delete_review)
]
