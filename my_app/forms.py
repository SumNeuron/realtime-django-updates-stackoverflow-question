from django import forms
from django.core import validators
from django.utils.translation import gettext as _


# a basic field to scrub text into integers
class IntegerField(forms.Field):
    def to_python(self, value):
        just_digits = ''.join(char for char in value if (char.isdigit() or  char == "."))
        if not just_digits:
            return value
        return just_digits

    def validate(self, value):
        super(IntegerField, self).validate(value)
        errors = []
        try:
            value = round(float(value))
        except ValueError:
            errors += [
                forms.ValidationError(
                    _('Given value %(value)s is not an integer.'),
                    code='NaI',
                    params={'value':value},
                )
            ]

        if errors:
            raise forms.ValidationError(errors)



# our simple form
class MyForm(forms.Form):
    a = IntegerField(
            label='a',
            widget=forms.TextInput(
                attrs={
                'id':'a',
                'name': 'a',
                'placeholder': '3'
                }
            )
        )
    b = IntegerField(
            label='b',
            widget=forms.TextInput(
                attrs={
                'id':'b',
                'name': 'b',
                'placeholder': '3'
                }
            )
        )


    def clean(self):
        cleaned_data = super(MyForm, self).clean()

        a = cleaned_data.get('a')
        b = cleaned_data.get('b')
