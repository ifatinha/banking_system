def report_generator(transactions, report_type):

    for transaction in transactions:
        transaction_type = transaction.get("type")

        if report_type == 1 and transaction_type == "Deposit":
            yield transaction
        elif report_type == 2 and transaction_type == "Withdraw":
            yield transaction
        elif report_type == 3:
            yield transaction
