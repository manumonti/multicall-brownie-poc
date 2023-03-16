# Multicall PoC

This repo is a PoC about how to implement and use MakerDAO multicall contract.

## Get started

This project uses [Brownie](https://github.com/eth-brownie/brownie) development environment. To build and deploy the contracts:

### Prerequisites

- ganache-cli
- python3.7 or greater
- pipx
- eth-brownie

### Installation

You have to install [multicall.py](https://github.com/banteg/multicall.py) package. If you installed eth-brownie with pipx:

```
pipx inject eth-brownie multicall
```

Export the INFURA API key:

```
export WEB3_INFURA_PROJECT_ID='aaaa1111bbbb2222cccc3333dddd4444'
```

### Run script

```
brownie run scripts/multicall.py --network mainnet
```
