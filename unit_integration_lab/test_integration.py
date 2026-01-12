
import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest, check_loan_eligibility

# ---------- deposit (Black Box) ----------
def test_deposit_success():
    assert deposit(1000, 500) == 1500

def test_deposit_invalid():
    with pytest.raises(ValueError):
        deposit(1000, -100)

# ---------- withdraw (Black Box) ----------
def test_withdraw_success():
    assert withdraw(1000, 300) == 700

def test_withdraw_failure():
    with pytest.raises(ValueError):
        withdraw(500, 800)

# ---------- transfer (Black Box) ----------
def test_transfer_success():
    from_acc, to_acc = transfer(1000, 500, 200)
    assert from_acc == 800
    assert to_acc == 700

def test_transfer_failure():
    with pytest.raises(ValueError):
        transfer(200, 500, 300)

# ---------- calculate_interest (Black Box) ----------
def test_calculate_interest():
    assert calculate_interest(1000, 10, 1) == 1100

# ---------- check_loan_eligibility (Black Box) ----------
def test_loan_eligible():
    assert check_loan_eligibility(6000, 750) is True

def test_loan_not_eligible():
    assert check_loan_eligibility(3000, 650) is False
