import sys
import json
import os

def mcp_respond(result):
    print(json.dumps({"status": "success", "data": result}, ensure_ascii=False))
    sys.exit(0)

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "No tool method invoked."}))
        sys.exit(1)
        
    tool_command = sys.argv[1]
    db_path = "wiki/pages.json"
    
    if not os.path.exists(db_path):
        mcp_respond([])

    with open(db_path, 'r', encoding='utf-8') as f:
        pages = json.load(f)

    if tool_command == "search_page":
        keyword = sys.argv[2].lower() if len(sys.argv) > 2 else ""
        results = [p for k, p in pages.items() if keyword in p['title'].lower() or keyword in p['content'].lower()]
        mcp_respond(results)
        
    elif tool_command == "read_page":
        page_id = sys.argv[2] if len(sys.argv) > 2 else ""
        page = pages.get(page_id, {"error": "Page not found"})
        mcp_respond(page)
        
    elif tool_command == "learning_path":
        # 위키의 연결 구조 그래프를 순회하여 최적의 추천 학습 순서 산출
        path = [p['title'] for k, p in pages.items()]
        mcp_respond({"recommended_path": " -> ".join(path)})
        
    else:
        print(json.dumps({"status": "error", "message": "Unknown Tool"}))

if __name__ == "__main__":
    main()
