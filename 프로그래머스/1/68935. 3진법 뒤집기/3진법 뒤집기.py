def solution(n):
    arr = []

    while n > 0:
        arr.append(n % 3)
        n //= 3

    result = 0

    for num in arr:
        result = result * 3 + num

    return result