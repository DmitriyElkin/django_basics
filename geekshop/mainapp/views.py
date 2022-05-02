from django.views.generic import DetailView, TemplateView, ListView
from mainapp.models import Product, ProductCategories


class IndexTemplateView(TemplateView):
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop'
        return context


class ProductListView(ListView):
    template_name = 'mainapp/products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        if self.kwargs.get('id_category'):
            products_ = Product.objects.filter(category_id=self.kwargs['id_category'])
        else:
            products_ = Product.objects.all()
        return products_

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop | Каталог'
        context['categories'] = ProductCategories.objects.all()
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'
