from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    subject = data.get('subject')
    message = data.get('message')

    # Replace with your own email credentials and SMTP server details
    smtp_server = 'umangc.2000@gmail.com'
    smtp_port = 587
    smtp_username = 'umang'
    smtp_password = 'chaurasia'
    from_email = 'chaurasiaumang24@gmail.com'
    to_email = 'umangc.2000@gmail.com'

    try:
        msg = MIMEText(f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())

        return jsonify({'message': 'Email sent successfully!'}), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
