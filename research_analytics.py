import pandas as pd
import numpy as np

class ResearchAnalytics:
    """
    Statistical Research Pipeline
    Source: OAU Statistics Project - Chapter 4
    Architect: Irem Victor Chinonso
    """
    def __init__(self, sample_size=265):
        self.sample_size = sample_size

    def calculate_distribution(self, frequencies):
        """Calculates percentages and validates against sample size."""
        total = sum(frequencies.values())
        if total != self.sample_size:
            print(f"Warning: Data total ({total}) does not match sample size ({self.sample_size})")
        
        return {k: round((v / self.sample_size) * 100, 2) for k, v in frequencies.items()}

    def generate_table(self, title, data):
        print(f"\n--- {title} ---")
        dist = self.calculate_distribution(data)
        for category, freq in data.items():
            print(f"{category}: {freq} ({dist[category]}%)")

if __name__ == "__main__":
    pipeline = ResearchAnalytics(265)
    
    # Data from Chapter 4 Doc
    gender_data = {"Male": 119, "Female": 146}
    pipeline.generate_table("Distribution of Respondents by Gender", gender_data)
    
    usage_data = {"Very Often": 106, "Often": 101, "Rarely": 48, "Never": 10}
    pipeline.generate_table("Frequency of Digital Media Usage", usage_data)
