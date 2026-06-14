from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__, template_folder='templates')
DB_PATH = 'wiki/pages.json'

def load_wiki_data():
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/wiki')
def get_all_wiki():
    return jsonify(load_wiki_data())

@app.route('/api/graph')
def get_graph_data():
    data = load_wiki_data()
    nodes = []
    edges = []
    
    valid_ids = set(data.keys())

    for key, val in data.items():
        # 노드 등록
        nodes.append({
            "id": val["id"], 
            "label": val["title"]
        })
        
        # 엣지 등록
        for rel_id in val.get("related", []):
            clean_rel_id = rel_id.lower().strip()
            # 실제로 DB에 존재하는 타겟 노드 아이디일 경우에만 매핑 선 연결
            if clean_rel_id in valid_ids and clean_rel_id != val["id"]:
                edges.append({
                    "from": val["id"], 
                    "to": clean_rel_id
                })

    # 중복 관계선 정리
    unique_edges = [dict(t) for t in {tuple(d.items()) for d in edges}]
    return jsonify({"nodes": nodes, "edges": unique_edges})

if __name__ == '__main__':
    os.makedirs('wiki', exist_ok=True)
    os.makedirs('raw', exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
