from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
def logout_view(request):
 logout(request)
 return redirect('/')
class CustomLoginView(LoginView):
 def get_success_url(self):
# Redirection vers l'URL de la page d'accueil après la connexion
  return '/'

