// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract SimpleStorage {
    uint256 storageDisplayNumber;

    struct People {
        string name;
        uint256 favNumber;
    }

    People[] public people;
    mapping(string => uint256) public favNumberMap;

    function store(uint256 _displayNumber) public {
        storageDisplayNumber = _displayNumber;
    }

    function retrive() public view returns (uint256) {
        return storageDisplayNumber;
    }

    function addPerson(string memory _name, uint256 _favNumber) public {
        people.push(People(_name, _favNumber));
        favNumberMap[_name] = _favNumber;
    }
}
