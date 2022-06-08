部署第一版

```shell
(base) ➜  upgrades git:(main) ✗ GITHUB_TOKEN=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 brownie run scripts/01_deploy_box.py --network rinkeby
Brownie v1.19.0 - Python development framework for Ethereum

UpgradesProject is the active project.

Running 'scripts/01_deploy_box.py::main'...
Deploying to rinkeby
Transaction sent: 0x3809a3cca627c11ebfec8adddf8d7fcb92c3917e99d3c729354a9e5990bc3989
  Gas price: 1.071567174 gwei   Gas limit: 113404   Nonce: 16
  Box.constructor confirmed   Block: 10817173   Gas used: 103095 (90.91%)
  Box deployed at: 0xAF5D916CD4ceb839B14D0E9Bd781B3403A66D85b

/home/lxy/.local/pipx/venvs/eth-brownie/lib/python3.8/site-packages/brownie/network/contract.py:1198: BrownieCompilerWarning: 0xAF5D916CD4ceb839B14D0E9Bd781B3403A66D85b: Locally compiled and on-chain bytecode do not match!
  warnings.warn(
Transaction sent: 0x82e67c31a70d2096a208164c1e6b68272f3c8527a5ad3f1513b37cec42d85cbb
  Gas price: 1.071435875 gwei   Gas limit: 534673   Nonce: 17
  ProxyAdmin.constructor confirmed   Block: 10817174   Gas used: 486067 (90.91%)
  ProxyAdmin deployed at: 0xdb1aB44516B16727E3599509b42B9776204d95E5

Transaction sent: 0x0911a92a9a386ac77e20d2ee58acddf04fac380825c1853622043d2052b2dcb8
  Gas price: 1.071536386 gwei   Gas limit: 1000000   Nonce: 18
  TransparentUpgradeableProxy.constructor confirmed   Block: 10817175   Gas used: 574574 (57.46%)
  TransparentUpgradeableProxy deployed at: 0xAa4eBD030a4B9A1dbE81F32b34b167e29a5B2aB3

Fetching source of 0xAF5D916CD4ceb839B14D0E9Bd781B3403A66D85b from api-rinkeby.etherscan.io...
Proxy deployed to 0xAa4eBD030a4B9A1dbE81F32b34b167e29a5B2aB3 ! You can now upgrade it to BoxV2!
Here is the initial value in the Box: 0
```

升级

```shell
(base) ➜  upgrades git:(main) ✗ GITHUB_TOKEN=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 brownie run scripts/02_upgrade_box.py --network rinkeby
Brownie v1.19.0 - Python development framework for Ethereum

UpgradesProject is the active project.

Running 'scripts/02_upgrade_box.py::main'...
Deploying to rinkeby
Transaction sent: 0x908ff8ba498ebc8d545a1986c25cbe6648b8cad41a0e5e8d9f7edd407e0a6ce6
  Gas price: 1.071913368 gwei   Gas limit: 146012   Nonce: 19
  BoxV2.constructor confirmed   Block: 10817182   Gas used: 132739 (90.91%)
  BoxV2 deployed at: 0x17CaB44234Dae1ABdA4daeFB6f3938b4E5c0232f

/home/lxy/.local/pipx/venvs/eth-brownie/lib/python3.8/site-packages/brownie/network/contract.py:1198: BrownieCompilerWarning: 0x17CaB44234Dae1ABdA4daeFB6f3938b4E5c0232f: Locally compiled and on-chain bytecode do not match!
  warnings.warn(
Transaction sent: 0xa481c8f9609d19bd28f6123a61c11fc2577b815fbca3cffd5d5bcf3779c611ac
  Gas price: 1.071989878 gwei   Gas limit: 42764   Nonce: 20
  ProxyAdmin.upgrade confirmed   Block: 10817183   Gas used: 38739 (90.59%)

Proxy has been upgraded!
Starting value 0
Transaction sent: 0xcc7009f2d8cbf5513ab8c12c76834bfdb93e48da5e7087299bc5924a95fd2f5f
  Gas price: 1.071753945 gwei   Gas limit: 57303   Nonce: 21
  Transaction confirmed   Block: 10817184   Gas used: 51761 (90.33%)

Ending value 1
```

