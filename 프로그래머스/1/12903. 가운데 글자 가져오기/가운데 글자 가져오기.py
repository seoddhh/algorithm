def solution(s):
    answer = ''
    length = len(s)
    
    mid = length // 2

    if length % 2 == 1:      
        answer = s[mid]
    else:                   
        answer = s[mid - 1] + s[mid]

    return answer