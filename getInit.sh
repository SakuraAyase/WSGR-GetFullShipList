#!/bin/bash

echo -------战舰少女船只列表自动生成工具-------

#wget -O cn_init.json http://version.jr.moefantasy.com/index/getInitConfigs
#wget -O cn_cbt_init.json http://cbt.jianniang.com/index/getInitConfigs
#wget -O cn_cbt_init.json http://500cbt.jianniang.com/index/getInitConfigs
wget -O jp_init.json http://version.jp.warshipgirls.com/index/getInitConfigs
#wget -O tw_cbt_init.json http://cbt.jr.moepoint.tw/index/getInitConfigs
wget -O tw_init.json http://version.jr.moepoint.tw/index/getInitConfigs
./buildCsv.py cn
./buildCsv.py jp
./buildCsv.py tw
#./buildCsv.py cn_cbt
#./buildCsv.py tw_cbt

echo -------Program Complete-------
