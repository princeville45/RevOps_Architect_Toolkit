class DepotIntelligence:
    """
    Wholesale Operations Command Center
    Architect: Irem Victor Chinonso
    Role: Sales and Operations Associate (C-Way Depot)
    """
    def __init__(self, location="Ife, Osun State"):
        self.location = location
        self.inventory = {}
        self.revenue_log = []

    def sync_inventory(self, product, opening, inbound, outbound):
        """Calculates expected closing stock and validates physical count."""
        expected_closing = opening + inbound - outbound
        self.inventory[product] = expected_closing
        return expected_closing

    def track_revenue(self, product, qty_sold, unit_price):
        revenue = qty_sold * unit_price
        self.revenue_log.append({"product": product, "revenue": revenue})
        return revenue

    def get_total_revenue(self):
        return sum(item['revenue'] for item in self.revenue_log)

if __name__ == "__main__":
    depot = DepotIntelligence()
    
    # Example data from Wholesale Ops Dashboard (May 4th)
    expected = depot.sync_inventory("C-Way 50cl", 2890, 0, 10)
    rev = depot.track_revenue("C-Way 50cl", 10, 1600)
    
    print(f"Location: {depot.location}")
    print(f"Expected Closing Stock: {expected}")
    print(f"Daily Revenue: ₦{rev:,.2f}")
