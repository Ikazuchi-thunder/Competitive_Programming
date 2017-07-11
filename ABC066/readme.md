# ABC066

## A
やるだけ

## B
文字列の長さを`2n`として，`S[0:n - i] == S[n - i: 2 * (n - i)]`をチェックすればよい．

## C
実験してみると，`n`と偶奇が一致する値を降順に並べた後，偶奇が異なる値を昇順に並べれば良いことがわかる．

## D
`n`種類の数字を`n+1`個並べているので，鳩の巣原理から同じ数字`i`が1組だけ存在する．  
`i`のうち，左側のものよりも左にある数字の集合を`A`，右側のものよりも右にある数字の集合を`B`とする．  
このとき，（長さ3の部分列について考えるとき）`A, A, i`，`A, i, B`，`i, B, B`という数字のとり方をした場合，部分列の重複が発生する．  
たとえば，`2 1 1 3`に対して`2 1`，`1 3`，`2 1 3`やが重複している．  
したがって長さ`k`の部分列に対して<img src="https://latex.codecogs.com/gif.latex?_{n+1}C_{k}-_{right+left}C_{k-1}" />を求めれば良い．

ところで，この問題では組み合わせ関数の計算も問題になる．  
<img src="https://latex.codecogs.com/gif.latex?_nC_r=\frac{n!}{r!(n-r)!}" />として計算するが，<img src="https://latex.codecogs.com/gif.latex?n\le10^{5}" />という制約のもとでは階乗の数字が非常に大きくなるため<img src="https://latex.codecogs.com/gif.latex?10^9+7" />の剰余類で考えることが必要である．  
剰余類では通常の除算を求めることができないため，フェルマーの小定理<img src="https://latex.codecogs.com/gif.latex?k^{n-1}\equiv\,1\,(mod~n)" />すなわち<img src="https://latex.codecogs.com/gif.latex?k^{-1}\equiv\,k^{n-2}\,(mod~n)" />を用いて逆元を求める必要がある．  
さらに，この組み合わせを直接求めるには<img src="https://latex.codecogs.com/gif.latex?\mathcal{O}(n)" />かかるため，各`k`に対して直接求めると<img src="https://latex.codecogs.com/gif.latex?\mathcal{O}(n^2)" />かかることになりTLEする．  
それを回避するために，事前に動的計画法を用いて<img src="https://latex.codecogs.com/gif.latex?n!" />および<img src="https://latex.codecogs.com/gif.latex?n!^{-1}" />を計算しておかなければならない．
