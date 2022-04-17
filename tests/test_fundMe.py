from scripts.used_functions import get_account, LOCAL_BLOCKCHAIN
from scripts.deploy import deploy_fund_me

def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addresses_with_money(account.address) == entrance_fee
    tx2 = fund_me.withDraw({"from": account})
    tx2.wait(1)
    assert fund_me.addresses_with_money(account.address) == 0