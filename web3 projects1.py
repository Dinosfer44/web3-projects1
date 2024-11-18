from web3 import Web3

address = input ("Введите ваш адрес кошелька Metamask: ")
rpc_url = "https://1rpc.io/linea"

checksum_address = Web3.to_checksum_address(address)
print (checksum_address)
w3 = Web3(Web3.HTTPProvider("https://1rpc.io/linea"))
if w3.is_connected():
    print("Соединение установлено!")
else:
    print("Не удалось установить соединение.")
nonce = w3.eth.get_transaction_count(address)
print (f"Количество транзакций в кошелька в сети Linea: {nonce} txs")
balance = w3.eth.get_balance(address)
ether_balance = w3.from_wei(balance, 'ether')
print(f"Баланс адреса {address}: {ether_balance} ETH")