from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/user', methods=['GET', 'POST'])
def user():
if request.method == 'POST':
user_message = request.form['message']
# Handle the user message here (like storing or processing it)
response = f"Received your message: {user_message}. Admin will reply soon."
return render_template('user.html', response=response)
return render_template('user.html')
@app.route('/admin', methods=['GET', 'POST'])
def admin():
if request.method == 'POST':
admin_message = request.form['message']
# Handle the admin's message here (like storing or processing it)
response = f"Received admin's message: {admin_message}. Reply sent to the user."
return render_template('admin.html', response=response)
return render_template('admin.html')
if __name__ == '__main__':
app.run(debug=True)