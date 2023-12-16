from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/tickets/<filename>')
def get_ticket_image(filename):
    fileindex = filename[1:5]
    path = f'savedImg/{fileindex}.png'
    return send_file(path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9900, debug=True) 
    