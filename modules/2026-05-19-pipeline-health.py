def calculate_pipeline_health_score(weighted_pipeline, quota):
    """Calculates the pipeline coverage health score (Ideal: 3x quota)."""
    coverage = weighted_pipeline / quota
    score = min(100, (coverage / 3.0) * 100)
    return round(score, 2)