coins = [2, 3, 6, 7]

suma = 13

def findCoins(suma, coins):

    opts = [None] * (suma + 1)
    opts[0] = 0
    for i in range(1, suma + 1):
        nCoins = 5000
        for coin in coins:
            if coin <= i:
                nCoins = min(nCoins, opts[i-coin] + 1)
            opts[i] = nCoins
    print 'For coins {} and sum {}'.format(coins, suma)
    print opts

findCoins(suma, coins)
