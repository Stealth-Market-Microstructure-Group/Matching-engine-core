# exchange-simulator

## Overview
A custom Python-based exchange simulator built from scratch to understand market microstructure and prepare for trading competitions (e.g., IMC Prosperity).  
It implements core execution infrastructure so strategies can be plugged in, tested, and measured.

## Current Features
- Limit and market orders with correct matching logic  
- FIFO time priority at each price level  
- Partial and full fills  
- Timezone-aware real timestamps for orders/trades  
- Trade logging (trade objects stored with execution details)  
- Modular separation: Order, Trade, OrderBook  
- Simple baseline implementation using `defaultdict` for price levels

## Roadmap / Planned Extensions
- Replace or augment the current data structures (beyond `defaultdict`) to handle higher throughput and large order books more efficiently  
- REST API layer so external agents/strategies can place orders like clients of an exchange, without importing internal code  
- Automated agents (e.g., market-making) with dynamic quoting logic  
- Inventory and PnL tracking per agent  
- Strategy testing harness (simulated ticks, injected noise, stress scenarios)  
- Visualization of performance metrics (PnL, inventory, spread over time)

## Usage (dev sandbox)
1. Clone the repo.  
2. Run the simulation driver (`simulate.py` when available) to initialize the order book and agents.  
3. Observe trades, inventory, and PnL via logs or exported CSV.  

*(Detailed commands and examples will be added as the driver and agent layers mature.)*

## Motivation
Generic online backtesting platforms hide execution-level mechanics. I built this from scratch to gain full control over order matching, latency behavior, and strategy integration — enabling realistic practice and rapid iteration for competition-style algorithmic trading.

## Status & Next Steps
- Core engine working: order book, matching, trade recording.  
- In progress: building automated market-making agents, adding REST API interface, improving internal data structures for scale, and introducing PnL/inventory tracking.  
- Future: expand into stress-tested strategy scenarios and add lightweight visualization for analysis.
