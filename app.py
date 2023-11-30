from flask import Flask, render_template, request
from untitled import rag_pipeline  

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        
        # Call your rag_pipeline function with the input text
        result = rag_pipeline(input_text)

        

        return render_template('result.html', data=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
