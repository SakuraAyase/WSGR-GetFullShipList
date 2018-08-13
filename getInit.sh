#!/bin/bash

echo -------战舰少女船只列表自动生成工具-------

wget -O cn_init.json http://version.jr.moefantasy.com/index/getInitConfigs
echo 已下载国服init
wget -O jp_init.json http://version.jp.warshipgirls.com/index/getInitConfigs
echo 已下载日服init
wget -O tw_init.json http://version.jr.moepoint.tw/index/getInitConfigs
echo 已下载台服init
./buildCsv.py cn
echo 创建国服船只列表cn_全船表.csv成功
./buildCsv.py jp
echo 创建日服船只列表jp_全船表.csv成功
./buildCsv.py tw
echo 创建台服船只列表tw_全船表.csv成功
