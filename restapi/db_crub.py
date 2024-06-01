import sqlite3
from flask import Flask, jsonify, request, g

app = Flask(__name__)

DATABASE = 'database.db'

# เชื่อมต่อกับฐานข้อมูล
def connect_db():
    return sqlite3.connect(DATABASE)

# สร้างตารางในฐานข้อมูล
def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                done BOOLEAN NOT NULL
            )
        ''')
        db.commit()

# ขอเชื่อมต่อฐานข้อมูล
def get_db():
    if 'db' not in g:
        g.db = connect_db()
    return g.db

# ปิดการเชื่อมต่อกับฐานข้อมูลเมื่อเสร็จสิ้น
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()

# รายการงานทั้งหมด
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    db = get_db()
    cur = db.execute('SELECT id, title, description, done FROM tasks')
    tasks = [{'id': row[0], 'title': row[1], 'description': row[2], 'done': row[3]} for row in cur.fetchall()]
    return jsonify({'tasks': tasks})

# เพิ่มงานใหม่
@app.route('/api/tasks', methods=['POST'])
def add_task():
    db = get_db()
    db.execute('INSERT INTO tasks (title, description, done) VALUES (?, ?, ?)',
               [request.json['title'], request.json['description'], False])
    db.commit()
    return jsonify({'message': 'Task added successfully!'})

# ดูรายละเอียดของงาน
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    db = get_db()
    cur = db.execute('SELECT id, title, description, done FROM tasks WHERE id = ?', [task_id])
    task = cur.fetchone()
    if task is None:
        return jsonify({'error': 'Task not found!'}), 404
    return jsonify({'task': {'id': task[0], 'title': task[1], 'description': task[2], 'done': task[3]}})

# แก้ไขงาน
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    db = get_db()
    cur = db.execute('SELECT id, title, description, done FROM tasks WHERE id = ?', [task_id])
    task = cur.fetchone()
    if task is None:
        return jsonify({'error': 'Task not found!'}), 404
    db.execute('UPDATE tasks SET title = ?, description = ?, done = ? WHERE id = ?',
               [request.json.get('title', task[1]), request.json.get('description', task[2]), 
                request.json.get('done', task[3]), task_id])
    db.commit()
    return jsonify({'message': 'Task updated successfully!'})

# ลบงาน
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    db = get_db()
    cur = db.execute('SELECT id, title, description, done FROM tasks WHERE id = ?', [task_id])
    task = cur.fetchone()
    if task is None:
        return jsonify({'error': 'Task not found!'}), 404
    db.execute('DELETE FROM tasks WHERE id = ?', [task_id])
    db.commit()
    return jsonify({'message': 'Task deleted successfully!'})

if __name__ == '__main__':
     init_db()
     app.run(debug=True, port=6000)
