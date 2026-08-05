# 🚀 QA Automation — SauceDemo (Selenium + Python)

Automated UI testing framework for SauceDemo using Selenium WebDriver, Python, pytest, and the Page Object Model (POM). This project automates core user workflows including login, shopping cart, and checkout scenarios.

---

## Tech Stack

- Python 3.12
- Selenium WebDriver
- pytest
- Chrome WebDriver (Selenium Manager)
- Page Object Model (POM)

---

## Test Coverage

### Login (`test_login.py`)

- Valid login
- Invalid login
- Locked out user

### Cart & Checkout (`test_cart_checkout.py`)

- Add single item to cart
- Add multiple items to cart
- Remove item from product page
- Complete checkout flow
- Checkout validation (missing Last Name)

---

## Project Structure

```text
qa-selenium-saucedemo/
│
├── pages/
├── tests/
├── utils/
├── config.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## How to Run

Clone the repository

```bash
git clone https://github.com/Charvita-vali/qa-selenium-saucedemo.git
```

Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the tests

```bash
pytest
```

---

## Design Highlights

- Page Object Model (POM) for maintainable test code
- Reusable pytest fixtures for browser setup and login
- Explicit waits using Selenium WebDriverWait
- Shared configuration through `config.py`
- Modular project structure following automation framework best practices

---

## Author

**Charvita Vali**

GitHub:
https://github.com/Charvita-vali
