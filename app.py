from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Profile Page
@app.route("/profile")
def profile():
    return render_template("profile.html")


# Career Recommendation Page
@app.route("/recommendation")
def recommendation():
    return render_template("recommendation.html")


# Resume Page
@app.route("/resume")
def resume():
    return render_template("resume.html")


# Resume Analysis
@app.route("/analyse", methods=["POST"])
def analyse():

    file = request.files["resume"]

    if file.filename == "":
        return render_template(
            "resume.html",
            message="Please select a file"
        )


    skills = [
        "Python",
        "SQL",
        "HTML",
        "CSS",
        "Flask"
    ]


    recommendations = [
        "Python Developer",
        "Backend Developer",
        "Software Engineer"
    ]


    score = 75


    # Save result in database
    connection = sqlite3.connect("career.db")
    cursor = connection.cursor()


    cursor.execute("""
        INSERT INTO resume_results
        (student_name, detected_skills, score)
        VALUES (?, ?, ?)
    """,
    (
        "Pravalika",
        ", ".join(skills),
        score
    ))


    connection.commit()
    connection.close()


    return render_template(
        "resume.html",
        message="Resume analysed successfully ✅",
        skills=skills,
        recommendations=recommendations,
        score=score
    )



# Results Page
@app.route("/results")
def results():

    connection = sqlite3.connect("career.db")
    cursor = connection.cursor()


    cursor.execute("""
        SELECT student_name, detected_skills, score
        FROM resume_results
    """)


    results = cursor.fetchall()


    connection.close()


    return render_template(
        "results.html",
        results=results
    )



# Dashboard Page
@app.route("/dashboard")
def dashboard():

    connection = sqlite3.connect("career.db")
    cursor = connection.cursor()


    cursor.execute("""
        SELECT student_name, detected_skills, score
        FROM resume_results
        ORDER BY id DESC
        LIMIT 1
    """)


    result = cursor.fetchone()


    connection.close()


    careers = [
        "Python Developer",
        "Backend Developer",
        "Software Engineer"
    ]


    return render_template(
        "dashboard.html",
        result=result,
        careers=careers
    )



if __name__ == "__main__":
    app.run(debug=True)