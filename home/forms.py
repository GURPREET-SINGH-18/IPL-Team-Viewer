from django.db.models import fields
from django.forms import ModelForm,forms
from .models import addteam
class addteamform(ModelForm):
    class Meta:
        model = addteam
        fields=['teamname','player','batsmen','bowler','wk','coach','img']