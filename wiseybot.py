# -*- coding: utf-8 -*-

import random
import tweepy

CONSUMERKEY = "YOUR CONSUMER KEY"
CONSUMERSECRET = "YOUR CONSUMER SECRET"
ACCESTOKEN = "YOUR ACCES TOKEN"
ACCESTOKENSECRET = "YOUR ACCES TOKEN SECRET"

auth = tweepy.OAuthHandler(CONSUMERKEY, CONSUMERSECRET)
auth.set_access_token(ACCESTOKEN, ACCESTOKENSECRET)
api = tweepy.API(auth)
user = api.me()

def retweet():
    n = 0
    for tweet in api.mentions_timeline():
        try:
            tweet.retweet()
            n += 1
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    print("retweeted", n ,"Tweets.")

def get_quote():
    quotes = ["The price must be paid and the process followed. You always reap what you sow; there's no shortcut.", "But man is not made for defeat. A man can be destroyed but not defeated.", "There is nothing permanent except change.", "You cannot shake hands with a clenched fist.", "Learning never exhausts the mind.", "There is no charm equal to tenderness of heart.", "Independence is happiness.", "The supreme art of war is to subdue the enemy without fighting.", "Happiness can exist only in acceptance.", "There is only one corner of the universe you can be certain of improving, and that's your own self.", "Honesty is the first chapter in the book of wisdom.", "The best preparation for tomorrow is doing your best today.", "Change your life today. Don't gamble on the future, act now, without delay.", "Not all those who wander are lost.", "Whoever is happy will make others happy too.", "A leader is one who knows the way, goes the way, and shows the way.", "Very little is needed to make a happy life; it is all within yourself, in your way of thinking.", "The secret of getting ahead is getting started.", "Wise men speak because they have something to say; Fools because they have to say something.", "When we are no longer able to change a situation - we are challenged to change ourselves.", "All our dreams can come true, if we have the courage to pursue them.", "The only true wisdom is in knowing you know nothing.", "As we express our gratitude, we must never forget that the highest appreciation is not to utter words, but to live by them.", "Believe you can and you're halfway there.", "The future belongs to those who believe in the beauty of their dreams.", "Success is not final, failure is not fatal: it is the courage to continue that counts.", "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.", "Don't judge each day by the harvest you reap but by the seeds that you plant.", "Act as if what you do makes a difference. It does.", "Never bend your head. Always hold it high. Look the world straight in the eye.", "What you get by achieving your goals is not as important as what you become by achieving your goals.", "It is our attitude at the beginning of a difficult task which, more than anything else, will affect its successful outcome.", "Life is like riding a bicycle. To keep your balance, you must keep moving.", "Limit your 'always' and your 'nevers.'", "You are never too old to set another goal or to dream a new dream.", "You do not find the happy life. You make it.", "Sometimes you will never know the value of a moment, until it becomes a memory.", "You must do the things you think you cannot do.", "It is never too late to be what you might have been.", "You get what you give.", "Be the change that you wish to see in the world.", "Let us make our future now, and let us make our dreams tomorrow's reality.", "Don't wait. The time will never be just right.", "If you look at what you have in life, you'll always have more.", "Life is a series of baby steps.", "What comes easy won’t last long, and what lasts long won’t come easy.", "The best time for new beginnings is now.", "One day or day one. It's your decision.", "Those who dare to fail miserably can achieve greatly.", "Challenges are what make life interesting and overcoming them is what makes life meaningful.", "Never let the fear of striking out keep you from playing the game.", "Life is trying things to see if they work.", "You will face many defeats in life, but never let yourself be defeated.", "You miss 100 percent of the shots you don't take."]
    quote = quotes[random.randint(0,len(quotes))]
    user_tweets = api.user_timeline(count=1000)
    tweeted_quotes = []
    contador = 1

    for tweet in user_tweets:
        tweeted_quotes.append(tweet.text)

    while quote in tweeted_quotes:
        print(contador)
        contador += 1
        print("This quote has already been tweeted:", quote)
        quote = quotes[random.randint(0,len(quotes))]
        if contador > len(quotes):
            print("You have reached the quotes limit")
            break


    print("Bot would finally tweet:", quote)
    tweet = quote

    return tweet


def tweet_quote():
    tweet = get_quote()
    api.update_status(tweet)
    print("FUNCIONA")

def follow_back():
    followers = api.followers()
    friends = api.friends()

    for follower in followers:
        try:
            api.create_friendship(follower.id)
            print("Followed:", follower.name)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def main():
    retweet()
    follow_back()
    tweet_quote()


main()