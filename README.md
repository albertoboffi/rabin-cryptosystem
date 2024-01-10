# Rabin Cryptosystem
Robust implementation of the Rabin cryptosystem encryption algorithm.
## Usage
To install the required dependencies:
```bash
pip install python-secrets primality
```
The repository provides the option to use the standard version of the Rabin cryptosystem, which operates on integers, or its extension for encrypting and decrypting generic texts. Usage illustrations for both cases can be found in the [examples](https://github.com/albertoboffi/rabin-cryptosystem/tree/main/examples) folder. 

Output examples:
```console
foo@bar:~/rabin-cryptosystem/examples$ python3 int_encryption.py
Original message >>  741
Encrypted message >>  196924014
Decrypted message >>  741
```
```console
foo@bar:~/rabin-cryptosystem/examples$ python3 str_encryption.py
Original message >>  Hello world! What a beautiful day :)
Encrypted message >>  ᒨ߀Ვ莦⃣𖪈⃣𖪈֦飄Дᛀᢶ쵯֦飄‑𕺷⃣𖪈ᒷ笍і⊹Дᛀḩՙ㒧﬽╾ҹ㈓⠃Дᛀ╾ҹДᛀ♅ƔᲕ莦╾ҹؽᾷ㈓⠃ߡ㝙⒇鯡ؽᾷ⃣𖪈Дᛀᒷ笍╾ҹ⮀㌏Дᛀ൧᠔ڲỉ
Decrypted message >>  Hello world! What a beautiful day :)
```
## License
This project falls under the GNU General Public License v3.0.