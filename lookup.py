def lookup(obj, path):
    """
    Looks up a value in a nested dict using a dot-separated path.
    Returns None if the path is invalid. Empty path returns obj.
    """
    if path == "":
        return obj
    keys = path.split(".")
    current = obj
    for key in keys:
        if not isinstance(current, dict):
            return None
        if key not in current:
            return None
        current = current[key]
    return current 