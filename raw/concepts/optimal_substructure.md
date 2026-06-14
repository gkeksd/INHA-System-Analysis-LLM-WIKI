# Optimal Substructure

## 부제목
최적 해가 부분 문제의 최적 해로 구성되는 성질

## 한 줄 정의
최적 부분 구조(Optimal Substructure)란 문제의 최적 해가 부분 문제(subproblem)들의 최적 해를 포함하는 성질이다.
> 이 성질이 성립하면 Dynamic Programming 또는 Greedy Algorithm을 적용할 수 있다.

## 예시 — Matrix Chain Multiplication
A₁…Aⱼ의 최적 분할은 A₁…Aₖ의 최적 분할과 Aₖ₊₁…Aⱼ의 최적 분할을 포함한다.
```text
m[i,j] = 0                          (i = j)
m[i,j] = min{ m[i,k] + m[k+1,j] + p_{i-1}·p_k·p_j }  (i < j)
```
## 강의자료 출처

* CH10.pdf — Dynamic Programming, pp.5–8
