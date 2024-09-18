from flask import Flask, render_template, request
import joblib
import numpy as np

popular_df = joblib.load(open('popular.jlb', 'rb'))
pt = joblib.load(open('pt.jlb', 'rb'))
similar_score = joblib.load(open('similar_score.jlb', 'rb'))
Books = joblib.load(open('Books.jlb', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_rating'].values),
                           rating=list(popular_df['mean_rating'].values))

@app.route('/recommendation')
def recommendation_ui():  # Fixed the typo here
    return render_template('recommendation.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    
    # Ensure user_input is valid
    if not user_input or not user_input.strip():
        return render_template('recommendation.html', data=[], message="Please enter a valid book name.")

    # Convert both user_input and pt.index to lowercase to avoid case sensitivity issues
    book_name = user_input.strip().lower()
    pt.index = pt.index.str.strip().str.lower()

    # Clean book titles in Books dataframe and drop duplicates
    Books['Book-Title'] = Books['Book-Title'].str.strip().str.lower()
    Books.drop_duplicates(subset='Book-Title', inplace=True)

    # Check if the book exists in the index
    if book_name not in pt.index:
        print(f"'{book_name}' not found in the book list.")
        return render_template('recommendation.html', data=[], message=f"No recommendations found for '{book_name}'.")

    # Fetch the index
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similar_score[index])), key=lambda x: x[1], reverse=True)[1:8]

    data = []
    for i in similar_items:
        item = []
        temp_df = Books[Books['Book-Title'] == pt.index[i[0]]]

        if not temp_df.empty:
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Author')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Image-URL-M')['Image-URL-M'].values))
            data.append(item)

    return render_template('recommendation.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
