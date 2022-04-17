// SPDX-License-Identifier: MIT


pragma solidity ^0.6.6;


import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

contract FundMe{

    using SafeMathChainlink for uint256;
    mapping(address => uint256) public addresses_with_money;


    address public owner;

    address[] public funders;

    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) public {
        priceFeed = AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
    } 

    modifier onlyOwner()
    {
        require(msg.sender == owner);
        _;
    }

    function fund() public payable{
        uint256 minUSD = 50 * 10 ** 8;
        require(getConverion(msg.value) >= minUSD, " You Do not have enough amount of eth");
        addresses_with_money[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function withDraw() payable onlyOwner public{
        payable(msg.sender).transfer(address(this).balance);
        for(uint256 i = 0; i < funders.length; i++)
        {
            address funder = funders[i];
            addresses_with_money[funder] = 0;
        }
        funders = new address[](0);
    }

    /**
     * Network: Kovan
     * Aggregator: ETH/USD
     * Address: 0x9326BFA02ADD2366b30bacB125260Af641031331
     */
     function getPrice() public view returns (uint256) {
        (, int256 answer, , , ) = priceFeed.latestRoundData();
        return uint256(answer * 10000000000);
    }


    function getConverion(uint256 ethAmount) public view returns (uint256){
        uint256 price = getPrice();
        uint256 ethAmountInUSD = (price * ethAmount) * 1000000000000000000;
        return ethAmount;
    }

     function getEntranceFee() public view returns (uint256) {
        uint256 minimumUSD = 50 * 10**18;
        uint256 price = getPrice();
        uint256 precision = 1 * 10**18;
        return ((minimumUSD * precision) / price) + 1;
    }

}