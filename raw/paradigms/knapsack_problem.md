# Knapsack Problem

## 부제목
0/1 배낭 문제 — NP-hard이지만 DP로 의사 다항 시간에 해결

## 한 줄 정의
배낭 문제(Knapsack Problem)는 무게 제한이 있는 배낭에 가치의 합이 최대가 되도록 물건을 담는 최적화 문제이다.

## 0/1 Knapsack DP 점화식 구조
```text
K[i][w] = 0                              (i=0 또는 w=0)
K[i][w] = K[i-1][w]                     (wᵢ > w)
K[i][w] = max(K[i-1][w],               (wᵢ ≤ w)
              K[i-1][w-wᵢ] + vᵢ)

```

## 복잡도 계층

* 시간 복잡도: `O(nW)` — 의사 다항 시간 (Pseudo-polynomial time, W는 배낭 최대 한도 용량)

> 0/1 Knapsack은 엄밀히 NP-hard 도메인이지만, DP 점화식 최적화를 통해 실용적인 시간 내 통제가 가능합니다.

## 강의자료 출처

* CH10.pdf — Dynamic Programming (Knapsack 응용 편)
