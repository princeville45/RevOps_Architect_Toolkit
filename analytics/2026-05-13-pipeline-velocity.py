def pipeline_velocity(opps, win_rate, avg_deal_size, cycle_length):
    if cycle_length == 0: return 0
    return (opps * win_rate * avg_deal_size) / cycle_length