from SentiAnalyzer import *
import pandas as pd

word_df = pd.read_csv('word.csv', header=None)
sentidata_df = pd.read_csv('sentidata.csv', header=None)

# DataFrame을 리스트로 변환
word = word_df.values.tolist()
sentidata = sentidata_df.values.tolist()

s = SentiAnalyzer()
# 1)
print('1)')
s.runAnalysis(sentidata, word, 10)
# 2)
print('2)')
s.runAnalysis(sentidata, word, 120)
# 3)
print('3)')
pos, neg, sent = s.runAnalysis(sentidata, word, 120)
print(pos)
print(neg)
print(sent)
