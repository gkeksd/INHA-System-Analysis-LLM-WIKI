# Dynamic Programming

## 부제목
부분 문제의 해를 저장하여 중복 계산을 제거하는 설계 패러다임

## 한 줄 정의
동적 프로그래밍(DP)은 중복되는 부분 문제(overlapping subproblems)의 해를 테이블에 저장(memoization)하여 재계산을 피하는 알고리즘 설계 패러다임이다.

## 핵심 충족 조건
- **Optimal Substructure**: 전역 최적 해 구조 내에 하위 부분 문제의 최적 해가 완전히 내포됨.
- **Overlapping Subproblems**: 동일한 연산 구조를 가진 하위 스페이스의 문제들이 반복하여 호출됨.

## 대표 구현 가이드라인
- **Top-Down (Memoization)**: 재귀 구조 + 캐싱 레이어 결합 (필요한 노드 위주 연산)
- **Bottom-Up (Tabulation)**: 루프 반복문 + 상태 테이블 빌드 (안정적 스택 관리 가능)

## 강의자료 출처
- CH10.pdf — Dynamic Programming 총론
