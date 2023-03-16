from multicall import Call, Multicall

T_TOKEN = "0xcdf7028ceab81fa0c6971208e83fa7872994bee5"
COUNCIL = "0x2ff7ab212cd6feae21bac5300465e149fb6b85a9"
IG = "0x9f6e831c8f8939dc0c830c6e492e7cef4f9c2f5f"
ENS_CONTRACT = "0x57f1887a8BF19b14fC0dF6Fd9B2acc9Af147eA85"
BORED_CONTRACT = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
ENS_TOKEN_ID = 7429818021171951900947901187182840629009317564384920882234443277502829601145
BORED_TOKEN_ID = 2260


def from_wei(value):
    return value / 1e18


def main():
    # Make a single call
    call1 = Call(T_TOKEN, "totalSupply()(uint256)")
    call1Result = call1()
    print(call1Result)

    # Make a multicall to the same contract: Threshold Token
    multi1 = Multicall(
        [
            Call(
                T_TOKEN,
                ["balanceOf(address)(uint256)", COUNCIL],
                [("council", from_wei)],
            ),
            Call(T_TOKEN, ["balanceOf(address)(uint256)", IG], [("ig", from_wei)]),
            Call(T_TOKEN, "totalSupply()(uint256)", [("supply", from_wei)]),
        ]
    )

    multi1Result = multi1()
    print(multi1Result)

    # Make a multicall to several contracts
    multi2 = Multicall(
        [
            # Call to Ethereum Name Service contract (ERC721)
            Call(
                ENS_CONTRACT,
                ["ownerOf(uint256)(address)", ENS_TOKEN_ID],
                [("ensOwner", None)],
            ),
            # Call to Bored Ape Yacht Club contract (ERC721)
            Call(
                BORED_CONTRACT,
                ["ownerOf(uint256)(address)", BORED_TOKEN_ID],
                [("boredOwner", None)]
            ),
            # Call to Threshold Token contract (ERC20)
            Call(
                T_TOKEN,
                ["balanceOf(address)(uint256)", COUNCIL],
                [("councilBalance", from_wei)],
            ),
        ]
    )
    multi2Result = multi2()
    print(multi2Result)


if __name__ == "__main__":
    main()
