import os
import json
import re

def pre_input_hook(raw_filepath, output_jsonpath):
    """
    개별 마크다운 파일을 파싱하여 구조화된 위키 JSON 포맷으로 전환 및 병합하는 함수
    """
    if not os.path.exists(raw_filepath):
        return False
        
    try:
        with open(raw_filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"[Error] 파일을 읽는 중 오류 발생 ({raw_filepath}): {e}")
        return False
        
    # 제목(H1) 추출 및 문자열 공백 제거 (.strip() 반영)
    title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Untitled Page"
    
    # 부제목 추출 시도 (없으면 기본값 제공)
    subtitle_match = re.search(r'^##\s+부제목\s*\n+(.*)', content, re.MULTILINE)
    subtitle = subtitle_match.group(1).strip() if subtitle_match else "Algorithm & System Analysis Document"
    
    # 상위 서브 디렉토리 이름을 태그로 자동 할당 (algorithm, concepts, paradigms)
    folder_tag = os.path.basename(os.path.dirname(raw_filepath)).lower()
    
    # [연관관계 강화 기법] 본문 내부 키워드 스캔 + 예외 방어선 구축
    keywords_map = {
        "big_o_notation": ["time_complexity", "space_complexity", "recurrence_relation", "algorithm_analysis"],
        "time_complexity": ["big_o_notation", "space_complexity", "algorithm_analysis"],
        "space_complexity": ["big_o_notation", "time_complexity", "dynamic_programming"],
        "recurrence_relation": ["merge_sort", "quick_sort", "binary_search", "divide_and_conquer"],
        "optimal_substructure": ["dynamic_programming", "greedy_choice", "knapsack_problem", "lcs", "tsp"],
        "greedy_choice": ["optimal_substructure", "dijkstra", "kruskal", "prim"],
        "algorithm_analysis": ["big_o_notation", "time_complexity", "space_complexity"],
        "merge_sort": ["divide_and_conquer", "quick_sort", "recurrence_relation"],
        "quick_sort": ["divide_and_conquer", "merge_sort", "recurrence_relation"],
        "binary_search": ["divide_and_conquer", "time_complexity"],
        "dijkstra": ["greedy_choice", "optimal_substructure", "floyd_warshall", "prim"],
        "floyd_warshall": ["dynamic_programming", "dijkstra", "optimal_substructure"],
        "kruskal": ["greedy_choice", "prim", "optimal_substructure"],
        "prim": ["greedy_choice", "kruskal", "dijkstra"],
        "insertion_sort": ["time_complexity", "merge_sort"],
        "kmp": ["algorithm_analysis", "time_complexity"],
        "knapsack_problem": ["dynamic_programming", "optimal_substructure", "np_completeness", "tsp"],
        "lcs": ["dynamic_programming", "optimal_substructure", "knapsack_problem"],
        "tsp": ["np_completeness", "dynamic_programming", "knapsack_problem"],
        "divide_and_conquer": ["merge_sort", "quick_sort", "binary_search", "recurrence_relation"],
        "dynamic_programming": ["optimal_substructure", "knapsack_problem", "lcs", "floyd_warshall", "tsp"],
        "np_completeness": ["tsp", "knapsack_problem", "algorithm_analysis"]
    }

    current_id = title.lower().replace(" ", "_").replace("-", "_").replace("'", "")
    
    # 딕셔너리 기반 연관 링크 자동 바인딩 (없을 시 본문 텍스트 매칭 유도)
    related = keywords_map.get(current_id, [])
    if not related:
        # 폴더명이 같으면 서로 연결 고리를 만들어 주도록 서브 백업 규칙 배치
        if folder_tag == "algorithm":
            related = ["merge_sort", "quick_sort", "dijkstra"]
        elif folder_tag == "concepts":
            related = ["big_o_notation", "time_complexity"]
        else:
            related = ["dynamic_programming", "divide_and_conquer"]

    new_page = {
        "id": current_id,
        "title": title,
        "subtitle": subtitle,
        "content": content,
        "tags": [folder_tag.capitalize(), "Auto-Hooked"],
        "related": related
    }
    
    # 기존 중앙 위키 DB 로드 후 누적 병합
    db_data = {}
    if os.path.exists(output_jsonpath):
        try:
            with open(output_jsonpath, 'r', encoding='utf-8') as db_f:
                db_data = json.load(db_f)
        except json.JSONDecodeError:
            db_data = {}
            
    db_data[current_id] = new_page
    
    with open(output_jsonpath, 'w', encoding='utf-8') as db_f:
        json.dump(db_data, db_f, ensure_ascii=False, indent=2)
        
    print(f"  └ [성공] 파싱 및 링크 결합 완료: '{title}' -> 위키 DB 반영")
    return True

def hook_all_subdirectories(base_raw_dir, output_jsonpath):
    print("==================================================")
    print("🚀 하네스 지식 인프라: 고밀도 토폴로지 일괄 스캔 시작")
    print("==================================================")
    
    if os.path.exists(output_jsonpath):
        try: os.remove(output_jsonpath)
        except: pass

    count = 0
    for root, dirs, files in os.walk(base_raw_dir):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                success = pre_input_hook(full_path, output_jsonpath)
                if success: count += 1
                    
    print("==================================================")
    print(f"✨ 종합 결과: 총 {count}개의 데이터가 유기적 관계망으로 묶였습니다.")
    print("==================================================")

if __name__ == "__main__":
    os.makedirs("wiki", exist_ok=True)
    hook_all_subdirectories("raw", "wiki/pages.json")
