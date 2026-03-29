from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Adam Novák", "age": 20, "nickname": "Adko", "fun_fact": "Vie žonglovať s troma jablkami naraz.", "image": "https://i.pravatar.cc/150?img=1"},
    {"id": 2, "name": "Barbora Kováčová", "age": 21, "nickname": "Barbi", "fun_fact": "Hovorí plynule štyrmi jazykmi vrátane japončiny.", "image": "https://i.pravatar.cc/150?img=2"},
    {"id": 3, "name": "Cyril Horváth", "age": 19, "nickname": "Cyco", "fun_fact": "Nikdy v živote nejedol pizzu s ananásom a je na to hrdý.", "image": "https://i.pravatar.cc/150?img=3"},
    {"id": 4, "name": "Dana Slobodová", "age": 22, "nickname": "Danka", "fun_fact": "Raz prečítala 5 kníh za jeden víkend.", "image": "https://i.pravatar.cc/150?img=4"},
    {"id": 5, "name": "Erik Blaho", "age": 20, "nickname": "Ero", "fun_fact": "Má doma kolekciu 200 rôznych klobúkov.", "image": "https://i.pravatar.cc/150?img=5"},
    {"id": 6, "name": "Filip Mináč", "age": 21, "nickname": "Filo", "fun_fact": "Dokáže spievať pieseň pozadu slovo po slove.", "image": "https://i.pravatar.cc/150?img=6"},
    {"id": 7, "name": "Gabriela Lukáčová", "age": 19, "nickname": "Gabi", "fun_fact": "Vyhrala regionálnu súťaž v skladaní origami.", "image": "https://i.pravatar.cc/150?img=7"},
    {"id": 8, "name": "Henrich Polák", "age": 23, "nickname": "Henky", "fun_fact": "Spal pod holým nebom 30 nocí za sebou.", "image": "https://i.pravatar.cc/150?img=8"},
    {"id": 9, "name": "Ivana Šimková", "age": 20, "nickname": "Ivi", "fun_fact": "Pozná naspamäť prvých 100 desatinných miest čísla pí.", "image": "https://i.pravatar.cc/150?img=9"},
    {"id": 10, "name": "Jakub Varga", "age": 21, "nickname": "Kubo", "fun_fact": "Postavil funkčný retro počítač z dielov z bazára.", "image": "https://i.pravatar.cc/150?img=10"}
]

@app.route("/")
def index():
    return "<h1>Vitaj v mojom prvom Flask API!</h1><p>Použi <a href='/api'>/api</a> pre zoznam študentov.</p>"

@app.route("/api")
def get_students():
    return jsonify(students)

@app.route("/api/student/<int:student_id>")
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        return jsonify(student)
    return jsonify({"error": "Študent nenájdený"}), 404

if __name__ == "__main__":
    app.run(debug=True)
