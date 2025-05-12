class Solution:
    def minimumCost(self, source: str, target: str,
                    original: List[str], changed: List[str], cost: List[int]) -> int:

        ALPHABET = 26
        graph = defaultdict(list)

        # Construir grafo
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            graph[u].append((v, w))  # direcionado

        def dijkstra(start: int) -> List[int]:
            dist = [float('inf')] * ALPHABET
            dist[start] = 0
            heap = [(0, start)]

            while heap:
                d, u = heapq.heappop(heap)
                if d > dist[u]:
                    continue
                for v, w in graph[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        heapq.heappush(heap, (dist[v], v))
            return dist

        min_cost = [dijkstra(i) for i in range(ALPHABET)]

        total_cost = 0
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
            s = ord(s_char) - ord('a')
            t = ord(t_char) - ord('a')
            if min_cost[s][t] == float('inf'):
                return -1
            total_cost += min_cost[s][t]

        return total_cost
