"""
HW02 — Airport Luggage Tags (Open Addressing with Delete)
Implement linear probing with EMPTY and DELETED markers.
"""

# TODO Step 4: create unique marker objects
# Example:
# EMPTY = object()
# DELETED = object()

def make_table_open(m):
    """Return a table of length m filled with EMPTY markers."""
    # TODO Steps 4–6
    raise NotImplementedError

def _find_slot_for_insert(t, key):
    """Return index to insert/overwrite (may return DELETED slot). Return None if full."""
    # TODO Steps 4–6: probe with wrap; remember first DELETED
    raise NotImplementedError

def _find_slot_for_search(t, key):
    """Return index where key is found; else None. DELETED does not stop search."""
    # TODO Steps 4–6
    raise NotImplementedError

def put_open(t, key, value):
    """Insert or overwrite (key, value). Return True on success, False if table is full."""
    # TODO Steps 5–6: use _find_slot_for_insert; handle overwrite
    raise NotImplementedError

def get_open(t, key):
    """Return value for key or None if not present."""
    # TODO Steps 5–6: use _find_slot_for_search
    raise NotImplementedError

def delete_open(t, key):
    """Delete key if present. Return True if removed, else False."""
    # TODO Steps 5–6: mark slot as DELETED
    raise NotImplementedError

if __name__ == "__main__":
    # Optional manual checks (not graded)
    pass
