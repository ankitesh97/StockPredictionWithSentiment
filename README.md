# Stock price prediction using sentiment analysis

This comparative study aims to find the relation between the social popularity of a company and its stock price value

## Steps
[The Dataset](#the-dataset)  
[Baseline Model](#baseline-model)  
[Features For Without Sentiment](#features-for-without-sentiment)  
[Features For With Sentiment](#features-for-with-sentiment)  
[Features For With Sentiment And The Tweet Encoded](#features-for-with-sentiment-and-the-tweet- encoded)  
[Comparision](#comparision)

## The Dataset

* We have focused on only 1 company as the main aim is to find the relation between sentiment and the stock price
* We have used the stock prices of Google (GOOG) in the NASDAQ market
* The series that we monitored was 1 day long (9:30am-4pm EDT)
* The aim was to predict the stock price in the time interval of 2 mins
* The stock prices were scraped from yahoo finance
* For the sentiment analysis we took tweets related to google using the twitter's api.


## Baseline Model

The model that we used to predict the stock prices was stack many to one LSTM  
![LSTM]('https://github.com/ankitesh97/StockPredictionWithSentiment/lstm.png')


The model remained the same for the comparision purpose, only the input features were changed  

Loss : MSE  
Error: Mean Absolute Error  
Optimization: rmsprop  
Epochs: 500

## Features For Without Sentiment

For the 1st task we used the following Features
* Open Stock price  
* Low price
* High price
* Volume
* Running Max price
* Running Min price

The variable that was to be predcited was the closing price within that time span

Mae: 71


## Features For With Sentiment
Preprocessing  

Along with the previous features we added some features related to sentiment


The below image explains it all  

![architechture]('https://github.com/ankitesh97/StockPredictionWithSentiment/architechture.png')


Then we took the average of the positiveness, and the negativeness across the different tweets in a given time span

So two new features  
* positiveness
* negativeness


Total features - 8  
Mae: 38


## Features For With Sentiment And The Tweet Encoded

Along with the previous features, we encoded each tweet using a variation of the Word2Vec model(encodec in 50 dimension)

Again we took weighted averages of the tweets belonging to one time span

And now along with the previous 8 features we added these 50 features totalling upto 58 features

Mae: 5


## Comparision

The Mae curve  

![mae_curve]('https://github.com/ankitesh97/StockPredictionWithSentiment/saved_params/mae_plot.png')



## Conclusion

So the conclusion that we deduced, was that there is some relation between the popularity on the social media and the companie's stock price (This relation can be evaluated statistically using the various correlation coefficient)
