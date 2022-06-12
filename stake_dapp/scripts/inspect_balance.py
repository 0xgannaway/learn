from scripts.helpful_scripts import get_contract
from brownie import DappToken, Contract

def main():
    contract_address = "0x80D026fd3C908134e6B37912DbaAb412889b6d33"
    contract_type = DappToken
    contract = Contract.from_abi(
        contract_type._name, contract_address, contract_type.abi
    )
    dapp_token = contract
    print("balance", dapp_token.balanceOf("0xC778555B0808881599CDbE7D8fBD2aaC4986Cc7a"))
