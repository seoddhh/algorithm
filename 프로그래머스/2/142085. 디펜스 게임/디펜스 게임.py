import heapq

def solution(n, k, enemy):
    heap = []
    
    for round_index, round_enemy in enumerate(enemy):
        
        n -= round_enemy
        heapq.heappush(heap, -round_enemy)
        
        if n < 0:
            if k == 0:
                return round_index
            n += -heapq.heappop(heap)
            k -= 1
            
    return len(enemy)
    
    