def calculate_pipeline_health(stages_data):
    """
    Scores CRM pipeline stages on a scale of 0-100.
    stages_data: list of dicts with stage_name, deal_count, avg_value, avg_days, conv_rate
    """
    scored_stages = []
    for stage in stages_data:
        # Scoring Logic
        # 1. Conversion Rate (Higher is better) - Weight: 40%
        # 2. Velocity (Lower avg_days is better) - Weight: 30%
        # 3. Deal Volume (Higher is better, but needs balance) - Weight: 30%
        
        conv_score = stage['conv_rate'] * 40
        velocity_score = max(0, (30 - stage['avg_days']) / 30) * 30
        volume_score = min(30, (stage['deal_count'] / 10) * 30)
        
        total_health = conv_score + velocity_score + volume_score
        
        status = "Healthy" if total_health > 70 else "At Risk" if total_health > 40 else "Critical"
        
        scored_stages.append({
            "stage": stage['stage_name'],
            "score": round(total_health, 2),
            "status": status,
            "bottleneck": "Yes" if total_health < 50 else "No"
        })
    return scored_stages

if __name__ == "__main__":
    pipeline = [
        {"stage_name": "Discovery", "deal_count": 50, "avg_value": 5000, "avg_days": 5, "conv_rate": 0.8},
        {"stage_name": "Proposal", "deal_count": 20, "avg_value": 15000, "avg_days": 15, "conv_rate": 0.4},
        {"stage_name": "Negotiation", "deal_count": 5, "avg_value": 45000, "avg_days": 45, "conv_rate": 0.2},
    ]
    
    health_report = calculate_pipeline_health(pipeline)
    print("--- RevOps Pipeline Health Report ---")
    for item in health_report:
        print(f"Stage: {item['stage']} | Score: {item['score']} | Status: {item['status']} | Bottleneck: {item['bottleneck']}")
