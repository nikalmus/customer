from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Customer

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'
    ordering = ['-id']

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['first_name', 'last_name', 'address', 'city', 'zip_code', 'state']
    success_url = reverse_lazy('customer-list')

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['first_name', 'last_name', 'address', 'city', 'zip_code', 'state']
    success_url = reverse_lazy('customer-list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('customer-list')
