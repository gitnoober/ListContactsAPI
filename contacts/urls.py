from django.urls import path
# from .views import ContactList , ContactDetailView
from .views import ContactList , ContactDetailView

urlpatterns = [
    path('' , ContactList.as_view()), #maps /contacts to this
    path('<int:id>' , ContactDetailView.as_view() #maps /contacts/id to this
            )
]
