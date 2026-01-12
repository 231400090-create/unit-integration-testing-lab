import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest, check_loan_eligibility

# ---------- deposit (White Box) ----------
def test_deposit_error_branch():
    with pytest.raises(ValueError):
        deposit(1000, 0)

def test_deposit_success_path():
    assert deposit(500, 200) == 700

# ---------- withdraw (White Box) ----------
def test_withdraw_negative_amount():
    with pytest.raises(ValueError):
        withdraw(1000, -10)

def test_withdraw_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(500, 700)

def test_withdraw_success_path():
    assert withdraw(1000, 400) == 600

# ---------- transfer (White Box) ----------
def test_transfer_negative_amount():
    with pytest.raises(ValueError):
        transfer(1000, 500, -50)

def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(200, 300, 400)

def test_transfer_success_path():
    assert transfer(1000, 500, 300) == (700, 800)

# ---------- calculate_interest (White Box) ----------
def test_interest_negative_balance():
    with pytest.raises(ValueError):
        calculate_interest(-1000, 5, 2)

def test_interest_negative_rate():
    with pytest.raises(ValueError):
        calculate_interest(1000, -5, 2)

def test_interest_valid_path():
  assert round(calculate_interest(1000, 10, 2), 2) == 1210


# ---------- check_loan_eligibility (White Box) ----------
def test_loan_condition_true():
    assert check_loan_eligibility(7000, 800) is True

def test_loan_condition_false():
    assert check_loan_eligibility(4000, 600) is False