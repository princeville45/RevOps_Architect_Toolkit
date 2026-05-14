def identify_duplicates(records):
    """
    Identifies duplicate CRM records using a combination of Email and Company Name.
    Financial Pivot Law: Prevents double-counting revenue projections.
    """
    seen = set()
    duplicates = []
    for record in records:
        identifier = f"{record['email']}_{record['company_name'].lower()}"
        if identifier in seen:
            duplicates.append(record)
        else:
            seen.add(identifier)
    return duplicates
