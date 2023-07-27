import hashlib, base58, ecdsa
import bech32
import random
from bitcoinlib.services.services import Service


# Function to generate a random private key
def generate_random_private_key():
    return ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

# Function to generate a P2PKH address
def generate_p2pkh_address(private_key):
    ecdsa_public_key = private_key.get_verifying_key().to_string()
    sha256_hash = hashlib.sha256(ecdsa_public_key).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()

    versioned_hash = b'\x00' + ripemd160_hash

    sha256_hash = hashlib.sha256(hashlib.sha256(versioned_hash).digest()).digest()
    checksum = sha256_hash[:4]

    address_bytes = versioned_hash + checksum
    return base58.b58encode(address_bytes).decode('utf-8')

# Function to generate a P2SH address
def generate_p2sh_address(private_key):
    ecdsa_public_key = private_key.get_verifying_key().to_string()
    sha256_hash = hashlib.sha256(ecdsa_public_key).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()

    # P2SH addresses start with '3'
    versioned_hash = b'\x05' + ripemd160_hash

    sha256_hash = hashlib.sha256(hashlib.sha256(versioned_hash).digest()).digest()
    checksum = sha256_hash[:4]

    address_bytes = versioned_hash + checksum
    return base58.b58encode(address_bytes).decode('utf-8')

# Function to generate a Bech32 address (SegWit)
def generate_bech32_address(private_key):
    ecdsa_public_key = private_key.get_verifying_key().to_string()
    ripemd160_hash = hashlib.new('ripemd160', hashlib.sha256(ecdsa_public_key).digest()).digest()

    # Witness version for Bech32 addresses is '0' for P2WPKH (Pay to Witness Public Key Hash)
    witness_version = 0
    hrp = 'bc'  # Human-readable part for mainnet (replace with 'tb' for testnet)
    address = bech32.encode(hrp, witness_version, ripemd160_hash)

    return address

# Function to randomly select an address type
def get_random_address_type():
    address_types = ["P2PKH", "P2SH", "Bech32"]
    return random.choice(address_types)


def check_balance(address):  
    bitcoin_address = address
  
    balance = Service().getbalance(bitcoin_address)
    # Print the balance
    print(f"Address {bitcoin_address} Balance: {balance} Satoshi")
    return balance

# Function to save private key and address to a file
def save_to_file(private_key_hex, address):
    with open("generated_addresses.txt", "a") as file:
        file.write(f"Private Key: {private_key_hex}\n")
        file.write(f"Address: {address}\n\n")

while True:
    private_key = generate_random_private_key()
    address_type = get_random_address_type()

    private_key_hex = private_key.to_string().hex()
    print(f"Private Key: {private_key_hex}")

    if address_type == "P2PKH":
        address = generate_p2pkh_address(private_key)
    elif address_type == "P2SH":
        address = generate_p2sh_address(private_key)
    elif address_type == "Bech32":
        address = generate_bech32_address(private_key)
    else:
        print("Invalid address type. Supported types are 'P2PKH', 'P2SH', and 'Bech32'")
        continue

    balance = check_balance(address)
    balance_btc = balance / 100000000
    if balance > 0:
        print("\n\n\nFound a Bitcoin address with a non-zero balance!")
        print(balance_btc)
        save_to_file(private_key_hex, address)
        break


