from django.forms import ModelForm
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    full_name = forms.CharField(max_length = 100)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('full_name', 'username', 'email','password1', 'password2')

    def __init__ (self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)




# class PasswordChangeForm(SetPasswordForm):
#     """
#     A form that lets a user change their password by entering their old
#     password.
#     """
#     error_messages = dict(SetPasswordForm.error_messages, **{
#         'password_incorrect': _("Your old password was entered incorrectly. "
#                                 "Please enter it again."),
#     })
#     old_password = forms.CharField(label=_("Old password"),
#                                    widget=forms.PasswordInput)

#     def clean_old_password(self):
#         """
#         Validates that the old_password field is correct.
#         """
#         old_password = self.cleaned_data["old_password"]
#         if not self.user.check_password(old_password):
#             raise forms.ValidationError(
#                 self.error_messages['password_incorrect'],
#                 code='password_incorrect',
#             )
#         return old_password


# PasswordChangeForm.base_fields = OrderedDict(
#     (k, PasswordChangeForm.base_fields[k])
#     for k in ['old_password', 'new_password1', 'new_password2']
# )
