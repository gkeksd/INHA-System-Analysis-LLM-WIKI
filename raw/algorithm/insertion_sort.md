# Insertion Sort

## 부제목
순차적으로 원소를 적절한 위치에 삽입하는 정렬

## 한 줄 정의
삽입 정렬은 배열을 순회하며 각 원소를 이미 정렬된 앞부분의 적절한 위치에 삽입하는 정렬 알고리즘이다.

```java
void insertionSort(Element[] E, int n) {
    for (int xindex = 1; xindex < n; xindex++) {
        Element current = E[xindex];
        Key x = current.key;
        int xLoc = shiftVacRec(E, xindex, x);
        E[xLoc] = current;
    }
}

```

## 복잡도

* Best (이미 완벽히 정렬됨): `O(n)`
* Average / Worst (역순 정렬 상태): `O(n²)` — 최악 연산 횟수 `W(n) = n(n-1)/2`

## 강의자료 출처

* CH04.pdf — Insertion Sort, pp.3–6
