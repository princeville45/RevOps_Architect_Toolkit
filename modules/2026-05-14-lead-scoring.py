def score_lead(firmographics):
    """Scores a lead based on company size, industry, and annual revenue."""
    score = 0
    # Size weights
    size = firmographics.get('size', 0)
    if size > 1000: score += 40
    elif size > 100: score += 20
    
    # Industry weights
    industry = firmographics.get('industry', '').lower()
    if industry in ['fintech', 'saas', 'logistics']: score += 30
    
    return score