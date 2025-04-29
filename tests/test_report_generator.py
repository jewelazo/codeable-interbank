from report_generator import compute_metrics, load_data

def test_compute_metrics():
    """Test the compute_metrics function."""
    
    df = load_data(file="tests/test_data.csv")
    result = compute_metrics(df)

    assert result['balance_final'] == 325
    assert result['transaccion_max_id'] == 3
    assert result['transaccion_max_amount'] == 200
    assert result['frequency_credit'] == 3
    assert result['frequency_debit'] == 2