from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, AdminCategoryForm, AdminProductForm
from authapp.models import User
from adminapp.mixin import BaseClassContextMixin, CustomDispatchMixin
from mainapp.models import ProductCategories, Product
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView


class IndexTemplateView(TemplateView, BaseClassContextMixin, CustomDispatchMixin):
    template_name = 'adminapp/admin.html'
    title = 'Admin'


# Пользователи

class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    title = 'Admin | Пользователи'
    context_object_name = 'users'


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    title = 'Admin | Регистрация'
    success_url = reverse_lazy('adminapp:admin_users')


class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    title = 'Admin | Редактирование пользователя'
    success_url = reverse_lazy('adminapp:admin_users')


class UserDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('adminapp:admin_users')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False if self.object.is_active else True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Категории

class CategoryListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-categories-read.html'
    title = 'Admin | Категории'
    context_object_name = 'categories'


class CategoryCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-category-create.html'
    form_class = AdminCategoryForm
    title = 'Admin | Новая категория'
    success_url = reverse_lazy('adminapp:admin_categories')


class CategoryUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-category-update.html'
    form_class = AdminCategoryForm
    title = 'Admin | Редактирование категории'
    success_url = reverse_lazy('adminapp:admin_categories')


class CategoryDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-category-update.html'
    success_url = reverse_lazy('adminapp:admin_categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


# Продукты

class ProductListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-read.html'
    title = 'Admin | Продукты'
    context_object_name = 'products'


class ProductCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-product-create.html'
    form_class = AdminProductForm
    title = 'Admin | Новый продукт'
    success_url = reverse_lazy('adminapp:admin_products')


class ProductUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-product-update.html'
    form_class = AdminProductForm
    title = 'Admin | Редактирование продукта'
    success_url = reverse_lazy('adminapp:admin_products')


class ProductDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-product-update.html'
    success_url = reverse_lazy('adminapp:admin_products')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
