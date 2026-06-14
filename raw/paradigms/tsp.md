# Traveling Salesman Problem (TSP)

## 부제목
모든 도시를 한 번씩 방문하는 최단 순회 경로 문제

## 한 줄 정의
외판원 문제(TSP)는 모든 도시를 정확히 한 번씩 방문하고 출발 도시로 돌아오는 최소 비용 경로를 찾는 NP-hard 문제이다.

## 구현 접근법별 복잡도 스펙
- Brute-force 전수 조사: `O(n!)`
- DP 기반 (Held-Karp 알고리즘): `O(2ⁿ · n²)`
- 다항 시간 근사 알고리즘 구조: `O(n² log n)`

> TSP는 완전한 계산 이론 내 NP-complete/NP-hard 범주의 대표적인 난제 모델입니다.

## 강의자료 출처
- CH13.pdf — NP-Complete Problems
