# AIKOH_RZ-5_forcegage_for_ros

## Overview
フォースゲージ（AIKOH_RZ-5）のROSパッケージ。 <br>
詳細：https://www.aikoh.co.jp/forcegauge/rz/ <br>

![AIKOH_RZ-5](https://user-images.githubusercontent.com/56574063/164232267-6496de6f-6890-427c-a996-e86fa7fa0d8b.png) <br>

## Requirement <br>

- ubuntu 18.04 <br>
- python2系 <br>
- ROS melodic <br>
多分他環境でも動く

## Installation <br>
     - cd catkin_ws/src
     - git clone https://github.com/Ryo-hack/AIKOH_RZ-5_forcegage_for_ros.git
     - catkin build
     - sudo chmod 777 ~/catkin_ws/src/AIKOH_RZ-5_forcegage_for_ros/src/force_gage_read_serial.py
     - source ~/catkin_ws/devel/setup.bash 
     
## Usage

- フォースゲージをUSB接続 <br>
- 権限の付与<br>
  `sudo chmod 777 /dev/ttyUSB"NUM"` <br>
- 実行
  `rosrun AIKOH_RZ-5_forcegage_for_ros force_gage_read_serial.py` <br>
node名：AIKOH_forcegage
publisher:AIKOH_forcegage

## Features

## Reference
[商品ページ (Japanese)](https://www.aikoh.co.jp/forcegauge/rz/) <br>
[取扱説明書 (Japanese)](https://www.aikoh.co.jp/wp-content/uploads/AIKOH_RZ_manual_JP_2019.5.pdf)   <br>

## Author
[twitter](https://twitter.com/Ryo_hack_) <br>

## Licence
This software is released under the MIT License, see [LICENSE](./LICENSE). <br>

```
