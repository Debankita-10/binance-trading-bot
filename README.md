# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot for Binance Futures Testnet (USDT-M).

It supports:

* MARKET orders
* LIMIT orders
* BUY and SELL operations
* Command-line input
* Logging
* Error handling
* Input validation

---

## Tech Stack

* Python 3.x
* python-binance
* python-dotenv
* argparse
* logging

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── __init__.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Setup Instructions

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add API Keys

Create `.env` file:

```env
API_KEY=your_api_key
API_SECRET=your_secret_key
```

---

## Run Examples

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000
```

---

## Features

* Binance Futures Testnet integration
* MARKET & LIMIT order support
* BUY/SELL support
* CLI input handling
* Logging system
* Exception handling
* Structured modular code

---

## Author

Debankita Poddar
