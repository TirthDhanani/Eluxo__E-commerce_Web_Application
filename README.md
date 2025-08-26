Eluxo — Django E-commerce Web App

A production-style e-commerce web application built with Django and vanilla JS/jQuery + AJAX. Eluxo supports seller-managed product listings, coupon engine, order tracking, OTP-based password reset, and Razorpay payments. Deployed demo: https://tirthdhanani.pythonanywhere.com/

✨ Features

Customer-facing

Product catalog with category filter, manual price-range slider, sort by newness/price, and pagination that keeps filters.

AJAX cart (add/update/remove) with live totals.

Coupon application via AJAX (min/max thresholds, validity window).

Secure authentication (login/signup), session-based cart persistence.

OTP-based “Forgot Password” via email.

Order tracking: buyers see live delivery status updates.

Admin panel (seller workflow)

Sellers/admins add/update/delete categories, subcategories, and products; changes reflect instantly on storefront.

Coupons: create/edit/delete with min/max order value; auto-validation on cart.

Orders: list all orders; update delivery status in real time (buyers see updates).

Basic dashboard for quick ops.

Payments

Razorpay checkout (order creation, signature verification).

🧱 Tech Stack

Backend: Django, Django ORM, Sessions

Frontend: HTML5, CSS3, JavaScript, jQuery, AJAX

Payments: Razorpay

Email (OTP): Django email backend (SMTP or console for dev)

DB: SQLite (dev) or PostgreSQL/MySQL (prod)

Deploy: PythonAnywhere (demo)
