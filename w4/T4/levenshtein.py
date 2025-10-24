import streamlit as st 

# build levenshtenin distance 
def levenshtein_distance(s , t) : 
    n , m = len(s) , len(t) 
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1) : 
        dp[i][0] = i 
    for j in range(m + 1) : 
        dp[0][j] = j 

    cost = 0 
    for i in range(1 , n + 1) :
        for j in range(1 , m + 1) : 
            if s[i - 1] == t[j - 1] : cost = 0 
            else : cost = 1 
            dp[i][j] = min(
                dp[i - 1] + 1 , # xoá 
                dp[i][j - 1] + 1 , # chèn 
                dp[i - 1][j - 1] + cost # thay thế 
        )
    return dp[n][m]

# read file 
def load_vocab(file_path) : 
    with open(file_path , 'r') as file : 
        lines = file.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words 

vocabs = load_vocab(file_path = '/Users/macos/AIO/module 1 /w4/T4/Solution/source/data/vocab.txt') 

# build by streamlit 
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

