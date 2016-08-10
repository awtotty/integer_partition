# Assumes series1 and series2 have same length and returns a truncated
# series product that drops terms past the length of original series.
# Ex: _trunc_product([1, 0, 1, 0], [1, 1, 1, 1]) returns [1, 1, 2, 1]

def _trunc_product(series1, series2):
    if len(series1) == 0 or len(series2) == 0:
        return []

    res = [0 for _ in range(len(series1))]
    for i in range(len(series1)):
        for j in range(len(series2)):
            if i+j < len(series1):
                res[i+j] += series1[i]*series2[j]
    return res


# Returns a partial power series representation of 1/(1-x^k) where
# k is coin_value.

def _generate_coin_series(coin_value, size):
    if size == 0:
        return []

    res = [i for i in range(size+1)]
    index_list = res[::coin_value]
    for i in res:
        res[i] = 1 if (i in index_list) else 0
    return res

# Create a list of all series representations for coin values,
# then find their product. Return the coefficient of the x^n term.

def p(n, coin_list):
    series_array = [_generate_coin_series(i, n) for i in coin_list]

    for i in range(1, len(series_array)):
        series_array[0] = _trunc_product(series_array[0], series_array[i])

    return series_array[0][n]


# Examples:
print 'amount = 4, denoms = [1,2,3]:', p(4,[1,2,3])
print 'amount = 5, denoms = [1,2,3]:', p(5,[1,2,3])
print 'amount = 5, denoms = [1,2,4]:', p(5,[1,2,4])
print 'amount = 6, denoms = [1,2,3]:', p(6,[1,2,3])
print 'amount = 20, denoms = [2,3,6]:', p(20,[2,3,6])
print 'amount = 100, denoms = [1, 2, .. , 99]:', p(100, range(1, 100))
