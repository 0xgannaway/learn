from brownie import accounts, network, config
from brownie import Mora
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "development",
    "ganache",
    "local-ganache",
    "mainnet-fork",
]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print(accounts[0].balance())
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])


initial_supply = Web3.toWei(1000, "ether")


def main():
    account = get_account()
    mora = Mora.deploy(initial_supply, {"from": account}, publish_source=True)
    print(mora.name())
