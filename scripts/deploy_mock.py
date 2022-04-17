from brownie import (
    MockV3Aggregator,
    network,
)

from scripts.used_functions import (
    get_account,
)

DECIMALS = 8
# This is 2,000
INITIAL_VALUE = 200000000000

def deploy_mocks():
   
    print(f"Network used {network.show_active()}")
    print("Deploying Mocks...")
    account = get_account()
    print(account)
    MockV3Aggregator.deploy(DECIMALS, INITIAL_VALUE, {"from": account})
    print("Mocks Deployed!")


def main():
    deploy_mocks()