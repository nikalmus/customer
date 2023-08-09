from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Customer
from .mixins import ZipCodeValidationMixin
    

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'
    ordering = ['-id']

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('customer-list')

class CustomerCreateView(ZipCodeValidationMixin, CreateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['first_name', 'last_name', 'address', 'city', 'zip_code', 'state']
    success_url = reverse_lazy('customer-list')

    def form_valid(self, form):
        if not self.validate_zip_code(form):
            return self.form_invalid(form)
        return super().form_valid(form)

class CustomerUpdateView(ZipCodeValidationMixin,UpdateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['first_name', 'last_name', 'address', 'city', 'zip_code', 'state']
    success_url = reverse_lazy('customer-list')

    def form_valid(self, form):
        if not self.validate_zip_code(form):
            return self.form_invalid(form)
        return super().form_valid(form)


