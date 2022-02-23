from brownie import accounts, config, SimpleStorage, network


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def simple_storage_deploy():
    account = get_account()
    # account = accounts.load("freecode-brownie")
    # account = accounts.add(config["wallets"]["from_key"])
    print(account)

    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrive()
    print(stored_value)

    txn = simple_storage.store(143, {"from": account})
    txn.wait(1)

    updated_value = simple_storage.retrive()
    print(updated_value)


def main():
    print("Scripts deploy start")
    simple_storage_deploy()
