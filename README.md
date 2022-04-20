# AIKOH_RZ-5_forcegage_for_ros

## Overview
フォースゲージ（AIKOH_RZ-5）のROSパッケージ。
詳細：https://www.aikoh.co.jp/forcegauge/rz/

![AIKOH_RZ-5](https://user-images.githubusercontent.com/36100321/140645407-81af34fd-451e-4b16-b041-acf035970be1.jpeg)

## Requirement

-ubuntu 18.04 
- python2系
- ROS melodic

多分他環境でも動く

##Installation
     - `cd catkin_ws/src`  
     - `git clone https://github.com/Ryo-hack/AIKOH_RZ-5_forcegage_for_ros.git`
     - `source ~/catkin_ws/devel/setup.bash`  
## Usage

フォースゲージをUSB接続
 - `sudo chmod 777 /dev/ttyUSB"NUM"`  

## Features

## Reference
[商品ページ (Japanese)](https://www.aikoh.co.jp/forcegauge/rz/)
[取扱説明書 (Japanese)](https://www.aikoh.co.jp/wp-content/uploads/AIKOH_RZ_manual_JP_2019.5.pdf)  

## Author
[twitter](https://twitter.com/Ryo_hack_)

## Licence
This software is released under the MIT License, see [LICENSE](./LICENSE).

```
