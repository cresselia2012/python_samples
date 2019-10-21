# sample_list.py

# リストを作る
Mylist = [ 1, 3, 5]

# 空で初期化
Mylist = []
#Mylist = list() も同じ

# 要素を追加
Mylist.append( 1 )
Mylist.append( 10 )
Mylist.append( 99 )

# リストの長さ
print(len(Mylist))

# 中身を表示
print(Mylist)

# 指定した要素にアクセス
print(Mylist[1])

# 最後尾の要素にアクセス
print(Mylist[-1])

# for文で各要素にアクセス
for x in Mylist:
    print(x)

# 検索, 値がリストに入っていれば True
print( 99 in Mylist )

# 削除
Mylist.remove( 99 )

# リスト内包表記
print([ i*2 for i in range(5)])
