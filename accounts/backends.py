from django.contrib.auth import get_user_model


User = get_user_model()
class UserEmailBackedn:
    '''
    Override Authenticate Method For A Custom Backend  User Can log in With Email , Password 
    '''
    def authenticate(self, request, username=None, password=None):

        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None 
    
    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None
