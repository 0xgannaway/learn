# learn

```shell
pip install py-solc-x web3 pipx
python3 -m pipx ensurepath
pipx install eth-brownie
brownie --version
brownie init
brownie compile
brownie run scripts/deploy.py # 部署
brownie run scripts/deploy.py --network rinkeby # 部署
brownie accounts new <name>
brownie accounts list
brownie accounts delete <name>
brownie test
brownie test -s
brownie test -k test_deploy
brownie test --pdb
brownie networks list
brownie console
brownie networks add Ethereum ganache-local host=http://0.0.0.0:8545 chainid=1337
brownie networks delete mainnet-fork
brownie bake chainlink-mix # 项目模板
```

```
from brownie import accounts

account = accounts.load("<name>")
```