import streamlit as st

def load_vocab(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words

vocabs = load_vocab("vocab.txt")
print(vocabs)

def levenshtein_distance(token1, token2):
    distance = [[0]*(len(token2) + 1) for _ in range(len(token1) + 1)]
    
    for t1 in range(len(token1) + 1):
        distance[t1][0] = t1
    for t2 in range(len(token2) + 1):
        distance[0][t2] = t2
        
    a = 0
    b = 0
    c = 0
    
    for t1 in range(len(token1) + 1):
        for t2 in range(len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distance[t1][t2] = distance[t1 - 1][t2 - 1]
            else:
                a = distance[t1][t2 - 1]
                b = distance[t1 - 1][t2]
                c = distance[t1 - 1][t2 - 1]
                
                distance = min(min(a, b), c) + 1
                
    return distance[len(token1)][len(token2)]

def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')
    
    if st.button("Compute"):
        # compute levenshtein Distance
        leven_distances = dict()
        
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)
            
        # sorted by distance
        sorted_distances = dict(sorted(leven_distances.items(), key = lambda item: item[1]))
        correct_word = list(sorted_distances.key())[0]
        st.write('Correct Word: ', correct_word)
        
        col1, col2 = st.columns(2)
        col1.write('Vocabulary: ')
        col1.write(vocabs)
        
        col2.write('Distances: ')
        col2.write(sorted_distances)
        
if __name__ == "main":
    main()