# =============================================================
# brock_analysis.py
# Módulo de análisis comparativo: USD vs Bitcoin
# Autor: Alejandro Castellanos (@BrockaBTC)
#
# La pregunta no es si Bitcoin sube o baja.
# La pregunta es: ¿cuánto poder adquisitivo pierdes
# cada año que no lo tienes?
# =============================================================

from datetime import datetime

# ------------------------------------------------------------------
# BASE DE DATOS DE PRECIOS HISTÓRICOS (BTC/USD)
# Fuente: CoinGecko / CoinMarketCap
# Fechas seleccionadas por relevancia económica y política para SV
# ------------------------------------------------------------------
PRECIOS_BTC = {
    # Antes del halving 2020 - mercado aún desconocido para la región
    "01-01-2019": 3843.52,
    "01-01-2020": 7195.66,
    # Primer halving post-pandemia, inicio del bull market
    "01-05-2020": 8624.15,
    "01-01-2021": 29374.15,
    # Junio 2021: El Salvador anuncia la Ley Bitcoin — punto histórico
    "09-06-2021": 31677.00,
    # Septiembre 2021: Bitcoin se vuelve moneda de curso legal en SV
    "07-09-2021": 46487.87,
    "01-01-2022": 47686.81,
    # Bear market 2022 - lección de volatilidad y convicción
    "01-06-2022": 31792.31,
    "01-11-2022": 20496.00,   # Colapso de FTX - pánico generalizado
    "01-01-2023": 16541.77,
    # Recuperación gradual post-FTX
    "01-06-2023": 27219.73,
    "01-01-2024": 44168.00,
    # Aprobación ETFs spot en EEUU - institucionalización de Bitcoin
    "11-01-2024": 46631.00,
    "01-04-2024": 69700.00,   # Zona del ATH pre-halving 2024
    "20-04-2024": 63800.00,   # Halving 2024
    "01-06-2024": 67734.00,
    "01-01-2025": 94616.00,
    # Contexto actual
    "01-04-2026": 85000.00,
}

# ------------------------------------------------------------------
# CONTEXTO ECONÓMICO SALVADOREÑO
# Datos reales para traducir ganancias a realidad local
# Fuente: DIGESTYC, Ministerio de Economía, BCR 2024-2025
# ------------------------------------------------------------------
ECONOMIA_SV = {
    "canasta_basica_rural":   232.00,   # USD/mes (zona rural)
    "canasta_basica_urbana":  362.00,   # USD/mes (zona urbana)
    "salario_minimo_comercio": 365.00,  # USD/mes (sector comercio)
    "galon_gasolina":           4.20,   # USD aprox. 2025
    "tarifa_agua_mensual":      8.50,   # USD promedio ANDA
    "matricula_universitaria": 45.00,   # USD/ciclo promedio UFG
    "remesa_promedio_mensual": 320.00,  # USD promedio recibido por familia
}

PRECIO_HOY = 85000.00  # USD - precio referencia abril 2026


# ------------------------------------------------------------------
# FUNCIONES PRINCIPALES
# ------------------------------------------------------------------

def obtener_precio(fecha: str) -> float:
    """
    Busca el precio histórico de BTC para una fecha.
    Si no está en la base de datos, sugiere las más cercanas.
    """
    if fecha in PRECIOS_BTC:
        return PRECIOS_BTC[fecha]

    # Si no existe, mostrar fechas disponibles ordenadas
    fechas_ordenadas = sorted(
        PRECIOS_BTC.keys(),
        key=lambda f: datetime.strptime(f, "%d-%m-%Y")
    )
    raise ValueError(
        f"\n  ⚠️  Fecha '{fecha}' no está en la base de datos.\n"
        f"  Fechas disponibles:\n"
        + "\n".join(f"    → {f}  (${PRECIOS_BTC[f]:,.2f})" for f in fechas_ordenadas)
    )


def calcular_escenario(monto: float, fecha: str) -> dict:
    """
    Calcula qué hubiera pasado con un monto en USD
    si se hubiera convertido a BTC en una fecha dada.
    """
    precio_entonces = obtener_precio(fecha)
    btc = monto / precio_entonces
    valor_hoy = btc * PRECIO_HOY
    ganancia = valor_hoy - monto
    rendimiento = (ganancia / monto) * 100

    return {
        "fecha": fecha,
        "monto_usd": monto,
        "precio_entonces": precio_entonces,
        "precio_hoy": PRECIO_HOY,
        "btc_adquirido": btc,
        "valor_hoy": valor_hoy,
        "ganancia": ganancia,
        "rendimiento": rendimiento,
    }


def traducir_a_sv(monto: float) -> dict:
    """
    Traduce un monto en USD a equivalentes económicos
    del contexto salvadoreño. Porque los números abstractos
    no comunican lo mismo que 'X meses de salario'.
    """
    return {
        "canastas_rurales":   round(monto / ECONOMIA_SV["canasta_basica_rural"], 1),
        "canastas_urbanas":   round(monto / ECONOMIA_SV["canasta_basica_urbana"], 1),
        "salarios_minimos":   round(monto / ECONOMIA_SV["salario_minimo_comercio"], 1),
        "galones_gasolina":   round(monto / ECONOMIA_SV["galon_gasolina"], 0),
        "meses_agua":         round(monto / ECONOMIA_SV["tarifa_agua_mensual"], 1),
        "matriculas_univ":    round(monto / ECONOMIA_SV["matricula_universitaria"], 1),
        "remesas_equiv":      round(monto / ECONOMIA_SV["remesa_promedio_mensual"], 1),
    }


