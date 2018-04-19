from iota import *
import sys

SEED1 = b"INSERT A VALID SEED HERE!!!"
ADDRESS_WITH_CHECKSUM_SECURITY_LEVEL_2 = b"INSERT A VALID ADDR HERE!!"
api = Iota('http://localhost:14265/', seed = SEED1)

def main():
	if len(sys.argv[1:]) != 2:
		print("Error: Numero de argumentos invalido.")
		print("Uso: python tx_th.py NUM_BUNDLES NUM_TX_PER_BUNDLE")
		sys.exit(1)
	tx = ProposedTransaction(
              address = Address(ADDRESS_WITH_CHECKSUM_SECURITY_LEVEL_2),
              value = 0,
              tag = Tag(b'EXAMPLE'),
              message = TryteString.from_string('temperatura: 123 Fahrenheit :D'),
        )

	l_bundle = [ProposedBundle() for i in range(int(sys.argv[1]))]

	for i in range(int(sys.argv[1])):
		for j in range(int(sys.argv[2])):
			l_bundle[i].add_transaction(tx)
		l_bundle[i].finalize()
		api.send_trytes(trytes=l_bundle[i].as_tryte_strings(), depth=10)

main()
