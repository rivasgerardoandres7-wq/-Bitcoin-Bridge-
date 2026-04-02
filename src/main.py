# 🌉 BITCOIN BRIDGE - Prototipo de Análisis de Precios

def analizar_impacto(producto, precio_2025, precio_2026):
    diferencia = precio_2026 - precio_2025
    porcentaje = (diferencia / precio_2025) * 100
    
    print(f"📊 Análisis de Inflación para: {producto}")
    print(f"   Precio 2025: ${precio_2025:,.2f} USD")
    print(f"   Precio 2026: ${precio_2026:,.2f} USD")
    
    if porcentaje > 0:
        print(f"   ⚠️ El precio subió un {round(porcentaje, 2)}%. El poder adquisitivo bajó.")
    elif porcentaje < 0:
        print(f"   🚀 El precio bajó un {round(abs(porcentaje), 2)}%. ¡El Bitcoin Bridge está funcionando!")
    else:
        print("   ✅ El precio se mantiene estable.")
    print("-" * 40)

def simular_ahorro_btc(ventas_mensuales_usd, precio_btc_compra, precio_btc_actual):
    """
    1. Recibe ventas mensuales
    2. Calcula el 10% de ahorro
    3. Convierte el ahorro a BTC usando el precio de compra
    4. Compara el valor actual en USD contra el ahorro original
    5. Muestra los resultados en pantalla
    """
    ahorro_usd = ventas_mensuales_usd * 0.10
    btc_obtenido = ahorro_usd / precio_btc_compra
    valor_actual_usd = btc_obtenido * precio_btc_actual
    ganancia_usd = valor_actual_usd - ahorro_usd
    
    print("📈 SIMULACIÓN DE AHORRO EN BITCOIN (10% de las ventas)")
    print(f"   Ventas mensuales: ${ventas_mensuales_usd:,.2f} USD")
    print(f"   Ahorro destinado (10%): ${ahorro_usd:,.2f} USD")
    print(f"   BTC adquirido a ${precio_btc_compra:,.2f}: {btc_obtenido:.8f} BTC")
    print(f"   Valor actual (con BTC a ${precio_btc_actual:,.2f}): ${valor_actual_usd:,.2f} USD")
    
    if ganancia_usd > 0:
        print(f"   🎉 ¡Ganancia en dólares!: +${ganancia_usd:,.2f} USD")
    elif ganancia_usd < 0:
        print(f"   📉 Pérdida temporal en dólares: ${ganancia_usd:,.2f} USD")
    else:
        print("   ⚖️ Sin ganancia ni pérdida respecto al USD.")
    print("-" * 40)

if __name__ == "__main__":
    print("--- SISTEMA BITCOIN BRIDGE ACTIVADO ---\n")
    
    # 1. Comparativa de precios de Nathaly (Inflación vs Deflación)
    analizar_impacto("Libra de Frijoles", 1.20, 1.50)
    analizar_impacto("Saco de Café", 45.00, 42.00)
    analizar_impacto("Pupusas (3)", 3.00, 3.50)
    
    # 2. Esquema Técnico de Jonathan (Proyección de ahorro en BTC)
    # Ejemplo: ventas de $1500 USD. Compró cuando el BTC estaba en $85,000 USD y hoy llegó a $96,000 USD
    ventas = 1500.00 
    simular_ahorro_btc(
        ventas_mensuales_usd=ventas, 
        precio_btc_compra=85000.00, 
        precio_btc_actual=96000.00
    )