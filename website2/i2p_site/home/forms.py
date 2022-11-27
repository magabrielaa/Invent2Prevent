from django import forms

RACE_CHOICES =(
    ("1", "White"),
    ("2", "Black"),
    ("3", "Hispanic"),
    ("4", "Other"),
)

GENDER_CHOICES =(
    ("1", "Female"),
    ("2", "Male"),
    ("3", "Other"),
)

AGE_CHOICES =(
    ("1", "12–15"),
    ("2", "16–19"),
    ("3", "20–24"),
    ("4", "25–34"),
    ("5", "35–49"),
    ("6", "50–64"),
    ("7", "65 or older"),
)


class InputYourInfoForm(forms.Form):
    race = forms.MultipleChoiceField(choices = RACE_CHOICES)
    gender = forms.MultipleChoiceField(choices = GENDER_CHOICES)
    age = forms.MultipleChoiceField(choices = AGE_CHOICES)
