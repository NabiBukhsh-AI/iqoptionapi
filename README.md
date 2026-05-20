# IQ Option API — Python

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Maintained by](https://img.shields.io/badge/maintained%20by-NabiBukhsh--AI-brightgreen)](https://github.com/NabiBukhsh-AI/iqoptionapi)

> **Unofficial** community-maintained Python wrapper for the IQ Option WebSocket/HTTP API.
> For educational and research purposes only. **Do not use on a real account with money you cannot afford to lose.**

---

## What's new in this fork

- **Python 3.8–3.12 compatible** — updated `websocket-client` to `>=1.6.0` (fixes broken callbacks from the old `0.56` pin)
- **CPU bug fixed** — replaced all spin-wait `while x == None: pass` loops with `time.sleep(0.001)` to stop pegging the CPU at 100%
- **Logic bugs fixed** — operator-precedence bug in `start_mood_stream` / `stop_mood_stream` that caused subscriptions to never register correctly
- **Duplicate message handler removed** — `order_placed_temp` was called twice per WebSocket message
- **Unreachable code removed** — dead `break` and `time.sleep` statements after `return`
- **Type hints** added to all major public methods (`connect`, `buy`, `get_candles`, `get_balance`, `buy_digital_spot`, …)
- **Clean package exports** — `from iqoptionapi import IQ_Option` now works directly
- **`pylint` removed from runtime dependencies** — it's a dev tool, not a runtime requirement

---

## Requirements

- Python 3.8 or higher
- An IQ Option account (practice account recommended)

---

## Installation

```bash
pip install git+https://github.com/NabiBukhsh-AI/iqoptionapi.git
```

Or clone and install locally:

```bash
git clone https://github.com/NabiBukhsh-AI/iqoptionapi.git
cd iqoptionapi
pip install -e .
```

---

## Quick start

```python
from iqoptionapi import IQ_Option
import time

api = IQ_Option("your@email.com", "your_password")

# Connect (returns True on success)
status, reason = api.connect()
if not status:
    print("Login failed:", reason)
    exit(1)

# Switch to practice balance
api.change_balance("PRACTICE")
print("Balance:", api.get_balance())

# Fetch the last 100 one-minute candles for EUR/USD
candles = api.get_candles("EURUSD", 60, 100, time.time())
print("Latest close:", candles[-1]["close"])

# Place a 1-minute binary option (call, $1)
success, order_id = api.buy(1, "EURUSD", "call", 1)
if success:
    print("Order placed, id:", order_id)
    result = api.check_win_v4(order_id)
    print("Result:", result)
```

### Two-factor authentication (2FA)

```python
status, reason = api.connect()
if reason == "2FA":
    code = input("Enter SMS code: ")
    status, reason = api.connect_2fa(code)
```

---

## API reference

### Connection

| Method | Description |
|---|---|
| `connect(sms_code=None)` | Connect to IQ Option. Returns `(True, None)` on success or `(False, reason)` on failure. |
| `connect_2fa(sms_code)` | Complete a 2FA login with the SMS code. |
| `check_connect()` | Returns `True` if the WebSocket is connected. |

### Account

| Method | Description |
|---|---|
| `get_balance()` | Current balance amount. |
| `get_balance_mode()` | `"REAL"`, `"PRACTICE"`, or `"TOURNAMENT"`. |
| `change_balance(mode)` | Switch between `"REAL"`, `"PRACTICE"`, `"TOURNAMENT"`. |
| `get_currency()` | Account currency string (e.g. `"USD"`). |
| `reset_practice_balance()` | Reset practice account to default balance. |

### Candles

| Method | Description |
|---|---|
| `get_candles(active, interval, count, endtime)` | Fetch historical candles. `interval` in seconds (e.g. `60`). |
| `start_candles_stream(active, size, maxdict)` | Subscribe to real-time candles. `size` is seconds or `"all"`. |
| `stop_candles_stream(active, size)` | Unsubscribe from real-time candles. |
| `get_realtime_candles(active, size)` | Read the latest real-time candle data. |

### Binary / Turbo options

| Method | Description |
|---|---|
| `buy(price, active, direction, duration)` | Place a binary option. `direction`: `"call"` or `"put"`. Returns `(result, order_id)`. |
| `buy_multi(prices, actives, directions, expirations)` | Place multiple options at once. |
| `check_win_v4(order_id)` | Block until the option closes. Returns `(win, profit)`. |
| `sell_option(options_ids)` | Sell an open option early. |

### Digital options

| Method | Description |
|---|---|
| `buy_digital_spot(active, amount, action, duration)` | Place a digital option. `action`: `"call"` or `"put"`. |
| `sell_digital_option(options_ids)` | Sell a digital option early. |
| `get_digital_current_profit(active, duration)` | Current payout percentage for a digital option. |

### Market data

| Method | Description |
|---|---|
| `get_all_open_time()` | Dict of which assets are currently open for trading. |
| `get_all_profit()` | Payout percentages for all binary/turbo actives. |
| `get_traders_mood(active)` | Percentage of traders going higher (put %). |
| `start_mood_stream(active)` | Subscribe to traders-mood updates. |
| `get_technical_indicators(active)` | Fetch technical indicator data for an active. |

---

## Asset names

Use standard ticker strings like `"EURUSD"`, `"GBPUSD"`, `"BTCUSD"`, etc.
For a full list of available actives call:

```python
api.get_all_ACTIVES_OPCODE()
```

---

## Disclaimer

This is an **unofficial**, **unsupported** project not affiliated with IQ Option.
Use at your own risk. The authors accept no liability for financial losses.

---

## Contributing

Pull requests are welcome. Please open an issue first to discuss the change.

## License

MIT
