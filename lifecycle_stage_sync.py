def sync_lifecycle_stage(deal_stage, current_lifecycle):
    """
    Syncs HubSpot Lifecycle Stage based on Deal Stage movement.
    Logic:
    - 'Contract Sent' -> 'SQL'
    - 'Closed Won' -> 'Customer'
    - 'Closed Lost' -> 'Other'
    """
    mapping = {
        'contract_sent': 'sql',
        'closed_won': 'customer',
        'closed_lost': 'other'
    }
    return mapping.get(deal_stage, current_lifecycle)

if __name__ == "__main__":
    print(f"Synced Stage: {sync_lifecycle_stage('closed_won', 'lead')}")
