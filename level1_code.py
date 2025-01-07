import csv
import random
import enchant


def get_words():
 with open('wordlist.csv', newline='') as csvfile:
    
    wordlist=[]
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #print(spamreader)
    for i in spamreader:
    	#print(i)
    	if ('-' in i[0]) or ("'" in i[0]):
            continue
    	wordlist.append(i[0].lower())
    #print(wordlist)
    
    wordlist.sort()    
    #print("sorted: ",wordlist)
    
    
    file1=open("wordlist.txt","w")

    file1.write(str(wordlist))
 return wordlist


def get_start_fixed_list(wordlist,letter):
   l=[i for i in wordlist if i[0]==letter]
   return l

def get_end_fixed_list(wordlist,letter):
   l=[i for i in wordlist if i[-1]==letter]
   return l

def get_missing_letters_list(wordlist,missing_count):
   l=[]
   letter_list=[ ]
   for i in range(missing_count):
      letter=chr(random.randint(0,25)+97)
      while letter in letter_list:
         letter=chr(random.randint(0,25)+97)
      letter_list.append(letter)
   
   print("MISSING LETTERS: ",letter_list)

   for i in wordlist:
      add=True
      for j in letter_list:
         if j in i:
            add=False
            break
      if add:
         l.append(i)
   return l
      

def calculate_heuristic(word,used_words,current_points):
   heuristic=0
   #for calculating heuristic using length of word
   heuristic+=15-len(word)

   #for calculating heuristic based on repetition of words
   if word in used_words:
      heuristic+=2
   #based on current points
   heuristic+=(30-current_points)

   return heuristic


def get_top_words(word_list,no_of_words,used_word,current_points):
   word_heuristics={}
   top_words=[]

   for i in word_list:
      word_heuristics[i]=calculate_heuristic(i,used_words,current_points)
   
   #print(word_heuristics)

   val=list(word_heuristics.values())
   key=list(word_heuristics.keys())
   i=0
   while i<no_of_words:   
      mini=min(val)
      freq=val.count(mini)
      for j in range(freq):

         if (len(top_words)==no_of_words):
            return top_words
         
         min_word=key[val.index(mini)]
         top_words.append(min_word)
         key.pop(val.index(mini))
         val.pop(val.index(mini))
         i+=1
   return top_words
   

def round1(used_words,user_used_words,lifelines,d):
   letter=chr(random.randint(97,122))
   print("\nALL THE WORDS FORMED SHOULD START WITH THE LETTER : ",letter)

   user_life=30
   ai_life=30

   ##user turn
   ###retrieve from pygame
   while ai_life>0 and user_life>0:
      print("USER LIFE: ",user_life,"\n ai_life: ",ai_life)
      #user_word=input("ENTER WORD: ")
      user_word=input_text
      print(d.check(user_word))
      print("USER USED WORDS: ",user_used_words,"USED_WORDS: ",used_words)
      if (user_word.startswith(letter) and user_word not in user_used_words and user_word not in used_words and d.check(user_word)):
         user_used_words.append(user_word)
         '''
      elif (user_word.startswith(letter) and user_word not in user_used_words and user_word not in used_words and not d.check(user_word)):
         while (user_word.startswith(letter) and user_word not in user_used_words and user_word not in used_words and not d.check(user_word) and lifelines>0):
            print("\nYOU HAVE ENTERED A WORD THAT GO AGAINST THE CONDITION SPECIFIED! TRY AGAIN POTTER!!")
            user_word=input("ENTER WORD: ")
            print(d.check(user_word))
            lifelines-=1
         if lifelines==0:
            print("\nYOU LOST POTTER!!!!!!!")
         else:
            user_used_words.append(user_word)
            '''
      elif (not (user_word.startswith(letter)) or (user_word in user_used_words or user_word in used_words) or not (d.check(user_word)) and lifelines>0):
         while (not (user_word.startswith(letter)) or  (user_word in user_used_words or user_word in used_words) or not (d.check(user_word)) and lifelines>0):
            print("\nYOU HAVE ENTERED A WORD THAT GO AGAINST THE CONDITION SPECIFIED! TRY AGAIN POTTER!!")
            lifelines-=1
            #user_word=input("ENTER WORD: ")
            #user_word=input_text
            print(d.check(user_word))
         if lifelines==0:
            print("\nYOU LOST POTTER!!!!!!!")
         else:
            user_used_words.append(user_word)

      

      if ai_life<=0 or lifelines<=0:
         break

      ai_life-=len(user_word)
   
      ##AI turn
      start_word_list=get_start_fixed_list(wordlist,letter)
      start_top_words=get_top_words(start_word_list,10,used_words,(30-user_life))
      reply_word=start_top_words[random.randint(0,len(start_top_words)-1)]

      while reply_word in used_words or reply_word in user_used_words:
         reply_word=start_top_words[random.randint(0,len(start_top_words)-1)]
      print("AI: ",reply_word)
      user_life-=len(reply_word)
      used_words.append(reply_word)


   print("\nUSER LIFE: ",user_life,"\nAI_LIFE: ",ai_life)
   if (user_life<=0):
      print("YOU GOT DEFEATED BY BELLATRIX!!")
      print("NOW GO THROUGH YOUR BOOKS AS MAY NEED MORE WORDS TO BEAT THE NEXT ONE!")

   elif (ai_life<=0):
      print("WELL DONE POTTER!")
      print("YOU MAY HAVE DEFEATED BELLATRIX BUT YOU WILL DEFINITELY BE DEFEATED BY THE NEXT ONE!!")
      print("WAITING TO SEE YOU GET DEFEATED POTTER!")
   
   else:
      print("IN MY PLACE, YOU HAVE TO OBEY MY RULES!")











      
   





#MAIN
d = enchant.Dict("en_US")
wordlist=get_words()
used_words=[]
user_used_words=[]

max_len=0
max_word=""
for i in wordlist:
   if len(i)>max_len:
      max_len=len(i)
      max_word=i

#print("MAX LENGTH: ",max_len," word: ",max_word)

letter=chr(random.randint(0,25)+97)
#print("start fixed with ",letter," : ",get_start_fixed_list(wordlist,letter))
#print("end fixed with ",letter," : ",get_end_fixed_list(wordlist,letter))

missing_count=random.randint(1,3)

      
temp=get_missing_letters_list(wordlist,missing_count)
#print(get_top_words(temp,5,[],25))

round1(used_words,user_used_words,3,d)