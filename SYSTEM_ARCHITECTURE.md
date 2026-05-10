# 🕸️ Total Overlay: System Architecture Map
**Synchronized Data Ecosystem | Mirrored Logic Architecture**
**Architect: Irem Victor Chinonso**

This document outlines the **"Total Overlay"** strategy—a zero-friction data environment where every operational action triggers a mirrored response across the entire technical stack.

---

## 🏗️ The Three-Tier Architecture

### 1. The Input Layer (Real-Time Operations)
*   **Mobile Interface (InShot / WhatsApp):** Rapid content assembly and field sales logging.
*   **Depot Operations Hub:** Manual entry points for inventory movement at the bottled water depot.

### 2. The Logic Layer (The "Total Overlay" Sync)
*   **Google Sheets (The Ledger):** Acts as the primary transactional database for revenue and stock movement.
*   **Airtable (The Relational Core):** Houses the deep connections between products, customers, and logistics status.
*   **Notion (The Knowledge Vault):** Stores the long-term documentation, script bank, and statistical frameworks.

### 3. The Automation Layer (Connective Tissue)
*   **n8n Orchestration:** A series of self-hosted workflows that watch for a change in *Google Sheets* and instantly update the corresponding record in *Airtable*.
*   **Apps Script Triggers:** Ensures that every new sales entry triggers a **Normalization Event** (converting NGN to USD via the `normalization_engine.py`).

### 4. The Intelligence Layer (Decision Support)
*   **Global ROI Optimizer:** A high-level weighting engine (`global_roi_optimizer.py`) that calculates the daily "Success Index" across Sales, Content, and Education.
*   **Predictive Logistics:** Forecasts stock depletion to prevent revenue leakage at the Depot.

---

## 🔄 The Mirrored Sync Workflow
1.  **Action:** Sales Associate logs a sale of 50 units in Ife, Nigeria.
2.  **Trigger:** n8n detects the new row in the C-Way Dashboard (Google Sheets).
3.  **Process:**
    *   `normalization_engine.py` standardizes the revenue.
    *   `predictive_modeling.py` updates the "Stock Depletion" forecast.
4.  **Result:** Airtable displays the updated inventory level, and the "Street Code Studios" production budget reflects the new available capital.

---
## 🎯 Goal: Zero Manual Duplication
The architecture is designed so that no piece of data is ever entered twice. It is a "Living Mirror" of the business.

**Status: Architecture Optimized.**
