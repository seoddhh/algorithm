import heapq

def solution(n, k, enemy):
    heap = []
    
    for round_index, total_enemy in enumerate(enemy):
        
        n -= total_enemy
        heapq.heappush(heap, -total_enemy)
        
        if n < 0:
            if k == 0:
                return round_index
            n += -heapq.heappop(heap)
            k -= 1
            
    return len(enemy)
    
    