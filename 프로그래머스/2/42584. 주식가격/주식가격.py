def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)
    
    while stack:
        idx = stack.pop()
        answer[idx] = (n - 1) - idx
        
    return answer


# def solution(prices):
#     n = len(prices)
#     answer = [0] * n
    
#     for i in range(0, n-1):
#         for j in range(i+1, n):
#             answer[i] += 1
            
#             if prices[j] < prices[i]:
#                 break
#     return answer
            
            
            
            
            
            
            