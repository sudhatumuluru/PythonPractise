def find_sum_below(limit=1000):
    return False

def is_multiple_of_3and5(x):
    results = [x % 3, x % 5]
    return any(not i for i in results)

if __name__ == '__main__':
    STOP=1000
    result=0
    for i in range(1,STOP):
        if is_multiple_of_3and5(i):
            result+=i
    print(result)
