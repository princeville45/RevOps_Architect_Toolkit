"""
RevOps KPI Framework
Author: Irem Victor Chinonso | Statistical Business Architect
Date: 2026-05-12
Repo: RevOps-Architect-Toolkit

A modular KPI scoring framework for revenue operations.
Converts raw business data into actionable scores across
Sales Efficiency, Customer Health, and Revenue Quality.
"""

import pandas as pd
import numpy as np


def generate_business_data():
    """Simulate current period RevOps data."""
    return {
        "new_leads": 85,
        "qualified_leads": 42,
        "proposals_sent": 28,
        "deals_closed": 18,
        "deals_lost": 10,
        "revenue_ngn": 1_840_000,
        "revenue_target_ngn": 2_000_000,
        "avg_deal_size_ngn": 102_222,
        "avg_sales_cycle_days": 14,
        "customer_count": 94,
        "churned_customers": 6,
        "upsell_count": 12,
        "csat_score": 4.1,       # out of 5
        "support_tickets": 38,
        "resolved_tickets": 34,
        "mrr_ngn": 620_000,
        "prev_mrr_ngn": 580_000,
        "cac_ngn": 8_500,
        "ltv_ngn": 95_000,
    }


class KPIFramework:
    def __init__(self, data):
        self.d = data
        self.scores = {}

    def score_sales_efficiency(self):
        d = self.d
        lead_to_close = round(d["deals_closed"] / d["new_leads"] * 100, 2)
        qualified_rate = round(d["qualified_leads"] / d["new_leads"] * 100, 2)
        win_rate = round(d["deals_closed"] / (d["deals_closed"] + d["deals_lost"]) * 100, 2)
        quota_attainment = round(d["revenue_ngn"] / d["revenue_target_ngn"] * 100, 2)
        pipeline_velocity = round((d["qualified_leads"] * win_rate / 100 * d["avg_deal_size_ngn"]) / d["avg_sales_cycle_days"], 2)

        self.scores["Sales Efficiency"] = {
            "Lead to Close Rate (%)": lead_to_close,
            "Lead Qualification Rate (%)": qualified_rate,
            "Win Rate (%)": win_rate,
            "Quota Attainment (%)": quota_attainment,
            "Pipeline Velocity (NGN/day)": pipeline_velocity
        }
        return self.scores["Sales Efficiency"]

    def score_customer_health(self):
        d = self.d
        churn_rate = round(d["churned_customers"] / d["customer_count"] * 100, 2)
        upsell_rate = round(d["upsell_count"] / d["customer_count"] * 100, 2)
        csat_pct = round(d["csat_score"] / 5 * 100, 2)
        ticket_resolution = round(d["resolved_tickets"] / d["support_tickets"] * 100, 2)
        net_retention = round((d["customer_count"] - d["churned_customers"] + d["upsell_count"]) / d["customer_count"] * 100, 2)

        self.scores["Customer Health"] = {
            "Churn Rate (%)": churn_rate,
            "Upsell Rate (%)": upsell_rate,
            "CSAT Score (%)": csat_pct,
            "Ticket Resolution Rate (%)": ticket_resolution,
            "Net Revenue Retention (%)": net_retention
        }
        return self.scores["Customer Health"]

    def score_revenue_quality(self):
        d = self.d
        mrr_growth = round((d["mrr_ngn"] - d["prev_mrr_ngn"]) / d["prev_mrr_ngn"] * 100, 2)
        ltv_cac_ratio = round(d["ltv_ngn"] / d["cac_ngn"], 2)
        revenue_per_customer = round(d["revenue_ngn"] / d["customer_count"], 2)
        avg_deal_to_target = round(d["avg_deal_size_ngn"] / (d["revenue_target_ngn"] / d["deals_closed"]) * 100, 2)

        self.scores["Revenue Quality"] = {
            "MRR Growth (%)": mrr_growth,
            "LTV:CAC Ratio": ltv_cac_ratio,
            "Revenue per Customer (NGN)": revenue_per_customer,
            "Avg Deal vs Target (%)": avg_deal_to_target
        }
        return self.scores["Revenue Quality"]

    def compute_composite_score(self):
        """Weighted composite RevOps health score (0-100)."""
        d = self.d
        s1 = min(100, d["revenue_ngn"] / d["revenue_target_ngn"] * 100) * 0.35
        win_rate = d["deals_closed"] / (d["deals_closed"] + d["deals_lost"]) * 100
        s2 = min(100, win_rate) * 0.25
        churn = d["churned_customers"] / d["customer_count"] * 100
        s3 = max(0, 100 - churn * 5) * 0.20
        ltv_cac = d["ltv_ngn"] / d["cac_ngn"]
        s4 = min(100, ltv_cac * 10) * 0.20
        return round(s1 + s2 + s3 + s4, 1)

    def print_report(self):
        print("=" * 60)
        print("REVOPS KPI FRAMEWORK REPORT")
        print("RevOps Architect Toolkit | Irem Victor Chinonso")
        print("=" * 60)

        self.score_sales_efficiency()
        self.score_customer_health()
        self.score_revenue_quality()

        for category, metrics in self.scores.items():
            print(f"\n--- {category.upper()} ---")
            for metric, value in metrics.items():
                print(f"  {metric:<40} {value}")

        composite = self.compute_composite_score()
        print(f"\n{'='*60}")
        print(f"COMPOSITE REVOPS HEALTH SCORE: {composite}/100")
        if composite >= 80:
            print("Status: STRONG. Revenue engine is firing on all cylinders.")
        elif composite >= 60:
            print("Status: STABLE. Minor optimizations needed.")
        else:
            print("Status: AT RISK. Immediate attention required on key metrics.")
        print("=" * 60)


if __name__ == "__main__":
    data = generate_business_data()
    framework = KPIFramework(data)
    framework.print_report()
