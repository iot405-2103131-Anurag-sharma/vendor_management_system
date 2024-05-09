# vendor_management_system
# vendor-management-system-django

Develop a Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics

## version used

- Python (version 3.10.8)
- Django (version 4.2.7)

## Installation

# 2.Create a virtual environment:
python -m venv venv  
source venv/bin/activate  # For Linux/Mac  
venv\Scripts\activate     # For Windows  

# 3.Install dependencies:
pip install -r requirements.txt  

# 4.Database setup:
python manage.py makemigrations  
python manage.py migrate  
# 4.1 mysql database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'annu_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
we can use mysql database in project
# 5.Create a superuser:
python manage.py createsuperuser
superuser login username =vendor
superuser pswrd = vendor

## Usage
# 1.Start the server:
python manage.py runserver  

# 2.Access API endpoints:

## Vendor API: /vendor/
Purchase Order API: 'purchase/purchase_api/'  
Historical metrices API:'performance_metrics/metrices_api/'
 


## API Endpoints
Vendor API  
● POST /api/vendors/: Create a new vendor.  
● GET /api/vendors/: List all vendors.  
● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.  
● PUT /api/vendors/{vendor_id}/: Update a vendor's details.  
● DELETE /api/vendors/{vendor_id}/: Delete a vendor  
  
● Vendor Performance Endpoint (GET /api/vendors/{vendor_id}/performance)  
  
Purchase Order API  
● POST /api/purchase_orders/: Create a purchase order.  
● GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.  
● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.  
● PUT /api/purchase_orders/{po_id}/: Update a purchase order.  
● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order  
  
Vendor Performance Evaluation  
● GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance metrics  

Historical Performance API  
GET /vendor/historical_performance: List historical performance for all vendors.  
GET /vendor/historical_performance/{id}/: Retrieve historical performance for a specific vendor.  
  
Update Acknowledgment Endpoint:  
● While not explicitly detailed in the previous sections, consider an endpoint like  
POST /api/purchase_orders/{po_id}/acknowledge for vendors to acknowledge POs.  
● This endpoint will update acknowledgment_date and trigger the recalculationof average_response_time  

## Running Tests  
Run the test suite:  
  python manage.py test  



