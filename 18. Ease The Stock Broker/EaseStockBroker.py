def balance_statement(lst):
    if (len(lst) == 0):
        return f"Buy: 0 Sell: 0"

    lst = [order.split() for order in lst.split(", ")]

    buy = int()
    sell = int()
    badly_count = int(0)
    badly = str()

    for order in lst:
        if (len(order) == 4 and order[1].find(".") == -1 and order[2].find(".") != -1 and (order[3] == "B" or order[3] == "S")):
            if (order[3] == "B"):
                buy += int(order[1]) * float(order[2])
            elif (order[3] == "S"):
                sell += int(order[1]) * float(order[2])
        else:
            badly_count += 1
            badly += f"{' '.join(order)} ;"

    if (len(badly) == 0):
        return f"Buy: {round(buy)} Sell: {round(sell)}"
    else:
        return f"Buy: {round(buy)} Sell: {round(sell)}; Badly formed {badly_count}: {badly}"

print(balance_statement(
    "GOOG 300 542.0 B, AAPL 50 145.0 B, CSCO 250.0 29 B, GOOG 200 580.0 S"))
