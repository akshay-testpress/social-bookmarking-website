from .models import Event, EventTimes
from django import forms
from django.utils import timezone


class AddEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'place', 'description', 'tags',)


class AddEventTimeForm(forms.ModelForm):

    start_time = forms.DateTimeField(initial=timezone.now(), required=True,)
    end_time = forms.DateTimeField(initial=timezone.now(), required=False,)

    class Meta:
        model = EventTimes
        fields = ('is_all_day',)

    def clean(self):
        cleaned_data = super().clean()
        is_all_day = cleaned_data.get('is_all_day')
        end_time = cleaned_data.get('end_time')
        self.check_starting_date(cleaned_data.get('start_time'))

        if ((is_all_day is True and str(end_time) != 'None') or
                (is_all_day is False and str(end_time) == 'None')):
            raise forms.ValidationError(
                "Either you have to select all day or end date"
            )
        return cleaned_data

    def check_starting_date(self, start_time):
        if start_time <= timezone.now():
            raise forms.ValidationError(
                "Please enter a valid start date"
            )
