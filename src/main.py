# 🌉 BITCOIN BRIDGE - Prototipo de Análisis de Precios
# Este código calcula la inflación o deflación entre 2025 y 2026

def analizar_impacto(producto, precio_2025, precio_2026):
    diferencia = precio_2026 - precio_2025
    porcentaje = (diferencia / precio_2025) * 100
    
    print(f"📊 Análisis para: {producto}")
    print(f"   Precio 2025: ${precio_2025} USD")
    print(f"   Precio 2026: ${precio_2026} USD")
    
    if porcentaje > 0:
        print(f"   ⚠️ El precio subió un {round(porcentaje, 2)}%. El poder adquisitivo bajó.")
    elif porcentaje < 0:
        print(f"   🚀 El precio bajó un {round(abs(porcentaje), 2)}%. ¡El Bitcoin Bridge está funcionando!")
    else:
        print("   ✅ El precio se mantiene estable.")
    print("-" * 40)

# --- SIMULACIÓN DE DATOS ---
print("--- SISTEMA BITCOIN BRIDGE ACTIVADO ---\n")

analizar_impacto("Libra de Frijoles", 1.20, 1.50)
analizar_impacto("Saco de Café", 45.00, 42.00)