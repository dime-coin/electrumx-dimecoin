import requests, os

# barrystyle 23072023
#
# this method cannot be async as it is called directly
# from spend_utxo, which is not an async function.

utxo = []

def rpc_call(method, params):

    url = 'http://' + os.environ['DAEMON_URL']

    payload = {
        "method": method,
        "params": params,
        "jsonrpc": "2.0",
        "id": 0,
    }

    return requests.post(url, json=payload).json()['result']

def add_to_known_spends(tx_hash, tx_num):

    item = tx_hash + str(tx_num)
    if item in utxo:
        print ('** possible doublespend of ' + tx_hash + '/' + str(tx_num))
    else:
        utxo.append(item)

def get_raw_utxo_value(tx_hash, tx_num):

    value = 0

    try:
        tx = rpc_call("getrawtransaction", [tx_hash, True])
        vout = tx['vout'][tx_num]
        value = int(vout['value'] * 1000000)
        print ('retrieved nvalue ' + str(value) + ' for utxo ' + tx_hash + '/' + str(tx_num))
    except:
        print ('failed to retrieve nvalue of utxo ' + tx_hash + '/' + str(tx_num))

    add_to_known_spends(tx_hash, tx_num)

    return value
