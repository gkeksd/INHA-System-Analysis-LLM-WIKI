# Dijkstra's Algorithm

## 부제목
단일 출발점 최단 경로를 Greedy로 구하는 알고리즘

## 한 줄 정의
Dijkstra 알고리즘은 음수 간선이 없는 가중 그래프에서 단일 출발점(single-source)으로부터 모든 정점까지의 최단 경로를 구하는 탐욕 알고리즘이다.

## 핵심 아이디어
> 매 단계에서 아직 방문하지 않은 정점 중 출발점으로부터의 거리가 가장 짧은 정점을 선택한다 (Greedy Choice).

## 알고리즘
```text
dijkstra(G, s):
  dist[s] = 0; dist[v] = ∞ for all v ≠ s
  Q = priority queue with all vertices
  while Q not empty:
    u = extract_min(Q)
    for each neighbor v of u:
      if dist[u] + w(u,v) < dist[v]:
        dist[v] = dist[u] + w(u,v)
        decrease_key(Q, v)

```

## 복잡도

* 인접 행렬 구조: `O(V²)`
* 이진 힙 구조: `O((V+E) log V)`
* 피보나치 힙 구조: `O(V log V + E)`

## 강의자료 출처

* CH08.pdf — Single-Source Shortest Paths, pp.12–18
