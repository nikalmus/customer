import re
class ZipCodeValidationMixin:
    def validate_zip_code(self, form):
        zip_code = form.cleaned_data.get('zip_code')
        if not re.match(r'^\d{5}(?:-\d{4})?$', zip_code):
            form.add_error('zip_code', 'Enter a valid ZIP code in the format XXXXX or XXXXX-XXXX.')
            return False
        return True

