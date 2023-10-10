import os
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def handler():
    print("helloworld: received a request")
    try:
        result = subprocess.check_output(['/bin/sh', 'script.sh'], stderr=subprocess.STDOUT, universal_newlines=True)
        return result, 200
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")
        return "Internal Server Error", 500

if __name__ == '__main__':
    print("helloworld: starting server...")

    port = os.getenv('PORT', '8081')
    app.run(host='0.0.0.0', port=port)