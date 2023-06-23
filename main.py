from flask import Flask, render_template, url_for

app = Flask(__name__)


data = {
    "invoice_number": 3488,
    "date": "21/06/2023",
    "customer": "Elon Musk",
    "address": "123 walls street, Townhall, USA",
    "contact": "+44 222345667",
    "total_due": 1200,
    "ordered_items": [
        {"name": "Artificial Intelligence", "description": "Standard",
            "price": 3500, "quantity": 2, "total_price": 7000},
        {"name": "Web Development", "description": "Advanced",
            "price": 3500, "quantity": 1, "total_price": 3500},
        {"name": "Blockchain", "description": "Basics",
            "price": 1500, "quantity": 3, "total_price": 4500},
        {"name": "Backend Design & Development", "description": "Professional",
            "price": 4500, "quantity": 2, "total_price": 9000},
        {"name": "Data Analytics", "description": "Standard",
            "price": 8000, "quantity": 1, "total_price": 8000}
    ],
    "sub_total": 32000,
    "tax": 1600,
    "discount": 700,
    "grand_total": 32900
}


@app.route("/")
def index():
    return render_template('index.html', context=data)


if __name__ == "__main__":
    app.run(debug=True)
