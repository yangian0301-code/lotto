from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():

    html_doc = """
    <div class="balls">
        <span class="ball ball-orange">07</span>
        <span class="ball ball-orange">22</span>
        <span class="ball ball-orange">27</span>
        <span class="ball ball-orange">35</span>
        <span class="ball ball-orange">43</span>
        <span class="ball ball-orange">48</span>
        <span class="ball ball-red">45</span>
    </div>
    """

    soup = BeautifulSoup(html_doc, "html.parser")

    numbers = [
        x.text
        for x in soup.find_all(
            "span",
            class_="ball ball-orange"
        )
    ]

    special = soup.find(
        "span",
        class_="ball ball-red"
    ).text

    return f"""
    樂透號碼：{' '.join(numbers)}
    <br>
    特別號：{special}
    """

if __name__ == "__main__":
    app.run()
