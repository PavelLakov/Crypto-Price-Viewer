# 🧠 Crypto Price Viewer

A simple Flask + JavaScript + SQLite application to view historical cryptocurrency prices.

---

## 🌐 Overview

This project allows users to:

- Select a cryptocurrency (Bitcoin, Ethereum, Cardano, etc.)
- Filter price data by date range
- View the data in a styled table
- Backend served via Flask API
- Frontend built with HTML, JavaScript, and CSS

---

## 🏗️ Project Structure

```text
Crypto-API/
├── static/
│   ├── script.js         # JavaScript that fetches and displays data
│   └── style.css         # Styling for the page and data table
├── templates/
│   └── index.html        # Frontend HTML page with UI
├── crypto_data.db        # SQLite database with multiple coin tables
├── api.py                # Flask backend that serves the API
└── README.md             # Project description and instructions
```

---

## 🧪 How It Works

1. User selects a coin and date range
2. Button triggers JavaScript `fetch()` call to Flask route: `/crypto/<coin_name>`
3. Flask queries the database and returns JSON
4. JavaScript filters by selected date range
5. Data appears in a styled table

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/crypto-api.git
cd crypto-api
```

### 2. Install Requirements

```bash
pip install flask flask-cors
```

### 3. Run the App

```bash
python api.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📦 Technologies Used

- **Python** (Flask)
- **JavaScript** (Fetch API)
- **HTML/CSS** (Frontend UI)
- **SQLite** (Data storage)

---

## 🎨 Features

- Animated title (`<h1>Crypto Price Viewer</h1>`)
- Date filtering using `<input type="date">`
- Mobile-friendly layout
- CSS styling with animations and hover effects

---

## 📊 Example Data Tables

Each table in `crypto_data.db` is named after a cryptocurrency:

```text
Avalanche
Bitcoin
BNB
Cardano
Chainlink
Dogecoin
Ethereum
Hedera
Litecoin
```

---

## 🔒 Notes

- Ensure that table names in the DB match dropdown values exactly.
- Run the app via Flask, not by opening `index.html` directly in the browser.

---

## 🧑‍💻 Author

Pavel Lakov  
Created with ❤️ using Python & JavaScript.
