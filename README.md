# High-Fidelity Exchange Simulation Core

## Author
* **Pankaj J.** - ([@pankajj6](https://github.com/pankajj6))

## Project Mandate
This repository contains the core engine for our group's proprietary market simulator. Its purpose is to provide a deterministic, high-fidelity environment for testing quantitative models and hypotheses against realistic market mechanics. It is a foundational piece of our research infrastructure.

## Core System Features
- **Order Book:** Full limit order book (LOB) implementation.
- **Matching Engine:** Strict Price/Time (FIFO) matching logic for limit and market orders.
- **Execution States:** Accurately models partial and full fills.
- **Data Integrity:** Employs timezone-aware, microsecond-precision timestamps for all events.
- **Architecture:** Modular design (`Order`, `Trade`, `OrderBook`) for stability and extension.
- **Logging:** Generates detailed execution logs for post-hoc analysis.

## Integration
The engine is designed to interface with the group's Kafka-based ITCH data pipeline. For current development and analysis, it can also be driven by custom data sources, including scraped market data. Refer to the primary driver script for implementation examples.
