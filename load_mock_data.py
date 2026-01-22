import os
import django
import json
from datetime import datetime

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')
django.setup()

from store.models import Customer

# Load the JSON data
with open('store/fixtures/MOCK_DATA.json') as f:
    data = json.load(f)

# Create Customer objects
for item in data:
    birth_date_str = item.get('birth_date')
    if birth_date_str:
        # Parse the date from dd/mm/yyyy format
        birth_date = datetime.strptime(birth_date_str, '%d/%m/%Y').date()
    else:
        birth_date = None

    Customer.objects.create(
        first_name=item['first_name'],
        last_name=item['last_name'],
        email=item['email'],
        phone=item.get('phone') or '',
        birth_date=birth_date,
        membership=item['membership']
    )

print("Mock data loaded successfully into the Customer model.")