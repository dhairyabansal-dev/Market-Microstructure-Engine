# Architecture

```text
                    ┌────────────────────┐
                    │    Market Data     │
                    │ quotes / trades    │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │   Order Book       │
                    │ L2 state + quotes  │
                    └─────────┬──────────┘
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
       ┌───────────┐    ┌────────────┐   ┌────────────┐
       │ Spread    │    │ Microprice │   │ Imbalance  │
       └─────┬─────┘    └─────┬──────┘   └─────┬──────┘
             └─────────────────┼────────────────┘
                               ▼
                    ┌────────────────────┐
                    │ Execution Simulator │
                    │ fills + benchmarks  │
                    └─────────┬──────────┘
                              ▼
                    ┌────────────────────┐
                    │ Cost / Slippage    │
                    │ implementation     │
                    │ shortfall          │
                    └─────────┬──────────┘
                              ▼
                    ┌────────────────────┐
                    │ Research Analytics │
                    └────────────────────┘
```

The architecture intentionally separates state, metrics, execution logic, and analysis so each layer can be replaced or extended independently.
