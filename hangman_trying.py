#taking input
word_given_og = input("Enter the word:")
word_given= word_given_og
x = 0
y = 0

fig1='''
                _______
		|     |
		|
		|
		|
		|
	      __|__   '''

fig2='''
                _______
		|     |
		|     O
		|
		|
		|
	      __|__   '''
fig3='''
                _______
		|     |
		|     O
		|     |
		|
		|
	      __|__   '''
fig4='''
                _______
		|     |
		|     O
		|     |
		|     |
		|
	      __|__   '''
fig5='''
                _______
		|     |
		|     O
		|    /|
		|     |
		|
	      __|__   '''
fig6='''
                _______
		|     |
		|     O
		|    /|\\
		|     |
		|
	      __|__   '''
fig7='''
                _______
		|     |
		|     O
		|    /|\\
		|     |
		|    /
	      __|__   '''
fig8='''
                _______
		|     |
		|     O
		|    /|\\
		|     |
		|    / \\
	      __|__   '''

wrong_figs=[fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8]

opponent_display_array=[]
# printing the question to second player
while(x < len(word_given)):
#without vowels
    if(word_given[x] == " "):
        print("/", end=' ')
        opponent_display_array.append("/")
    else:
        print("__", end=' ')
        opponent_display_array.append("__")
    x=x+1

#other player guessing
i=0
k=0
m=0
n=0
wrong_letters_guessed=["" for i in range(8)]
while(i<8):#len(word_given)):
    j=input("\n\nGuess a letter:")
    
    #if the opponent guesses wrong
    if j not in word_given:
        
        while(k<len(word_given)):
            print(opponent_display_array[k], end=' ')
            k += 1
        k=0

        print(wrong_figs[i])
        
        wrong_letters_guessed[i]=j
        print("\n WRONG GUESSED LETTERS :")
        print(wrong_letters_guessed)
        i += 1
    else:
#        right_ans_pos=word_given.find(j)
        
        while(n<len(word_given)):
            if(word_given[n]==j):
                opponent_display_array[n]=j
            n += 1
        n=0
        
        
#         print(right_ans_pos)
#        opponent_display_array[right_ans_pos]=j
#        word_given[right_ans_pos] = "0"
        
        while(m<len(word_given)):
            print(opponent_display_array[m], end=' ')
            m += 1
        m=0
        
        print(wrong_figs[i])
        
        print("\nGUESSED LETTERS:")
        print(wrong_letters_guessed)
        
        if "__" not in opponent_display_array:
            print("\nYOU WIN")
            break
    
    if(i==7):
        print("\nYOU LOST")
        