- [Upgrades Mix](#upgrades-mix)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Useage](#useage)
  - [Scripts](#scripts)
  - [Test](#test)
  - [Linting](#linting)
  - [Resources](#resources)
  - [License](#license)

This repo shows users how to use the Transparent Proxy pattern for upgrading smart contracts. It uses most of the code from openzeppelin's repo, and adds brownie scripts on top.

## Prerequisites

Please install or have installed the following:

- [nodejs and npm](https://nodejs.org/en/download/)
- [python](https://www.python.org/downloads/)
## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already. Here is a simple way to install brownie.

```bash
pip install eth-brownie
```
Or, if that doesn't work, via pipx
```bash
pip install --user pipx
pipx ensurepath
# restart your terminal
pipx install eth-brownie
```

2. For local testing [install ganache-cli](https://www.npmjs.com/package/ganache-cli)
*Skip if you only want to use testnets*

```bash
npm install -g ganache-cli
```
or
```bash
yarn add global ganache-cli
```

3. Download the mix and install dependancies.

```bash
brownie bake upgrades-mix
cd upgrades
```

Or, you can clone from source:

```bash
git clone https://github.com/PatrickAlphaC/upgrades-mix
cd upgrades-mix
```

## Environment Variables
If you want to be able to deploy to testnets or work with mainnet-fork, do the following.

1. Set your `WEB3_INFURA_PROJECT_ID`, and `PRIVATE_KEY` [environment variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html).

You can get a `WEB3_INFURA_PROJECT_ID` by getting a free trial of [Infura](https://infura.io/). At the moment, it does need to be infura with brownie. If you get lost, you can [follow this guide](https://ethereumico.io/knowledge-base/infura-api-key-guide/) to getting a project key. You can find your `PRIVATE_KEY` from your ethereum wallet like [metamask](https://metamask.io/).

You'll also need testnet rinkeby ETH and LINK. You can get LINK and ETH into your wallet by using the [rinkeby faucets located here](https://docs.chain.link/docs/link-token-contracts#rinkeby). If you're new to this, [watch this video.](https://www.youtube.com/watch?v=P7FX_1PePX0)

You can add your environment variables to the `.env` file:

```
export WEB3_INFURA_PROJECT_ID=<PROJECT_ID>
export PRIVATE_KEY=<PRIVATE_KEY>
```

AND THEN RUN `source .env` TO ACTIVATE THE ENV VARIABLES
(You'll need to do this everytime you open a new terminal, or [learn how to set them easier](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html)).

> DO NOT SEND YOUR PRIVATE KEY WITH FUNDS IN IT ONTO GITHUB

Otherwise, you can build, test, and deploy on your local environment.

# Useage
## Scripts

```
brownie run scripts/01_deploy_box.py
brownie run scripts/02_upgrade_box.py
```
This will:
1. Deploy a `Box` implementation contract
2. Deploy a `ProxyAdmin` contract to be the admin of the proxy
3. Deploy a `TransparentUpgradeableProxy` to be the proxy for the implementations

Then, the upgrade script will:

4. Deploy a new Box implementation `BoxV2`
5. Upgrade the proxy to point to the new implementation contract, essentially upgrading your infrastructure.
6. Then it will call a function only `BoxV2` can call

## Test

```
brownie test
```

## Linting

```
pip install black
pip install autoflake
autoflake --in-place --remove-unused-variables -r .
black .
```
## Resources
To get started with Brownie:

* Check out the other [Brownie mixes](https://github.com/brownie-mix/) that can be used as a starting point for your own contracts. They also provide example code to help you get started.
* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) is a good tutorial to help you familiarize yourself with Brownie.
* For more in-depth information, read the [Brownie documentation](https://eth-brownie.readthedocs.io/en/stable/).
* Or watch any of the [Brownie YouTube](https://www.youtube.com/watch?v=QfFO22lwSw4&t=2s) tutorials or [articles](https://alphachain.io/blogs/)

Any questions? Join our [Discord](https://discord.gg/9zk7snTfWe)
## License

This project is licensed under the [MIT license](LICENSE).


