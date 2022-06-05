# Quick statistics data calculations for chemistry

import statistics as stats

def promptDataList():
    data = []
    n = 1
    print('Please enter your data values:')
    while (True):
        num = input(f"{n}  ")
        if num == '':
            break
        try:
            num = float(num)
        except:
            print('NaN')
            continue
        data.append(num)
        n += 1
    return data
    
def promptSingleNum():
    print('Please input a number:')
    while(True):
        num = input()
        try:
            num = float(num)
            break
        except:
            print('NaN')
    return num

# stats.mean()
def findMean(data):
    return sum(data) / len(data)

# stats.stdev()
def sampleStandardDeviation(data):
    N = len(data)
    mean = findMean(data)
    ssd = (1/(N-1) * sum([(val - mean)**2 for val in data]))**0.5
    return ssd 

# stats.pstdev()
def populationStandardDeviation(data):
    N = len(data)
    mean = findMean(data)
    sdev = (1/N * sum([(val - mean)**2 for val in data]))**0.5
    return sdev

def relativeStandardDeviation(data):
    return sampleStandardDeviation(data) / abs(findMean(data))

def coefficientOfVariation(data):
    return sampleStandardDeviation(data) / findMean(data)

def percentRelativeStandardDeviation(data):
    return 100 * relativeStandardDeviation(data)

def percentRelativeError(trueVal, data):
    mean = findMean(data)
    return 100 * ((mean - trueVal)/trueVal)

# stats.variance()
def sampleVariance(data):
    return sampleStandardDeviation(data)**2

# stats.pvariance()
def populationVariance(data):
    return populationStandardDeviation(data)**2


if __name__ == '__main__':
    print('Welcome')
    print('Input the true value')
    trueVal = promptSingleNum()
    data = promptDataList()
    print('Mean:', findMean(data))
    print('Percent Relative Error:', percentRelativeError(trueVal, data))