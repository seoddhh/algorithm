def solution(k, m, score):
    result = 0
    score.sort(reverse=True)
    
    for i in range(0, len(score), m):
        
        if len(score) - i < m:
            break
            
        result += score[i + m - 1] * m
        
    return result
       
