# Distributor Service - Django Backend

This project provides a backend system for managing distributor onboarding and payment confirmations, with simulated integration points for SAP and Cashfree.

## Features

- Onboard new distributors with GST, PAN, and bank details
- Record and confirm payments with transaction metadata
- Simulated Cashfree payment confirmation
- Placeholder integration for SAP syncing
- REST API built with Django REST Framework

## Installation

1. Clone or unzip the project
2. Navigate to the project directory
3. Create a virtual environment and install dependencies:

```
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
```

4. Apply migrations and start the server:

```
python manage.py migrate
python manage.py runserver
```

## API Endpoints

See `apiGuide.txt` for a full list of endpoints and sample values.

## Integration Notes

- SAP: Sync functions are defined in `core/integrations/sap.py`
- Cashfree: Payment confirmation logic is in `core/integrations/cashfree.py` and can be extended for real API calls

## Requirements

- Python 3.8+
- Django 4.x
- djangorestframework

## License

This project is for educational/demo purposes.