def analisis_multifecha(monto: float) -> list:
    """
    Genera tabla comparativa para un mismo monto
    en todas las fechas de la base de datos.
    Útil para visualizar patrones y tendencias.
    """
    resultados = []
    for fecha in sorted(PRECIOS_BTC.keys(),
                        key=lambda f: datetime.strptime(f, "%d-%m-%Y")):
        r = calcular_escenario(monto, fecha)
        resultados.append(r)
    return resultados


# ------------------------------------------------------------------
# FUNCIONES DE VISUALIZACIÓN
# ------------------------------------------------------------------

def imprimir_escenario(r: dict):
    """Imprime resultado de un escenario individual."""
    signo = "✅" if r["ganancia"] >= 0 else "❌"
    print(f"\n{'='*54}")
    print(f"  🟠 BITCOIN BRIDGE — Análisis Individual")
    print(f"{'='*54}")
    print(f"  💵 Monto invertido:       ${r['monto_usd']:>12,.2f} USD")
    print(f"  📅 Fecha de compra:       {r['fecha']:>15}")
    print(f"  📉 Precio BTC entonces:   ${r['precio_entonces']:>12,.2f}")
    print(f"  📈 Precio BTC hoy:        ${r['precio_hoy']:>12,.2f}")
    print(f"  ₿  BTC adquirido:         {r['btc_adquirido']:>18.8f}")
    print(f"  💰 Valor actual:          ${r['valor_hoy']:>12,.2f} USD")
    print(f"  {signo} {'Ganancia' if r['ganancia']>=0 else 'Pérdida'}:"
          f"              ${r['ganancia']:>12,.2f} USD")
    print(f"  🚀 Rendimiento:           {r['rendimiento']:>13.2f}%")
    print(f"{'='*54}")


def imprimir_contexto_sv(ganancia: float):
    """Traduce la ganancia al contexto económico de El Salvador."""
    if ganancia <= 0:
        print("\n  📊 Sin ganancia que traducir en este escenario.")
        return

    sv = traducir_a_sv(ganancia)
    print(f"\n{'='*54}")
    print(f"  🇸🇻 ¿Qué representa esa ganancia en El Salvador?")
    print(f"{'='*54}")
    print(f"  🛒 Canastas básicas rurales:   {sv['canastas_rurales']:>8} meses")
    print(f"  🏙️  Canastas básicas urbanas:   {sv['canastas_urbanas']:>8} meses")
    print(f"  💼 Salarios mínimos (comercio):{sv['salarios_minimos']:>8} meses")
    print(f"  ⛽ Galones de gasolina:        {sv['galones_gasolina']:>8.0f} galones")
    print(f"  💧 Meses de servicio de agua:  {sv['meses_agua']:>8} meses")
    print(f"  🎓 Matrículas universitarias:  {sv['matriculas_univ']:>8} ciclos")
    print(f"  📦 Remesas familiares equiv.:  {sv['remesas_equiv']:>8} meses")
    print(f"{'='*54}")


def imprimir_tabla_multifecha(resultados: list):
    """Imprime tabla comparativa de todos los escenarios."""
    print(f"\n{'='*70}")
    print(f"  📊 TABLA COMPARATIVA — Mismo monto, distintas fechas de entrada")
    print(f"{'='*70}")
    print(f"  {'Fecha':<14} {'Precio BTC':<14} {'Valor Hoy':>12} {'Ganancia':>12} {'Rend.':>8}")
    print(f"  {'-'*62}")

    for r in resultados:
        signo = "▲" if r["rendimiento"] >= 0 else "▼"
        print(
            f"  {r['fecha']:<14}"
            f"  ${r['precio_entonces']:>10,.0f}"
            f"  ${r['valor_hoy']:>10,.2f}"
            f"  ${r['ganancia']:>10,.2f}"
            f"  {signo}{abs(r['rendimiento']):>6.0f}%"
        )
    print(f"{'='*70}")
    print(f"  * Monto base: ${resultados[0]['monto_usd']:,.2f} USD | "
          f"Precio BTC hoy: ${PRECIO_HOY:,.2f}")


# ------------------------------------------------------------------
# MENÚ PRINCIPAL
# ------------------------------------------------------------------

def menu():
    print("\n" + "🟠 "*18)
    print("  BITCOIN BRIDGE — Calculadora de Ventaja Comparativa")
    print("  ¿Cuánto poder adquisitivo has perdido sin Bitcoin?")
    print("🟠 "*18)
    print("\n  [1] Analizar una fecha específica")
    print("  [2] Ver tabla comparativa (todas las fechas)")
    print("  [3] Salir")
    return input("\n  Elige una opción: ").strip()


def main():
    while True:
        opcion = menu()

        if opcion == "1":
            try:
                monto = float(input("\n  ¿Cuántos USD hubieras invertido? $"))
                print("\n  Fechas disponibles: escribe exactamente como aparece")
                print("  Ejemplo: 07-09-2021 (día que Bitcoin fue ley en El Salvador)")
                fecha = input("  ¿En qué fecha? (DD-MM-YYYY): ").strip()

                r = calcular_escenario(monto, fecha)
                imprimir_escenario(r)
                imprimir_contexto_sv(r["ganancia"])

            except ValueError as e:
                print(e)

        elif opcion == "2":
            try:
                monto = float(input("\n  ¿Con cuántos USD quieres comparar? $"))
                resultados = analisis_multifecha(monto)
                imprimir_tabla_multifecha(resultados)

            except ValueError as e:
                print(e)

        elif opcion == "3":
            print("\n  Stay humble, stack sats. 🟠\n")
            break

        else:
            print("\n  Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()