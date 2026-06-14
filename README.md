
# 🚀 Agile Knowledge LLM Wiki & Topology Engine

본 저장소는 사용자가 투입한 원천 지식(Raw Data)을 규칙 기반 하네스(Hannes) 에이전트 인프라를 통해 파싱하고, [하네스 + LLM Wiki + 시각화 도구]를 단일 패키지로 통합하여 제공하는 지식 관리 프로그램입니다.

---

## 1. 시스템 아키텍처 및 MCP 도구 인터페이스

본 시스템은 에이전트가 외부 도구를 활용해 지식을 지능적으로 관리할 수 있도록 Model Context Protocol(MCP) 규격을 지원합니다.

```text
  [User Raw Data Input] ──> [Hannes Hook Engine (hooks.py)]
                                     │
                                     ▼
 [Visualizer Dashboard] <── [Wiki Central DB (pages.json)] <── [MCP Server] <── [Agent]

```

### ⚙️ 제공 가능한 MCP 도구 목록 (MCP Tools)

* `search_page` : 지식 베이스 내부에서 특정 키워드를 기반으로 연관 페이지 목록을 검색합니다.
* `read_page` : 요청된 특정 위키 페이지의 내용, 태그, 관계 토폴로지를 JSON 객체로 반환합니다.
* `related_pages` : 현재 조회 중인 노드와 가장 긴밀한 연관성을 가진 주변 컨텍스트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된 전체 지식 그래프 구조를 위상 정렬(Topological Sort) 관점으로 분석하여 최적의 추천 시퀀스 경로를 산출합니다.

---

## 2. 개발 환경 및 요구 인프라 (Dependencies)

서버 및 전처리 모듈을 정상 구동하기 위해 아래 환경 세팅을 준비해야 합니다. (3분 이내 완료)

* **Runtime Environment**: Python 3.8 이상 설치 필수
* **의존성 패키지 설치**:
터미널 환경에서 아래 명령어를 실행하여 웹 서버 및 라우팅 인프라를 설치합니다.
```bash
pip install Flask==2.3.2

```



---

## 3. ⏱️ [30분 완성] 새로운 자료 투입 및 위키 빌드 퀵스타트 가이드

처음 프로젝트를 클론한 사용자라도 **30분 안에 본인 자료 1건을 반영하여 화면에서 시각화**할 수 있는 절차는 다음과 같습니다.

### 단 3개의 Step으로 나만의 위키 생성하기

#### 📌 Step 1: 나만의 지식 원천 데이터 투입 (`raw/` 경로)

`raw/` 디렉토리 내에 새로 추가하고 싶은 주제를 담은 마크다운 파일(예: `raw/my_topic.md`)을 생성하고 아래 예시 규격처럼 내용을 작성합니다.

> **🚨 중요 가이드라인:** 파일의 첫 번째 줄은 반드시 `# [주제명]` 형태의 대제목(H1) 구조여야 하네스 에이전트가 정상적으로 페이지 ID를 바인딩합니다.

```markdown
# Greedy Algorithm

## 탐욕 알고리즘의 정의
매 순간 가장 최적이라고 생각되는 단기적 선택을 유도하여 최종 해답에 도달하는 기법입니다.

## 핵심 해결 조건
- 탐욕스런 선택 조건 (Greedy Choice Property)
- 최적 부분 구조 (Optimal Substructure)

## 연결성 요소
이 개념은 Dynamic Programming의 메모이제이션 설계 방식 및 Dijkstra 최단 경로 모델과 결합하여 응용될 수 있습니다.

```

#### 📌 Step 2: 하네스 에이전트 전처리 Hook 실행

원천 마크다운 데이터 작성이 완료되면, 터미널에서 하네스 Hook 스킬 엔진을 구동합니다. 이 엔진은 스키마 유효성을 자동 검증하고 관계 토폴로지를 추출하여 데이터베이스에 저장합니다.

```bash
python hannes/hooks.py

```

*성공 시 콘솔에 `[Success] Hook processed: 'Greedy Algorithm' integration complete.` 메시지가 출력됩니다.*

#### 📌 Step 3: 통합 시각화 대시보드 뷰어 구동

최종 결과물을 확인하기 위해 아래 명령어로 웹 통합 엔진을 실행합니다.

```bash
python app.py

```

서버가 켜지면 브라우저를 열고 `http://localhost:5000`에 접속합니다. 좌측 내비게이션 메뉴에 내가 넣은 `Greedy Algorithm`이 정상 등록되어 있으며, 우측 시각화 패널에 연관 관계 그래프가 실시간 매핑되는 것을 확인하면 검증이 완료됩니다.

---

## 4. 데이터 무결성 검증 (Validation)

본 제품의 모든 산출물은 `schema/wiki_schema.json`에 정의된 정형 JSON 스키마 규격을 100% 준수합니다. 에이전트 운영 지침 파일인 `hannes/RULES.md`에 명시된 제약 사항에 따라 지식 고립 상태(연결 링크가 없는 상태)의 노드가 감지되거나 규격이 어긋날 경우 파싱 프로세스가 자동으로 보호 및 제한됩니다.

```
