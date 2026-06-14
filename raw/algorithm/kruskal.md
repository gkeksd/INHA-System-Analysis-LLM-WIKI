# Kruskal's Algorithm

## 부제목
간선 가중치 기준 Greedy로 MST를 구하는 알고리즘

## 한 줄 정의
Kruskal 알고리즘은 간선을 가중치 오름차순으로 정렬한 뒤, 사이클을 형성하지 않는 간선을 탐욕적으로 선택하여 최소 신장 트리(MST)를 구성한다.

## 알고리즘
```text
Kruskal(G):
  sort edges by weight (ascending)
  MST = {}
  initialize Union-Find for each vertex
  for each edge (u, v) in sorted order:
    if find(u) ≠ find(v):   // no cycle
      MST.add(u, v)
      union(u, v)
  return MST

```

## 복잡도

* `O(E log E)` — 간선 정렬 연산이 지배적임.

## 특징 및 연관관계

* Union-Find 자료구조와 함께 결합하여 파싱됨.
* Prim과 동일한 MST를 생성하지만 타겟 접근 전략이 다름.

## 강의자료 출처

* CH08.pdf — Minimum Spanning Tree, pp.5–10
