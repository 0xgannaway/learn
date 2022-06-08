from brownie import Lottery, accounts, config, network
from web3 import Web3


def test_lottery():
    account = accounts[0]
    price_feed_address = config["networks"][network.show_activate()]["eth_usd_price_feed"]
    lottery = Lottery.deploy(
        price_feed_address,
        {"from": account},
    )
    assert lottery.getEntranceFee() > Web3.toWei(0.018, "ether")
    assert lottery.getEntranceFee() < Web3.toWei(0.022, "ether")


def main():
    test_lottery()
