
from flask import Flask,request,jsonify
from database import get_db_connection
from datetime import datetime
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
@app.route("/api/tickets",methods=['GET'])
def get_tickets():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT *  FROM tickets ORDER BY created_at DESC")
    rows=cursor.fetchall()
    conn.commit()
    conn.close()
    tickets=[dict(row) for row in rows]
    return jsonify(tickets),200

@app.route("/api/tickets",methods=["POST"])
def create_ticket():
    data=request.get_json()
    title=data.get("title")
    description=data.get("description")
    priority=data.get("priority")
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO tickets(title,description,priority,created_at) VALUES(?,?,?,CURRENT_TIMESTAMP);"
                   ,(title,description,priority))
    conn.commit()
    conn.close()
    return jsonify({"message":"ticket created successfully"}),201

@app.route("/api/tickets/<int:ticket_id>",methods=['GET'])
def create_tickets(ticket_id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tickets WHERE id=?;",(ticket_id,))
    rows=cursor.fetchone()
    conn.commit()
    conn.close()
    tickets=[dict(rows)]
    return jsonify(tickets),200

@app.route("/api/tickets/<int:ticket_id>", methods=["PUT"])
def update_ticket(ticket_id):
    data=request.get_json()
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tickets WHERE id=?;",(ticket_id,))
    ticket=cursor.fetchone()
    title=data.get("title",ticket["title"])
    description=data.get("description",ticket["description"])
    priority=data.get("priority",ticket["priority"])
    cursor.execute("UPDATE tickets SET title=?,description=?,priority=? WHERE id=?;",(title,description,priority,ticket_id))
    conn.commit()
    conn.close()
    return jsonify({"message":"ticket created successfully"}),200

@app.route("/api/tickets/<int:ticket_id>",methods=["DELETE"])
def delete_ticket(ticket_id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tickets WHERE id=?;",(ticket_id,))
    ticket=cursor.fetchone()
    cursor.execute("DELETE FROM tickets WHERE id=?;",(ticket_id,))
    conn.commit()
    conn.close()
    return jsonify({"message":"deleted successfully"}),200

if __name__=="__main__":
    app.run(debug=True,port=5000)
