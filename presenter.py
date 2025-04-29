def print_exit(**kwargs):
    print (f"""
    Reporte de Transacciones
    ---------------------------------------------
    Balance Final: {kwargs.get("balance_final")}
    Transacción de Mayor Monto: ID {kwargs.get("transaccion_max_id")} - {kwargs.get("transaccion_max_amount")}
    Conteo de Transacciones: Crédito: {kwargs.get("frequency_credit")} Débito: {kwargs.get("frequency_debit")}
    """)

