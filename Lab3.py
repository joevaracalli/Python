
COMMISSION_RATE = 0.03
NUM_SHARES = 2000
PURCHASE_PRICE = 40.0
SELLING_PRICE = 42.75

amountPaidForStock = 0
purchaseCommission = 0
totalPaid = 0
tockSoldFor = 0
sellingCommission = 0
totalReceived = 0
profitOrLoss = 0

amountPaidForStock = NUM_SHARES*PURCHASE_PRICE
purchaseCommission= COMMISSION_RATE*amountPaidForStock

totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = NUM_SHARES *SELLING_PRICE
sellingCommission = COMMISSION_RATE*stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid

print('Cost paid of stock: $', amountPaidForStock)
print('Commission paid on the purchase: $', purchaseCommission)
print('Amount the stock sold: $', stockSoldFor)
print('Commission paid on the sale: $', sellingCommission)
print('Profit (or loss negative): $', profitOrLoss)
