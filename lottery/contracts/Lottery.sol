pragma solidity ^0.6.6;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract Lottery {
    address payable[] public players;
    uint256 public usdEntryFee;
    AggregatorV3Interface internal ethUsdPriceFeed;

    constructor(address _priceFeedAddress) public {
        usdEntryFee = 50;
        ethUsdPriceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    /**
     */
    function enter() public payable {
        players.push(msg.sender);
    }

    function genEntranceFee() public view returns (uint256) {
        uint256 minimumUSD = 50 * 10**18;
        uint256 price = getPrice();
        uint256 precision = 1 * 10**18;
        uint256 costToEnter = (price);
        return costToEnter;
    }

    function getPrice() public view returns (uint256) {
        (, int256 answer, , , ) = ethUsdPriceFeed.latestRoundData();
        return uint256(answer * 10000000000);
    }
    function startLottery() public {}

    function endLottery() public {}
}
