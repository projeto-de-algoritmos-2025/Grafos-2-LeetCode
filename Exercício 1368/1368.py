class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m, n = len(grid), len(grid[0])
        # Inicializa a matriz de custos com "infinito", exceto a célula inicial (0,0)
        custos = [[float('inf')] * n for _ in range(m)]
        custos[0][0] = 0

        # Mapear os movimentos:
        # índice 0 corresponde a sinal 1 (direita), índice 1 ao sinal 2 (esquerda),
        # índice 2 ao sinal 3 (baixo) e o índice 3, ao sinal 4 (cima)
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
        # A heap armazenará tuplas do tipo (custo_acumulado, i, j)
        heap = [(0, 0, 0)]
    
        while heap:
            custo_atual, i, j = heapq.heappop(heap)
        
            # Se já atingimos o destino, retornamos o custo acumulado.
            if i == m - 1 and j == n - 1: 
                return custo_atual
        
            # Se encontramos um custo maior que o registrado para esta célula, ignoramos.
            if custo_atual > custos[i][j]:
                continue
        
            # Para cada uma das 4 direções, calcula o novo custo e atualiza, se necessário.
            for d_index, (di, dj) in enumerate(DIRECTIONS):
                ni, nj = i + di, j + dj
                # Verifica se (ni, nj) está dentro dos limites do grid.
                if 0 <= ni < m and 0 <= nj < n:
                    # Se o movimento for o indicado pelo sinal na célula, extra_cost = 0; senão, 1.
                    custo_extra = 0 if grid[i][j] == d_index + 1 else 1
                    novo_custo = custo_atual + custo_extra
                    if novo_custo < custos[ni][nj]:
                        custos[ni][nj] = novo_custo
                        heapq.heappush(heap, (novo_custo, ni, nj))
    
        # Retorna o custo registrado na célula destino
        return custos[m - 1][n - 1]
