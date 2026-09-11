# Market Microstructure Engine 📊

A small Python project for understanding **market microstructure and trade execution** through an order-book simulation.

## What it covers

- Bid/ask spread and mid-price
- Microprice
- Order-book depth
- Order imbalance
- TWAP and VWAP scheduling
- Market-order execution
- Slippage
- Implementation shortfall
- Basic transaction-cost calculations
- Simple Streamlit dashboard

### Flow

```text
Order Book
    ↓
Microstructure Metrics
    ↓
Execution Simulation
    ↓
Slippage / Costs
    ↓
Execution Analysis
```

## Run it

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

Run the tests:

```bash
pytest
```

Run the example:

```bash
python examples/basic_analysis.py
```

Run the dashboard:

```bash
streamlit run app.py
```

## Project structure

```text
Market-Microstructure-Engine/
├── app.py
├── examples/
├── src/market_microstructure/
│   ├── order_book.py
│   ├── metrics.py
│   ├── execution.py
│   ├── strategies.py
│   └── costs.py
├── tests/
├── docs/
├── requirements.txt
└── pyproject.toml
```

## Why I built it

The goal is to move beyond just looking at prices and understand **how liquidity, order-book imbalance and execution costs affect a trade**.

The current version intentionally uses synthetic/in-memory order-book data so the calculations stay easy to inspect and test. A future version can plug in historical Level-2 data.

## Note

This is a research/learning project, not a live trading system or investment advice.
