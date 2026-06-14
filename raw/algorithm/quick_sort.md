# Quick Sort

## 부제목
피벗 기반 분할로 평균 O(n log n)을 달성하는 정렬

## 한 줄 정의
Quick Sort는 피벗(pivot)을 기준으로 배열을 분할하여 재귀적으로 정렬하는 분할 정복 알고리즘이다.

## 알고리즘 (파티션)
```java
int partition(int[] A, int low, int high) {
    int pivot = A[high];
    int i = low - 1;
    for (int j = low; j < high; j++)
        if (A[j] <= pivot) { i++; swap(A, i, j); }
    swap(A, i+1, high);
    return i + 1;
}
```
## 복잡도 분석

* Best / Average: `O(n log n)`
* Worst (이미 정렬된 입력): `O(n²)`

> 실제로는 Merge Sort보다 빠른 경우가 많다 — 캐시 친화적이고 제자리(in-place) 정렬이 가능하기 때문이다.

## 강의자료 출처

* CH04.pdf — Sorting, pp.5–9
