# led_binary_number
robosys_kadai2

# 概要
*　0から255までを2進数に直して1になるところを光らせるプログラム

## 
* 1，34，255，37，245，0を実行
* [ demo - YouTube](https://youtu.be/BtGi0TddrO0)

## 環境
* Raspberry Pi 3 Model B
* ROS melodic
* LED 8つ 
* 接続ピン - GPIO21,20,16,26,19,13,6,5 GND
* 抵抗 - 330[Ω]
* 実行方法
```
$ cd ~/catkin/src
$ git clone https://github.com/yurinishio1139/led_binary_number.git
$ cd ..
$ catkin_make
$ cd src/led_binary_number/myled/
$ bash setup bash
$ roslanch led_binary_number number.launch

```
## 回路図
![回路図‗課題2](https://user-images.githubusercontent.com/58972086/72796987-a253ba80-3c83-11ea-8ec8-2a88b9bc71c6.JPG)

