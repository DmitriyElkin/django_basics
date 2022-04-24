from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, AdminCategoryForm, AdminProductForm
from authapp.models import User
from mainapp.models import ProductCategories, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


# Пользователи

@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'title': 'Admin | Пользователи',
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Admin | Регистрация',
        'form': form
    }
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_update(request, id):
    user_select = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'Admin | Редактирование пользователя',
        'form': form,
        'user_select': user_select
    }
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('adminapp:admin_users'))


# Категории

@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    context = {
        'title': 'Admin | Категории',
        'categories': ProductCategories.objects.all()
    }
    return render(request, 'adminapp/admin-categories-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_create(request):
    if request.method == 'POST':
        form = AdminCategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_categories'))
        else:
            print(form.errors)
    else:
        form = AdminCategoryForm()
    context = {
        'title': 'Admin | Новая категория',
        'form': form
    }
    return render(request, 'adminapp/admin-category-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_update(request, id):
    category_select = ProductCategories.objects.get(id=id)
    if request.method == 'POST':
        form = AdminCategoryForm(data=request.POST, instance=category_select)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_categories'))
        else:
            print(form.errors)
    else:
        form = AdminCategoryForm(instance=category_select)
    context = {
        'title': 'Admin | Редактирование категории',
        'form': form,
        'category_select': category_select
    }
    return render(request, 'adminapp/admin-category-update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_delete(request, id):
    ProductCategories.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('adminapp:admin_categories'))


# Продукты

@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {
        'title': 'Admin | Продукты',
        'products': Product.objects.all()
    }
    return render(request, 'adminapp/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_create(request):
    if request.method == 'POST':
        form = AdminProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_products'))
        else:
            print(form.errors)
    else:
        form = AdminProductForm()
    context = {
        'title': 'Admin | Новый продукт',
        'form': form
    }
    return render(request, 'adminapp/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_update(request, id):
    product_select = Product.objects.get(id=id)
    if request.method == 'POST':
        form = AdminProductForm(data=request.POST, instance=product_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_products'))
        else:
            print(form.errors)
    else:
        form = AdminProductForm(instance=product_select)
    context = {
        'title': 'Admin | Редактирование продукта',
        'form': form,
        'product_select': product_select
    }
    return render(request, 'adminapp/admin-product-update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_delete(request, id):
    Product.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('adminapp:admin_products'))
