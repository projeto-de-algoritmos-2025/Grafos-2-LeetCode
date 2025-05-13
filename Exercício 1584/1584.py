class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        n = len(points)
        visitado = [False] * n
        # Inicializamos a heap com (custo, indice). Começamos do ponto 0 com custo 0.
        min_heap = [(0, 0)]
        custoTotal = 0
        arestasSelecionadas = 0

        while arestasSelecionadas < n:
            custo, i = heapq.heappop(min_heap)
        
            # Caso o ponto já tenha sido visitado, continuamos.
            if visitado[i]:
                continue
        
            # Adiciona o ponto à MST e soma o custo.
            visitado[i] = True
            custoTotal += custo
            arestasSelecionadas += 1
        
            # Para cada ponto que ainda não foi visitado, calculamos a distância e adicionamos à heap.
            for j in range(n):
                if not visitado[j]:
                    xi, yi = points[i]
                    xj, yj = points[j]
                    novo_custo = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(min_heap, (novo_custo, j))
                
        return custoTotal
