from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from ingredientes.models import Usuario

class MyBackend(ModelBackend):
  def authenticate(self, request, username=None, password=None):
    try:
      # Try to find a user matching your username
      user = Usuario.objects.get(Usuario=username)

      #  Check the password is the reverse of the username
      if password == user.Password:
        # Yes? return the Django user object
        return user
      else:
        # No? return None - triggers default login failed
        return None
    except Usuario.DoesNotExist:
      # No user was found, return None - triggers default login failed
      return None

    # Required for your backend to work properly - unchanged in most scenarios
  def get_user(self, user_id):
    try:
      return Usuario.objects.get(pk=user_id)
    except Usuario.DoesNotExist:
      return None