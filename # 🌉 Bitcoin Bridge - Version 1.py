# 🌉 Bitcoin Bridge - Version 1.0 (MVP)
# Project: CUBO+ Build Sprint 2026

def calculate_change(price_2025, price_2026):
    """Calcula la diferencia porcentual de precios."""
    change = ((price_2026 - price_2025) / price_2025) * 100
    return round(change, 2)

def analyze_product(name, p25, p26):
    diff = calculate_change(p25, p26)
    print(f"--- Analysis for: {name} ---")
    print(f"Price 2025: ${p25} USD")
    print(f"Price 2026: ${p26} USD")
    
    if diff > 0:
        print(f"Result: Price increased by {diff}%")
    elif diff < 0:
        print(f"Result: Price decreased by {abs(diff)}%")
    else:
        print("Result: Price remained stable.")
    print("-" * 30)

# --- Simulation of Data Collection (Nathaly's Role) ---
print("WELCOME TO BITCOIN BRIDGE ANALYTICS\n")

# Example: A pound of coffee and a local service
analyze_product("Local Coffee (1lb)", 5.00, 5.75)
analyze_product("Basic Lunch (Pupusas)", 3.00, 3.50)

print("\nSystem ready for real BTC/USD integration.")