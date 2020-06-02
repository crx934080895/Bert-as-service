from bert_serving.client import BertClient

bc = BertClient(ip="localhost")
dic = {}
word_list = ["hello", "good", "nice", "dog", "fish"]
for i in word_list:
    result = bc.encode([i], show_tokens=True)
    dic[i] = result[0][0][1]

