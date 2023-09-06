from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/<string:page_name>')
def hello(page_name):
    return render_template(page_name)


@app.route('/')
# it means everytime you access this webserver, this decorator will work and return the function
def home():
    return render_template('index.html')


# this render_template will try to find the file name "templates"
'''

@app.route('/<username>/<int:post_id>')
def username(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)
# in this way you can show the message like "thank you for sending the email" with this app.route
'''


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
# those post or get to obtain the information from "submit form" on HTML


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'data not saved'
    else:
        return 'something went wrong'
