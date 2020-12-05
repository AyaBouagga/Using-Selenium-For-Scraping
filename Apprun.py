import csv
from Tweets.tweet import Tweet, Reply


def get_accounts(filename):
#''' Get the account to scrap fom list file'''

    accounts = []
    accounts_Name = []

    with open(filename, mode='r', encoding='utf-8') as accounts_file:
        for acc in accounts_file:
            accounts.append(acc.split()[0])
            accounts_Name.append(acc.split()[1])
    return accounts, accounts_Name

accounts, accountsNames = get_accounts("List.txt")
length = len(accountsNames)

j = 0
while j < length:

    ACCOUNT = accounts[j]
    tw = Tweet(ACCOUNT)

    length, Alltweets = tw.tweets_split()
    i = 0
    FileName = accountsNames[j] + ".csv"


    with open(FileName, 'w', newline='') as file:
        fieldnames = ['Tweet', 'Replies']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()


        k=0
        numbertweetwithrep = 0
        while k <= len(Alltweets):
            rep = Reply(Alltweets[k])
            tweet_data, replies = rep.tweets_replies()
            if replies == "":
                numbertweetwithrep = numbertweetwithrep+1

            else:
                print(tweet_data)
                print(replies)



            k = k + 1


    j = j + 1
