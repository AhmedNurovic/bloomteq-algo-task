def generate_new_entry(entries):
    """
    Takes a list of dicts with 'id' and 'value'.
    Returns a new dict {'id': X, 'value': Y} as per the rules:
      - X: max existing id + 1 (or 1 if empty)
      - Y: smallest positive int not in values, and there is at least one smaller int (than Y) that appears >=2 times in values
    If no such Y exists (no duplicate), returns None.
    """
    if not entries:
        return None

    existing_ids = [entry['id'] for entry in entries]
    existing_values = [entry['value'] for entry in entries]

    new_id = max(existing_ids) + 1 if existing_ids else 1

    # Count occurrences of each value
    from collections import Counter
    value_counts = Counter(existing_values)
    duplicates = [val for val, count in value_counts.items() if count >= 2]
    if not duplicates:
        return None
    min_duplicate = min(duplicates)

    max_value = max(existing_values) if existing_values else 0
    # Candidate values: 1 to max_value+1
    for candidate in range(1, max_value + 2):
        if candidate in value_counts:
            continue
        if min_duplicate < candidate:
            return {'id': new_id, 'value': candidate}
    return None 