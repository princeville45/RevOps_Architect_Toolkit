def calculate_lead_velocity(current_month_leads, last_month_leads):
    """Calculates the Lead Velocity Index (LVI) to track pipeline growth trajectory."""
    if last_month_leads == 0: return 0
    return round(((current_month_leads - last_month_leads) / last_month_leads) * 100, 2)