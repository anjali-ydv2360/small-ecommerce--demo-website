# Django Stripe Shop (Mock Payment)

## Project Overview
This project is a simple Django + PostgreSQL ecommerce demo with 3 fixed products.

Users can:
- View products on the homepage
- Enter quantities
- Click Buy
- Complete a checkout flow (mock Stripe)
- See their paid orders listed on the homepage under "My Orders"

---

## Assumptions
- Products are fixed (added manually through Django admin).
- No user authentication (all orders are global).
- No shipping/tax calculations.
- Only 1 HTML page is required for product listing and order listing.

---

## Payment Flow Chosen
### Mock Stripe Checkout (Stripe simulation)

Normally Stripe Checkout would be used, but Stripe test keys could not be generated due to account onboarding restrictions.

So instead of real Stripe payment, this project simulates Stripe Checkout with a mock checkout page.

Flow:
1. User selects quantities and clicks Buy.
2. Order is created in database with status = `pending`.
3. User is redirected to `/mock-checkout/<order_id>/`.
4. User clicks "Pay" to mark order as `paid`.
5. Paid order appears on homepage under "My Orders".

---

## How double-submit / refresh issues are avoided
- When "Pay" is clicked, order status is updated only if it is not already `paid`.
- Refreshing the payment page does not create duplicate paid orders.
- An order can be paid only once.

---

## Setup Instructions

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd stripe_shop
```

### 2. Create a virtual environment
```bash
python -m venv virtual
```
### 3. Activate the virtual environment

Windows
```bash
virtual\Scripts\activate
```

macOS / Linux
```bash
source virtual/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```
### PostgreSQL Setup
```bash
CREATE DATABASE stripe_shop_db;
CREATE USER stripe_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE stripe_shop_db TO stripe_user;
```

### Environmental variables

DEBUG=True

DB_NAME=stripe_shop_db
DB_USER=stripe_user
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
---

### 5. Apply database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the development server
```bash
python manage.py runserver
```

Open your browser and visit:
http://127.0.0.1:8000/

### Create Admin User (Optional)

To access the Django admin panel:
```bash
python manage.py createsuperuser
```

Admin panel URL:
http://127.0.0.1:8000/admin/

<img width="1869" height="1077" alt="Screenshot 2026-04-09 145412" src="https://github.com/user-attachments/assets/fa50cfb9-80d2-471f-80e9-ed9950f9a4b7" />

<img width="959" height="577" alt="Screenshot 2026-04-09 210223" src="https://github.com/user-attachments/assets/731e6910-f07b-432b-9cd1-5a5c52b1cf0a" />

