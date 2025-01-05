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
[INFO] [1736072823.577485547] [olympic]: olympic year: 1896
[INFO] [1736072824.071120134] [olympic]: olympic year: 1898
[INFO] [1736072824.571211934] [olympic]: olympic year: 1900
[INFO] [1736072825.071253298] [olympic]: olympic year: 1902
[INFO] [1736072825.571168507] [olympic]: olympic year: 1904
[INFO] [1736072826.071122793] [olympic]: olympic year: 1906
[INFO] [1736072826.571261183] [olympic]: olympic year: 1908
[INFO] [1736072827.071091937] [olympic]: olympic year: 1910
```

## 必要なソフトウェア
- Python

## テスト環境
- Ubuntu 20.04 on Windows

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます.
- © 2024 Miyuu Taniguchi
