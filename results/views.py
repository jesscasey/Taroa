from flask import render_template, request
import app

@app.route("/results", methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        # Retrieve form data
        question = request.form.get("question")
        card_types = request.form.get("card_types")
        include_reversed_cards = request.form.get("include_reversed_cards")
        card_quantity = request.form.get("card_quantity")

        # Process form data here

        # Render results
        return render_template('tarot/results.html', 
                                question=question, 
                                card_types=card_types, 
                                include_reversed_cards=include_reversed_cards, 
                                card_quantity=card_quantity)
    return render_template('tarot/reading.html')
