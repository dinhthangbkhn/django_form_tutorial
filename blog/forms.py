from django import forms 


EMPTY_CHOICES = (
    ('', '-'*10)
)

GENDER_CHOICES = (
    ('man', '男'),
    ('woman', '女')
)

FOOD_CHOICES = (
    ('apple', 'りんご'),
    ('beef', '牛肉')
)

class SampleForm(forms.Form):
    age = forms.IntegerField(
        label='年齢',
        min_value=0,
        max_value=200,
        required=True
    )

    birthday = forms.DateField(
        label='誕生日',
        required=True,
        input_formats=[
            '%Y-%m-%d',
            '%Y/%m/%d',
        ]
    )

    send_message = forms.BooleanField(
        label='送信する',
        required=False, 
    )

    gender_s = forms.ChoiceField(
        label='性別',
        widget=forms.Select,
        choices= GENDER_CHOICES,
        required = False,
    )

