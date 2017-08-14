coins = [2, 3, 6, 7]

suma = 3

def findCoins(suma, coins):

    opts = [None] * (suma + 1)
    # If the value we are looking for is the value of a coin we need this value
    opts[0] = 0
    print 'Lets iterate from 1 to the sum we are looking for'
    for i in range(1, suma + 1):
        nCoins = 5000
        for coin in coins:
            print 'These are the coins {}'.format(coins)
            print 'If the coin {} is less than the number we are looking for {} it means maybe we can add up to that number'.format(coin, i)
            if coin <= i:
                print 'Maybe we can add up to this coin, lets see if the value - the coin {} - {} is less than the number of coins we already found'.format(i, coin)
                nCoins = min(nCoins, opts[i-coin] + 1)
            print 'We can form {} with {} coins'.format(i, nCoins)
            opts[i] = nCoins

findCoins(suma, coins)
