from django import forms

class PollForm(forms.Form):
    #Question validation
    question = forms.CharField(widget=forms.Textarea, required=True)

    #Choices validation
    def __init__(self, *args, **kwargs):
        #Gets by parameter in keyword arguments the choices count
        count = kwargs.pop('count', 3)
        super(PollForm, self).__init__(*args, **kwargs)
        print("Count:" + str(count))
        #Validates each choice
        for x in range(int(count)):
            self.fields['choice_' + str(x+1)] = forms.CharField(widget=forms.Textarea, required=True)
