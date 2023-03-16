from multicall import Call, Multicall

T_TOKEN = '0xcdf7028ceab81fa0c6971208e83fa7872994bee5'
COUNCIL = '0x2ff7ab212cd6feae21bac5300465e149fb6b85a9'
IG = '0x9f6e831c8f8939dc0c830c6e492e7cef4f9c2f5f'


def from_wei(value):
    return value / 1e18

def main():
    call = Call(T_TOKEN, "totalSupply()(uint256)")
    callResult = call()
    print (callResult)

    multi = Multicall(
        [
            Call(
                T_TOKEN, ["balanceOf(address)(uint256)", COUNCIL], [("council", from_wei)]
            ),
            Call(
                T_TOKEN, ["balanceOf(address)(uint256)", IG], [("ig", from_wei)]
            ),
            Call(T_TOKEN, "totalSupply()(uint256)", [("supply", from_wei)]),
        ]
    )

    multicallResult = multi()
    print (multicallResult)

if __name__ == "__main__":
    main()
