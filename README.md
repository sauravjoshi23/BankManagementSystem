### Steps
- File Processing : .txt files in Train_docs and Train_tags were not of the same name hence file processing had to be done so that their data could be mapped for training purpose. Similarly for Test_docs.
- Imported important libraries.
- Added all the file data into a dataframe so that applying pandas and numpy operation would make the task comparitively easier.
- Data Analysis on tags data : Frequency of tag, max number of tags, min number of tags, average number of tags, plotted the countplot, a wordcloud to analyse the tag data.
- Text Preprocessing : This is particularly performed on Train_docs which contains the body. Lowering of text, Removing punctuations, Lemmatizing words and removing stop words.
- Exploratory Data Analysis : Applying LDA to get the top words/top topics.
- Data Preparation : Applying MultiLabelBinarizer on tag data column as it is Multi label text classification problem. Applying TFIDF vectorizer on body data column and not CountVectorizer as TFIDF normalizes the count and gives better result.
- Model : DummyClassifier, MultinomialNB, LinearSVC, Perceptron, PassiveAggressiveClassifier. 
- Result : Test_docs contained body data for which tags had to be predicted. Hence, a new directory was made Test_tags to store the answers predicted by the model.



