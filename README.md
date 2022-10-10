# AUTOMATIC SHORT ANSWER GRADING

<p align="center">
    <img width="800" src="https://user-images.githubusercontent.com/115498474/194944827-83490289-4e06-4fda-a187-a72e81ae0645.png">
</p>

## Abstract</b> 

 This study aims to create a application that automatically grades the short answers given to
a question with a referenced answer. The similarity between the answer given to the question
by the examinee and the reference answer decided by the instructor are calculated by different
language processing methods. Those methods are used to find the similarity values of the
reference answers set for a collection example questions and student answers given to the
questions which are marked as correct or incorrect before-hand and to create a dataset. After
that, this dataset is used to evaluate new answers. The similarity values of the new answer and
the reference answer is calculated and compared with the ones in the dataset, A model
predicts if the answer is correct or not by checking the correctness of the answers with the
similar similarity values in the dataset. Lastly, the answer is scored depending on its
probability of being correct, decided by the model.

## Sources

### Universel Sentence Encoder
 The Universal Sentence Encoder encodes text into high-dimensional vectors that can be
used for text classification, semantic similarity, clustering and other natural language tasks.
 The model is trained and optimized for greater-than-word length text, such as sentences,
phrases or short paragraphs. It is trained on a variety of data sources and a variety of tasks
with the aim of dynamically accommodating a wide variety of natural language understanding
tasks. The input is variable length English text and the output is a 512 dimensional vector.
The model is trained with a deep averaging network (DAN) encoder. In this project, it is used
for semantic similarity calculations.

### Elmo Module
 The Elmo Module computes contextualized word representations using character-based
word representations and bidirectional LSTMs.
 This module supports inputs both in the form of raw text strings or tokenized text strings.
The module outputs fixed embeddings at each LSTM layer, a learnable aggregation of the 3
layers, and a fixed mean-pooled vector representation of the input. In this project, it is used
for word embedding.

### Wikipedia2Vec
 Wikipedia2Vec is a tool used for obtaining embeddings (or vector representations) of words and entities 
(i.e., concepts that have corresponding pages in Wikipedia) from Wikipedia. It is developed and maintained 
by Studio Ousia. In this project, it is used to access pretrained word embadings to use as reference point 
for word similarity calculations. 


[1] Elmo Module https://tfhub.dev/google/elmo/2
[2] Universal Sentence Encoder https://tfhub.dev/google/universal-sentence-encoder/4
[3] Wikipedia2Vec Pre-trained Embedding
https://wikipedia2vec.github.io/wikipedia2vec/pretrained/
[4] Jupyter Notebook https://jupyter.org/

