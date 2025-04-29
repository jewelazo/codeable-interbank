import pandas as pd
from presenter import print_exit

def load_data(file: str) -> pd.DataFrame:
    """Load CSV data into a dataFrame."""
    return pd.read_csv(file)

def compute_metrics(df: pd.DataFrame):
    """Compute metrics from the dataFrame."""
    total_credit = df[df['tipo'] == 'Crédito']['monto'].sum()
    total_debit = df[df['tipo'] == 'Débito']['monto'].sum()
    balance_final = round(total_credit - total_debit,2)
    transaccion_max = df.loc[df['monto'].idxmax()]
    transaccion_max_amount = transaccion_max["monto"]
    transaccion_max_id = transaccion_max["id"]
    frequencies = df['tipo'].value_counts()
    frequency_credit = frequencies["Crédito"]
    frequency_debit = frequencies["Débito"]

    return {
        'balance_final': balance_final,
        'transaccion_max_id': transaccion_max_id,
        'transaccion_max_amount': transaccion_max_amount,
        'frequency_credit': frequency_credit,
        'frequency_debit': frequency_debit
    }
    
def main():
    """Main function to load data and compute metrics."""
    df = load_data(file="data.csv")
    print_exit(**compute_metrics(df))

if __name__ == "__main__":
    main()
