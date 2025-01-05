# olympicコマンド
[![test](https://github.com/iuu1003/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/iuu1003/mypkg/actions/workflows/test.yml)  
オリンピックが開催される年を表示させます.

## 概要
- このプログラムは、夏季および冬季オリンピックが開催される年を表示します.

- オリンピックが初めて開催された1896年からスタートします.

## 使い方
実行方法の例  
`ros2 run mypkg olympic`  
別の端末で以下を実行  
`ros2 topic echo /countup`

実行結果の例
```
data: 1988
---
data: 1990
---
data: 1992
---
data: 1994
---
data: 1996
---
data: 1998
---
```

## 必要なソフトウェア
- Python

## テスト環境
- Ubuntu 20.04 on Windows

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます.
- © 2024 Miyuu Taniguchi
