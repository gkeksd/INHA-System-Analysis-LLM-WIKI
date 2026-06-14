from flask import Flask, render_template, jsonify, request
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
    """
    지식 시각화 도구: 페이지 간 연관관계를 D3/Vis.js 그래프용 데이터로 변환
    """
    data = load_wiki_data()
    nodes = []
    edges = []
    for key, val in data.items():
        nodes.append({"id": val["id"], "label": val["title"]})
        for rel in val.get("related", []):
            rel_id = rel.lower().replace(" ", "_")
            edges.append({"from": val["id"], "to": rel_id})
    return jsonify({"nodes": nodes, "edges": edges})

if __name__ == '__main__':
    # 저장소 초기화 설정
    os.makedirs('wiki', exist_ok=True)
    os.makedirs('raw', exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
