from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]

    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrive()
    excepted = 0

    # Assert
    assert starting_value == excepted


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # Act
    excepted = 15
    simple_storage.store(15, {"from": account})

    # Assert
    assert simple_storage.retrive() == excepted
