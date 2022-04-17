from brownie import accounts, network , config ,MockV3Aggregator

DECIMALS = 8
STARTING_PRICE = 200000000000       

LOCAL_BLOCKCHAIN = ["ganache-local","development"]
FORKED_BLOCKCHAIN = ["mainnet-fork-dev"]
def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN or network.show_active() in FORKED_BLOCKCHAIN): 
        account = accounts[0]
        return account
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mock():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks Deployed!")