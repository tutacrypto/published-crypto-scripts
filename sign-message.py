from web3 import Web3
from eth_account.messages import encode_defunct

web3 = Web3()
web3.eth.account.enable_unaudited_hdwallet_features()

my_mnemonic = ""
account = web3.eth.account.from_mnemonic(my_mnemonic, account_path="m/44'/60'/0'/0/0")

message = encode_defunct(text="wagmi anon")
signed_message = web3.eth.account.sign_message(message, private_key=account.key)

print(web3.eth.account.recover_message(message, signature=signed_message.signature))