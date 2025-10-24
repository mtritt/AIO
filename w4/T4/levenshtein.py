import streamlit as st 

def levenshtein_distance(token_1 , token_2) : 
    distances = [[0] * (len(token_2) + 1) for i in range(len(token_1) + 1)]

    for i in range(len(token_1) + 1) : 
        distances[i][0] = i 
    for j in range(len(token_2) + 1) : 
        distances[0][j] = j 
    
    cost = 0 
    
    for i in range(1 , len(token_2) + 1) :
        for j in range(1 , len(token_1) + 1) : 
            if token_1[i - 1] == token_2[j - 1] : 
                cost = 0 
            else : 
                cost = 1
            distances[i][j] = min(
                distances[i - 1][j] + 1 , # delete 
                distances[i][j - 1] + 1, # insert 
                distances[i - 1][j - 1] + cost # replace hoặc match 
            ) 
    return distances[len(token_1)][len(token_2)]

def load_vocab(file_path) : 
    with open(file_path , 'r') as file : 
        lines = file.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words 

vocabs = load_vocab(file_path = '/Users/macos/AIO/module 1 /w4/T4/Solution/source/data/vocab.txt') 

st.title('Word Correction')
word = st.text_input('Enter your word :')

if st.button('Compute') : 
    distances = {}
    for vocab in vocabs : 
        distance = levenshtein_distance(word , vocab)
        distances[vocab] = distance
    # sắp xếp theo số lần cần để chuyển từ word -> vocab 
    sorted_distances = sorted(distances.items() , key = lambda item : item[1]) 
    correct_word = sorted_distances[0][0]
    st.write('Correct :' , correct_word)

