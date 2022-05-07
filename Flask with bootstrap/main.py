from flask import Flask, render_template


app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')


# Code to run the Flask app
if __name__ == '__main__':
    for i in range(13000, 18000):
        try:
            app.run(debug=True, port=i)
            break
        except OSError as e:
            print(f"Port {i} not available")
