# Recurrence Relation

## 부제목
분할 알고리즘의 복잡도를 수식으로 표현

## 한 줄 정의
점화식(Recurrence Relation)은 알고리즘의 수행 시간을 더 작은 입력의 수행 시간으로 재귀적으로 정의하는 방정식이다.

## Master Theorem
`T(n) = aT(n/b) + f(n)` 형태일 때:
- `f(n) = O(n^(log_b a - ε))` → `T(n) = Θ(n^log_b a)`
- `f(n) = Θ(n^log_b a)` → `T(n) = Θ(n^log_b a · log n)`
- `f(n) = Ω(n^(log_b a + ε))` → `T(n) = Θ(f(n))`

## 예시 — Merge Sort
```text
T(n) = 2T(n/2) + O(n)
→ a=2, b=2, f(n)=n → n^log₂2 = n
→ Case 2: T(n) = Θ(n log n)
```
## 강의자료 출처

* CH01.pdf — Analyzing Algorithms and Problems
