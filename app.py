from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Student Performance Predictor</title>
<style>
body{font-family:Arial; background:#f0f4ff; text-align:center; padding:30px;}
.box{background:white; padding:20px; border-radius:10px; max-width:400px; margin:auto; box-shadow:0 4px 10px rgba(0,0,0,0.1);}
input{padding:10px; width:90%; margin:10px 0;}
button{padding:10px 20px; background:#4a6cf7; color:white; border:none; border-radius:5px; cursor:pointer;}
h2{color:#4a6cf7;}
</style>
</head>
<body>
<div class="box">
<h2>Student Result Predictor</h2>
<form method="post">
<input type="number" name="hours" placeholder="Study Hours per day" required>
<input type="number" name="attendance" placeholder="Attendance %" required>
<button type="submit">Predict</button>
</form>
{% if result %}
<h3>{{ result }}</h3>
{% endif %}
</div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            hours = float(request.form['hours'])
            attendance = float(request.form['attendance'])
            score = (hours * 5) + (attendance * 0.5)
            if score > 60:
                result = f"Pass Avuthav! Expected Score: {score:.1f}% 🎉"
            else:
                result = f"Konchem Kastapadali! Expected Score: {score:.1f}% 📚"
        except:
            result = "Correct values enter cheyyi"
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run()