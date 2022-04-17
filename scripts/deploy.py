from brownie import FundMe , config ,network, MockV3Aggregator
from scripts.used_functions import ( get_account , LOCAL_BLOCKCHAIN , deploy_mock)

def deploy_fund_me():

    account = get_account()
    if (network.show_active() not in LOCAL_BLOCKCHAIN ):
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address ## The most recent address
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},# whenever changing state we use {"from": account}
        publish_source=config["networks"][network.show_active()].get("verify"), #publish source is for adding the code to the network to be viewed by other
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()