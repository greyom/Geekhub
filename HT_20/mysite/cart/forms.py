from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        quant = kwargs.pop('quant', None)
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        if quant:
            quant_choices = [(i, str(i)) for i in range(1, quant['quant'] + 1)]
            self.fields['quantity'].choices = quant_choices
