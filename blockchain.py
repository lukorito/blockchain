class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self):
        # creates a new block and adds to the chain
        pass

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined block
        :param sender: <str> Address of the sender
        :param recipient: <str> Address of the recipient
        :param amount: <int> Amount
        :return: <int> The index of the block that will hold this transaction
        """
        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

    @staticmethod
    def hash(block):
        # creates hashes for blocks
        pass

    @property
    def last_block(self):
        # return the last block of the chain
        pass
