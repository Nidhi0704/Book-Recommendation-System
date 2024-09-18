# Book-Recommendation-System
A Flask-based Book Recommendation System using a dataset of top 50 books, combining content-based and collaborative filtering for personalized recommendations based on user preferences and ratings.

Book Recommendation System
Overview
This is a Book Recommendation System that suggests books based on a dataset of the top 50 popular books. When a user provides a book, the system recommends 7 similar books, enhancing the user's experience by delivering tailored book suggestions.

The system combines machine learning algorithms like Collaborative Filtering with EDA (Exploratory Data Analysis) and various data preprocessing techniques. It is built using Flask for the web interface and runs entirely on a Python-based backend.

Features
Top 50 Popular Books: Displays a curated list of 50 popular books.
Book Suggestions: Provides 7 similar book recommendations based on the user's input.
Machine Learning: Utilizes collaborative filtering to suggest books.
Flask Web Application: A simple and interactive web interface for book recommendations.
Key Components
1. Machine Learning:
Collaborative Filtering: Used to recommend books based on user preferences and similarity between books.
Content-Based Filtering: Recommends books based on the features of the input book.
2. EDA (Exploratory Data Analysis):
Analyzed and visualized the book dataset to extract meaningful insights and patterns.
3. Data Preprocessing:
Cleaned and prepared the dataset by handling missing values, transforming data types, and normalizing features for the machine learning model.
4. Flask Application:
Built a web interface using Flask where users can input their preferred book and receive personalized recommendations.
Dataset
The dataset consists of information about the top 50 books, including:
Title
Author
Genre
Ratings
User reviews
Book features
This dataset was cleaned and preprocessed before feeding it into the recommendation model.

Usage
Enter the name of a book in the input field.
The system will return 7 similar books based on the input.
Technologies Used
Python
Flask
Pandas
NumPy
Scikit-learn
Collaborative Filtering
Content-Based Filtering
EDA: Data analysis and visualization tools (Matplotlib, Seaborn)
Future Enhancements
Implement user-based collaborative filtering for more personalized recommendations.
Expand the dataset with more books and features.
Add user reviews and ratings for better recommendations.
