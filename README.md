# BruteForceBitcoin

BruteForceBitcoin is a tool that generates privates keys and their according public address recursively, until one of the generated public addresses have a positive balance. In which case the private key and its public address are saved to a file called generated_addresses.txt. This project is meant to demonstrate the robustness and security of the cryptography behind Bitcoin.

A Bitcoin private key is made up of 256 bits, thus, the chance of guessing a specific private key is 2^256. However in terms of financial motive guessing any address with a non-zero balance is sufficient, thus to find the probability of that occuring we have to divide the number of active addresses with a positive balance (let's say 45 million) by 2^256 yields the probability of guessing the key to an address with a positive balance. The number as you may imagine is miniscule, however what if you were to automate the process? For instance, how about you were able to generate 100 keys per second and check if the related public address has any BTC, and you let it run 24 hours for an entire year.

That would equate to 100*60*60*24*365 = 3,153,600,000 attempts. Despite this impressive number the probability of guessing a single one correctly is (45000000/2^256)*3153600000. In other words, 0.000000000000000000000000000000000000000000000000000000000000001225575952% chance.

In retrospect, cracking Bitcoin private keys is mind-bogglingly hard and practically impossible with current technology and foreseeable advancements. On other hand, this proves that your BTC is secure and cannot be hacked by this approach (realistically speaking). Nonetheless, there is still a chance that you get lucky and generate a private key linked to an active public address. If you want to try it out run **chmod +x main.sh** followed by **./main.sh** which will initiate 25 instances of the terminal that execute the test.py file, this program in turn goes through the entire process of generating private keys and checking the balance of the associated public addresses, in case it turns out that any of them have any bitcoin the program will store the private key and public address in a file called generated_addresses.txt. If you want to pressure your cpu even more, you can change the number of terminals test.py will run on in the bash file. There are 3 types of public addresses, the program is able of generating all of them and decides which one randomly.
