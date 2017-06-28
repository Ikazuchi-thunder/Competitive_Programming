#ABC065

## A
やるだけ

## B
ループ終了条件だけ気をつける．  
終了チェックのために<img src="https://latex.codecogs.com/gif.latex?\mathcal{O}(N)" />かけてしまうと全部で<img src="https://latex.codecogs.com/gif.latex?\mathcal{O}(N^2)" />になりTLEする．

## C
高校数学

## D
costが<img src="https://latex.codecogs.com/gif.latex?\min(|x[a] - x[b]|, |y[a] - y[b]|)" />なので，x座標またはy座標でソートしたときに隣り合う街同士の橋しか使わない（全部使えうるとすると<img src="https://latex.codecogs.com/gif.latex?\mathcal{O}(N^2)" />，この方法で絞ると<img src="https://latex.codecogs.com/gif.latex?\mathcal{O}(N\log N)" />）．  
また，街がつながっているかどうかの判定や街どうしをつなぐ処理にかけていい時間は<img src="https://latex.codecogs.com/gif.latex?\mathcal{O}(\log N)" />までで，<img src="https://latex.codecogs.com/gif.latex?\mathcal{O}(N)" />かけると全体として<img src="https://latex.codecogs.com/gif.latex?\mathcal{O}(N^2)" />になって死ぬことに気をつける．
