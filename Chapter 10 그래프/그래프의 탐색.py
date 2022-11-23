mygraph = { "A" : {"B","C"},
         "B": {"A","D"},
         "C": {"A","D","E"},
         "D": {"B","C","F"},
         "E": {"C","G","H"},
         "F": {"D"},
         "G": {"E","H"},
         "H": {"E","G"}}

import collections

def dfs(graph, start, visited = set()) :   # 처음 호출할 때 visited 공집합
    if start not in visited :   # start가 방문하지 않은 정점이면
        visited.add(start)  # start를 방문한 노드 집합에 추가
        print(start, end =" ")  # start를 방문했다고 출력함
        nbr = graph[start] - visited   # nbr : 차집합 연산 이용 ( nbr = 인접정점 - 방문접점 )
        for v in nbr:   # nbr이 set이므로 순서대로가 아니라 결과가 매번 다르게 나옴
            dfs(graph, v, visited) # nbr, 즉 인접한데 방문하지 않은 정점에 대하여 dfs를 순환적으로 호출
            
def bfs(graph, start, visited = set()) :
    visited.add(start)  # 맨 처음에 start만 방문한 정점
    queue = collections.deque([start])  # 덱 객체 생성 (큐로 사용)
    while queue:    # queue가 공백이 아닐 때 까지
        vertex = queue.popleft()    # 큐에서 하나의 정점을 꺼내서 vertex에 저장
        print(vertex, end=' ')  # vertex는 방문했으므로 출력
        nbr = graph[vertex] - visited   # nbr : 차집합 연산 이용 ( vertex와 연결된 인접정점 - 방문정점 )
        for v in nbr:   # vertex와 인접한데 방문하지 않은 정점에 대하여
            visited.add(v)  # v를 하나씩 방문
            queue.append(v) # 이제 v를 큐에 삽입하여 다시 반복문으로 
            
def bfsST(graph, start) :
    visited = set([start])
    queue = collections.deque([start])
    while queue:
        v = queue.popleft()
        nbr = graph[v] - visited
        for u in nbr:
            print("(", v, ",", u, ") ", end = "")
            visited.add(u)
            queue.append(u)

print("- "*20)
print("dfs (깊이 우선 탐색) : ", end = ' ')
dfs(mygraph, 'A')
print("\nbfs (너비 우선 탐색) : ", end = ' ')
bfs(mygraph, 'A')
print("\nbfsST (너비 우선 탐색.ver 신장 트리) : ", end = ' ')
bfsST(mygraph, 'A')
print()
print("- "*20)