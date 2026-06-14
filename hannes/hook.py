import os
import json
import re

def pre_input_hook(raw_filepath, output_jsonpath):
    """
    지식 투입 자동 파싱 및 유효성 검증 Hook Skill
    마크다운 텍스트를 구조화된 위키 JSON 데이터 포맷으로 자동 전환
    """
    if not os.path.exists(raw_filepath):
        print(f"[Error] File not found: {raw_filepath}")
        return False
        
    with open(raw_filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 간단한 정규식 기반 메타데이터 및 타이틀 추출 파싱 엔진
    title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Untitled Page"
    
    # 핵심 단어 추출을 통한 연관 관계 후보군 자동 추천 알고리즘 (Skill)
    keywords = ["Dijkstra", "Kruskal", "Dynamic Programming", "Greedy", "Graph", "Complexity"]
    related = [kw for kw in keywords if kw.lower() in content.lower() and kw.lower() != title.lower()]

    new_page = {
        "id": title.lower().replace(" ", "_"),
        "title": title,
        "subtitle": "Auto-generated via Hannes Input Hook System",
        "content": content.replace("'", '"'),
        "tags": ["Algorithm", "Concepts"],
        "related": list(set(related))
    }
    
    # 기존 DB 파일 로드 및 병합
    db_data = {}
    if os.path.exists(output_jsonpath):
        try:
            with open(output_jsonpath, 'r', encoding='utf-8') as db_f:
                db_data = json.load(db_f)
        except json.JSONDecodeError:
            db_data = {}
            
    db_data[new_page["id"]] = new_page
    
    with open(output_jsonpath, 'w', encoding='utf-8') as db_f:
        json.dump(db_data, db_f, ensure_ascii=False, indent=2)
        
    print(f"[Success] Hook processed: '{title}' integration complete.")
    return True

if __name__ == "__main__":
    # 테스트 구동 프로세스
    os.makedirs("wiki", exist_ok=True)
    pre_input_hook("raw/algorithm/binary_search.md", "wiki/pages.json")
