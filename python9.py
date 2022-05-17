# w・・・新規書き込み
# a・・・つい書き込み
# r・・・読み込み
# x・・・ファイルが存在しない場合、新規書き込み
# r+など+の機能・・・こちらについては+がほかの機能を果たす(例 r+・・・本来はないwrite機能が使える w+・・・本来は使えないreadの機能が使えるようになる)
f = open('myfile.txt', 'a+')

f.write('おはようおはよう\n')
f.write('こんにちはこんにちは\n')
f.write('こんばんはこんばんは\n')

s = f.read()
print(s)

# f2 = open()
# f2 = open('myfile.txt', 'r')
# f2.read()

# f.write('おはよう2     おはよう2\n')
# f.write('こんにちは2     こんにちは\n')
# f.write('こんばんは2     こんばんは\n')

# s = f.read()
# print(s)

f.close()
# f2.close()