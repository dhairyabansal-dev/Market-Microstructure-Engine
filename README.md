# Market Microstructure Engine

A research-grade Python framework for studying market microstructure and execution quality.

## What it does

The engine turns order-book and trade data into measurable execution signals:

**Market Data → Order Book → Microstructure → Execution → Transaction Costs → Analytics**

Core research areas:
- Bid/ask spread and mid-price
- Microprice
- Order-book depth and liquidity
- Order imbalance
- Trade-flow metrics
- VWAP and TWAP execution
- Slippage
- Market impact
- Implementation shortfall
- Execution-quality analytics

## Project status

Phase 1 focuses on a deterministic, testable research core. The initial implementation uses in-memory market events so the framework can be tested without depending on a live data vendor.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
pytest
python examples/basic_analysis.py
```

## Design principles

1. Keep market-data ingestion separate from quantitative logic.
2. Make every metric deterministic and unit-testable.
3. Never hide assumptions about fills, costs, or market impact.
4. Prefer research transparency over black-box execution models.

## Disclaimer

This repository is for research and educational purposes. It is not investment advice and does not guarantee execution or trading performance.
