
def maximumPoints(k, costs):
    if (sum(costs) < k):
        return len(costs)
    else:
        while (sum(costs) > k):
            costs.remove(max(costs))
        return len(costs)
    
costs = [6,3,2,6,4,6,1, 9 ,14, 14 ,15 ,1 ,14]
k = 10
print(maximumPoints(k, costs))