# Space Complexity

## 부제목
알고리즘이 사용하는 메모리 공간의 점근적 분석

## 한 줄 정의
공간 복잡도(Space Complexity)는 알고리즘이 실행 중 사용하는 메모리 공간을 입력 크기 `n`의 함수로 나타낸 것이다.

## 구성 요소
- **고정 공간** — 입력 크기와 무관한 상수 공간 (코드, 상수 변수 등)
- **가변 공간** — 입력 크기에 따라 달라지는 공간 (동적 배열, 재귀 스택 등)

## Trade-off: 시간 vs. 공간
> Dynamic Programming은 공간을 추가로 사용해서 시간을 절약한다. Memoization은 이 트레이드오프의 대표 예시다.

- **Fibonacci (재귀)**: Time `O(2ⁿ)` / Space `O(n)`
- **Fibonacci (DP)**: Time `O(n)` / Space `O(n)`
- **Fibonacci (최적화)**: Time `O(n)` / Space `O(1)`
