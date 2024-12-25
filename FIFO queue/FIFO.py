import csv
from collections import deque
from datetime import datetime

class FIFOBasedInvestmentSystem:
    
    def __init__(money):
        money.inflows = deque()
        money.outflows = []

    def process_transaction(money, trxn_id, transaction_amount, transaction_date, transaction_sign):
        transaction_date = datetime.strptime(transaction_date, "%Y-%m-%d")

        if transaction_sign == '+':
             # inflow "+"
            money.inflows.append({
                "trxn_id": trxn_id,
                "amount_remain": transaction_amount,
                "inflow_date": transaction_date,
                "outflow_date": None
            })

        elif transaction_sign =='-'    :
              # Out flow "-"
              outflow_amount = transaction_amount
              while outflow_amount > 0 and money.inflows:
                  inflow = money.inflows[0]
                  if inflow["amount_remain"] > outflow_amount:
                      inflow["amount_remain"] -= outflow_amount
                      outflow_amount = 0
                
                  else:
                    outflow_amount -= inflow["amount_remain"]
                    inflow["amount_remain"] = 0
                    inflow["outflow_date"] = transaction_date
                    money.inflows.popleft()

def generate_report(self, output_file):
    with open(output_file, mode='w' , newline='')as file:
        writer = csv.writer(file)
        writer.writerow(["Transaction ID", "Amount Remaning", "Inflow Date"])

        for inflow in self.inflows:
            writer.writerow([
                inflow["trxn_id"],
                inflow["amount_remain"],
                inflow["inflow_date"].strftime("%Y-%m-%d"),
                inflow["outflow_date"].strtime("%Y-%m-%d") if inflow["outflow_date"] else ""
            ])

if __name__ =="__main__":
    system = FIFOBasedInvestmentSystem()
              #transection data    
    transactions =[
        {"trxn_id": "S1", "transaction_amount": 10000, "transaction_date": "2024-12-01", "transaction_sign": "+" },
        {"trxn_id": "S2", "transaction_amount": 800, "transaction_date": "2024-12-02",   "transaction_sign": "-" },
        {"trxn_id": "S3", "transaction_amount": 500, "transaction_date": "2024-12-03",   "transaction_sign": "-" },
        {"trxn_id": "S4", "transaction_amount": 800, "transaction_date": "2024-12-04",   "transaction_sign": "+" }

]

for transaction in transactions:
    system.process_transaction(
        transaction["trxn_id"],
        transaction["transaction_amount"],
        transaction["transaction_date"],
        transaction["transaction_sign"]
    )
            # Report
    output_file = "transaction_report.csv"
    system.generate_report(output_file)
    print(f"Report generated: {output_file}")