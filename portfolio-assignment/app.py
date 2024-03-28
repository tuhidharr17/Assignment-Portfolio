from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def AboutMe():
    return render_template('aboutme.html')
#creating end points
@app.route('/education')
def education():
    return render_template('education.html')
@app.route('/skills')
def skills():
    return render_template('skills.html')
@app.route('/projects')
def projects():
    return render_template('projects.html')
@app.route('/activity')
def activity():
    return render_template('activity.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
if __name__== "_main_":
    app.run(debug=True,port=5000)