from django import forms
from .models.customer import Customer

# class SimpleForm(forms.Form):
#     firstname = forms.CharField(max_length = 100)
#     lastname = forms.CharField(max_length = 100)

class GenderForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['gender']
        
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(GenderForm, self).__init__(*args, **kwargs)
        self.fields['gender'].label_from_instance = lambda gender: f"{gender.name}"
        

class HeightWeightForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['height', 'weight']
    
    def __init__(self, *args, **kwargs):
        super(HeightWeightForm, self).__init__(*args, **kwargs)
        self.fields['height'].widget.attrs['class'] = "number",  
        self.fields['weight'].widget.attrs['class'] = "number",
           
        self.fields["height"].widget.attrs.update({"min": '50'}),
        self.fields["height"].widget.attrs.update({"max": '250'}),     
        self.fields['height'].widget.attrs.update({'placeholder': 'cm'}),
        
        self.fields['weight'].widget.attrs.update({'min': '20'}),
        self.fields['weight'].widget.attrs.update({'max': '600'}),
        self.fields['weight'].widget.attrs.update({'placeholder': 'kg'}),    
        
class ColorForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['color']    

        # COLOR_CHOICES = (
        #         ('', 'Select an age'),
        #         ('10', '10'), #First one is the value of select option 
        #                       and second is the displayed value in option
        #         ('15', '15'),
        #         ('20', '20'),
        #         ('25', '25'),
        #         ('26', '26'),
        #         ('27', '27'),
        #         ('28', '28'),
        #         )
        
        widgets = {
            'color': forms.Select(attrs={'class': 'form-control'}),
        }
        
        # widgets = {
        #     'color': forms.RadioSelect(attrs={'class': 'form-control'}),
        # }
        
    
    def __init__(self, *args, **kwargs):
        super(ColorForm, self).__init__(*args, **kwargs)
        self.fields['color'].label_from_instance = lambda color: f"{color.name}"