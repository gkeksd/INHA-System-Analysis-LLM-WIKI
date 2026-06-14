# Time Complexity

## 부제목
알고리즘의 수행 시간을 입력 크기의 함수로 분석

## 한 줄 정의
시간 복잡도(Time Complexity)는 알고리즘이 수행하는 **기본 연산(basic operation)**의 횟수를 입력 크기 `n`의 함수로 나타낸 것이다.

## 분석 유형
- **최악의 경우 (Worst-Case)** W(n) — 가장 많은 연산을 요구하는 입력
- **평균적인 경우 (Average-Case)** A(n) — 균등 분포 가정 하의 기댓값
- **최선의 경우 (Best-Case)** B(n) — 가장 적은 연산을 요구하는 입력

## 예시 — Sequential Search
```java
int seqSearch(int[] E, int n, int K) {
    int ans = -1;
    for (int index = 0; index < n; index++)
        if (K == E[index]) { ans = index; break; }
    return ans;
}
```

기본 연산: `K == E[index]` 비교 / W(n) = n (키가 없는 경우) → `O(n)`

## 강의자료 출처

* CH01.pdf — Analyzing Algorithms and Problems, p.7
