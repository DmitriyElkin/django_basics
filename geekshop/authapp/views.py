from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from authapp.mixin import BaseClassContextMixin

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, TemplateView, UpdateView

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from authapp.models import User
from basket.models import Basket


class LoginView(FormView, BaseClassContextMixin):
    template_name = 'authapp/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('index')
    title = 'Geekshop | Авторизация'

    def form_valid(self, form):
        # вызывается после проверки "if form.is_valid():" в "django.views.generic.edit.ProcessFormView" в методе "post"
        user = auth.authenticate(username=form.data['username'], password=form.data['password'])
        if user.is_active:
            auth.login(self.request, user)
        else:
            print('юзер не активен')
        return super(LoginView, self).form_valid(form)


class RegisterView(CreateView, BaseClassContextMixin):
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('authapp:login')
    title = 'Geekshop | Регистрация'

    def form_valid(self, form):
        messages.success(self.request, 'Успешная регистрация')
        return super(RegisterView, self).form_valid(form)


class ProfileView(UpdateView, BaseClassContextMixin):
    template_name = 'authapp/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('authapp:profile')
    model = User
    title = 'Geekshop | Профайл'

    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        self.kwargs['pk'] = self.user.id
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.user)
        return context


class LogoutView(TemplateView, BaseClassContextMixin):
    template_name = 'mainapp/index.html'
    title = 'Geekshop | Logout'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
