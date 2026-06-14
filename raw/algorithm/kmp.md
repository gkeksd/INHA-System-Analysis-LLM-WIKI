# KMP Algorithm

## 부제목
접두사/접미사를 이용한 O(n+m) 문자열 매칭

## 한 줄 정의
KMP(Knuth-Morris-Pratt) 알고리즘은 불일치 발생 시 이미 비교한 정보를 재활용하여 패턴을 텍스트에서 효율적으로 탐색하는 문자열 매칭 알고리즘이다.

## 핵심 아이디어
> 불일치가 발생하면, P[0..j]의 고유한 최장 진접두사-접미사(failure function) 배열을 이용하여 패턴을 논리적으로 이동시킨다.

## 복잡도
- 전처리 단계: `O(m)`
- 본문 탐색 단계: `O(n)`
- 전체 매칭 복잡도: `O(n + m)` (기존 Brute-force의 O(nm) 대비 파격적 성능 개선)

## 강의자료 출처
- CH11.pdf — String Matching, KMP Algorithm
