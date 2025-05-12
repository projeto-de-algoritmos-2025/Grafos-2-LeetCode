class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1  # Sem movimento no primeiro passo

        heap = [(0, 0, 0)]  # (tempo, x, y)
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            time, x, y = heapq.heappop(heap)
            if (x, y) == (m - 1, n - 1):
                return time
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    next_time = time + 1
                    required_time = grid[nx][ny]
                    if next_time >= required_time:
                        heapq.heappush(heap, (next_time, nx, ny))
                    else:
                        wait = required_time - next_time
                        if wait % 2 == 0:
                            heapq.heappush(heap, (required_time, nx, ny))
                        else:
                            heapq.heappush(heap, (required_time + 1, nx, ny))
        return -1
