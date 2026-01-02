from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    # -------- Option 1: Casual & Fun --------
    {
        "question": "What is my favourite food?",
        "options": ["Biriyani", "Dosa", "Pizza", "Burger"],
        "answer": "Biriyani"
    },
    {
        "question": "Tea or Coffee – what do I like more?",
        "options": ["Tea", "Coffee", "Both", "None"],
        "answer": "Tea"
    },
    {
        "question": "Am I an early bird or night owl?",
        "options": ["Early bird", "Night owl", "Both", "None"],
        "answer": "Night owl"
    },
    {
        "question": "My favourite movie type?",
        "options": ["Action", "Romance", "Comedy", "Horror"],
        "answer": "Romance"
    },

    # -------- Option 2: Best Friend Test --------
    {
        "question": "Who is my best friend?",
        "options": ["Arun", "Karthi", "Mani", "You 😎"],
        "answer": "You 😎"
    },
    {
        "question": "What makes me angry fast?",
        "options": ["Lies", "Noise", "Waiting", "Nothing"],
        "answer": "Lies"
    },
    {
        "question": "What do I do when I am stressed?",
        "options": ["Sleep", "Listen to music", "Talk to friends", "Stay silent"],
        "answer": "Listen to music"
    },
    {
        "question": "What kind of friend am I?",
        "options": ["Funny", "Caring", "Silent", "All of these"],
        "answer": "All of these"
    },

    # -------- Option 3: College / Youth Style --------
    {
        "question": "My favourite time pass?",
        "options": ["Mobile", "Movies", "Music", "Sleep"],
        "answer": "Music"
    },
    {
        "question": "Which bike do I like most?",
        "options": ["R15", "RS200", "Duke", "Pulsar"],
        "answer": "RS200"
    },
    {
        "question": "What motivates me the most?",
        "options": ["Money", "Family", "Friends", "Dream"],
        "answer": "Dream"
    }
]
@app.route("/", methods=["GET", "POST"])
def quiz():
    score = 0
    if request.method == "POST":
        for i in range(len(questions)):
            user_ans = request.form.get(f"q{i}")
            if user_ans == questions[i]["answer"]:
                score += 1
        return render_template("result.html", score=score)

    return render_template("quiz.html", questions=questions)
if __name__ == "__main__":
    app.run(debug=True)