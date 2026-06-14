# Prim's Algorithm

## 부제목
정점 확장 방식의 Greedy MST 알고리즘

## 한 줄 정의
Prim 알고리즘은 임의의 정점에서 시작하여, 이미 선택된 정점 집합에서 아직 선택되지 않은 정점으로 가는 최소 가중치 간선을 반복적으로 추가하여 MST를 구성한다.

## 알고리즘
```text
Prim(G, s):
  key[s] = 0; key[v] = ∞ for v ≠ s
  parent[s] = NULL
  Q = priority queue with all vertices (by key)
  while Q not empty:
    u = extract_min(Q)
    for each neighbor v of u:
      if v ∈ Q and w(u,v) < key[v]:
        parent[v] = u
        key[v] = w(u,v)

```

## Kruskal vs Prim 비교 규격

* **Kruskal**: 간선 위주 선택 / 희소 그래프(E ≈ V)에 유리 / 복잡도 `O(E log E)`
* **Prim**: 정점 위주 확장 / 밀집 그래프(E ≈ V²)에 유리 / 복잡도 `O(E log V)`

## 강의자료 출처

* CH08.pdf — Minimum Spanning Tree
