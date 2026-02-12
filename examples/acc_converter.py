# acc_converter.py - Rough example (not production-ready)
def acc_from_gregorian(year, uncertainty_note=""):
    """
    Very approximate: Assumes base 13.797 Gyr + mnemonic offset.
    Real use needs days-since-ref + proper rounding.
    """
    base_gyr = 13.797
    days_in_year = 365.2425
    offset_for_2026 = 312026 - int(base_gyr * 1e9)  # Rough mnemonic calc
    acc_head = int(base_gyr * 1e9)
    acc_tail = offset_for_2026 + int((year - 2026) * days_in_year)
    return f"{acc_head + acc_tail} ACC ±0 (label)", uncertainty_note

print(acc_from_gregorian(2026))  # Example output
