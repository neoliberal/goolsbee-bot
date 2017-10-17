#!/usr/bin/python
import praw
import random

reddit = praw.Reddit('Goolsbee')
responses = open("Replies.txt").read().split("\n")
commented = open("replied_comments.txt").read().split()

def clean_text(s):
    punc_list = [".", ";", ":", "!", "?", "/", "\\", ",", "#", "@", "$", "&", ")", "(", "'", ">", "[", "]"]
    new_s = ''
    for i in s:
        if i not in punc_list:
            new_s += i
        else:
            new_s += ' '
    return new_s.lower()

def log_comment(comment):
    with open('replied_comments.txt', 'a') as file:
        file.write(str(comment))
        file.write(' ')

def write_comment(i, comment):
    response = responses[i]
    log_comment(comment)
    if(random.randint(1,11)==1):
        comment.reply(response)
        print('Comment written')
    else:
        print('Comment passed')
    

while True:
    for comment in reddit.subreddit('neoliberal').stream.comments():
        if not comment.author == "Goolsbee_Bot":
                text = comment.body
                text = clean_text(text)
                text = text.split()
                if str(comment) not in commented:
            
                    if 'bitcoin' in text:
                        write_comment(16, comment)

                    elif 'anime' in text:
                        write_comment(5, comment)
                        
                    elif 'democracy' in text:
                        write_comment(27, comment)
                    
                    elif 'stupid' in text:
                        write_comment(26, comment)
                        
                    elif 'tax' in text and 'cuts' in text:
                        write_comment(20, comment)

                    elif 'cut' in text and 'taxes' in text:
                        write_comment(20, comment)

                    elif 'cutting' in text and 'taxes' in text:
                        write_comment(20, comment)

                    elif 'tea' in text and 'party' in text:
                        write_comment(20, comment)

                    elif 'gold' in text and 'standard' in text:
                        write_comment(0, comment)

                    elif 'bernie' in text and 'would' in text and 'have' in text and 'won':
                        write_comment(25, comment)
                        
                    elif 'coal' in text and 'miners' in text:
                        write_comment(2, comment)
                
                    elif 'goolsbee' in text:
                        rint = random.randint(0,24)
                        write_comment(rint, comment)
