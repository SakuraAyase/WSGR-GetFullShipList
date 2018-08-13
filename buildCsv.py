#!/usr/bin/python3

from json import *
import codecs
import sys

inf = '_init.json'
ouf = '_全船表.csv'
serverList = ['cn','jp','tw']


if len(sys.argv) == 1 or sys.argv[1] not in serverList :
	sys.exit("Usage: ./buildcsv.py [cn|jp|tw]")
inF = sys.argv[1]+inf
outF = sys.argv[1]+ouf

with open(inF,'r') as f:
	j = loads(f.read())

countryList = ['未知','日本','德国','英国','美国','意大利','法国','苏联','中国','深海','深海','土耳其','荷兰','瑞典','泰国','澳大利亚','加拿大','蒙古','冰岛','智利','芬兰','波兰','奥匈帝国','希腊']
shipTypeList = {1:'航母',2:'轻母',3:'装母',4:'战列',5:'航战',6:'战巡',7:'重巡',8:'航巡',9:'雷巡',10:'轻巡',11:'重炮',12:'驱逐',13:'潜母',14:'潜艇',15:'炮潜',16:'补给',23:'导驱'}
shipTonList = ['未知','小型','中型','大型']
rangeList = ['无','短','中','长','超长']
printList = []
printList.append("编号,船名,国籍,稀有度,舰种,舰级,耐久,火力,护甲,鱼雷,防空,对潜,索敌,闪避,命中,幸运,航速,搭载,射程,船型,装备槽,装备,消耗油,消耗弹,维修油,维修钢,维修时间,分解资源(油弹钢铝),强化经验(火雷甲空)")
equipDic = {};
for equipmnt in j["shipEquipmnt"] :
	equipDic[equipmnt["cid"]] = equipmnt["title"]

for shipCard in j["shipCardWu"]:
	if shipCard["cid"]>=20000000: break
	if shipCard["cid"]==11000113: printList.append("")
	#舰船介绍部分
	data = str(shipCard["shipIndex"])
	data = ','.join((data, shipCard["title"]))
	data = ','.join((data, countryList[shipCard["country"]]))
	data = ','.join((data, str(shipCard["star"])))
	data = ','.join((data, shipTypeList[shipCard["type"]]))
	data = ','.join((data, shipCard["classNo"]))
	data = ','.join((data, str(shipCard["hp"])))
	atk = ' | '.join((str(shipCard["atk"]),str(int(shipCard["atk"])+int(shipCard["strengthenTop"]["atk"]/shipCard["strengthenLevelUpExp"]))))
	data = ','.join((data, atk))
	armor = ' | '.join((str(shipCard["def"]),str(int(shipCard["def"])+int(shipCard["strengthenTop"]["def"]/shipCard["strengthenLevelUpExp"]))))
	data = ','.join((data, armor))
	torp = ' | '.join((str(shipCard["torpedo"]),str(int(shipCard["torpedo"])+int(shipCard["strengthenTop"]["torpedo"]/shipCard["strengthenLevelUpExp"]))))
	data = ','.join((data, torp))
	airdef = ' | '.join((str(shipCard["airDef"]),str(int(shipCard["airDef"])+int(shipCard["strengthenTop"]["air_def"]/shipCard["strengthenLevelUpExp"]))))
	data = ','.join((data, airdef))
	#AntiSub
	antisub = ' | '.join((str(shipCard["antisub"]),str(int(shipCard["antisub"])+int((int(shipCard["antisubMax"])-int(shipCard["antisub"]))*1.1))));
	data = ','.join((data, antisub))
	#Radar
	radar = ' | '.join((str(shipCard["radar"]),str(int(shipCard["radar"])+int((int(shipCard["radarMax"])-int(shipCard["radar"]))*1.1))))
	data = ','.join((data, radar))
	#Miss
	miss = ' | '.join((str(shipCard["miss"]),str(int(shipCard["miss"])+int((int(shipCard["missMax"])-int(shipCard["miss"]))*1.1))))
	data = ','.join((data, miss))
	#Hit
	hit = ' | '.join((str(shipCard["hit"]),str(int(shipCard["hit"])+int((int(shipCard["hitMax"])-int(shipCard["hit"]))*1.1))))
	data = ','.join((data, hit))
	#Luck
	data = ','.join((data, str(shipCard["luck"])))
	#Speed
	data = ','.join((data, str(shipCard["speed"])))
	#Capacity
	if shipCard["capacityInit"] != "0" :
		capacity = '|'.join(map(str,shipCard["capacityInit"]))
	elif shipCard["missileInit"] != "0" :
		capacity = '|'.join(map(str,shipCard["missileInit"]))
	else :
		capacity = '0'
	data = ','.join((data, capacity))
	#Range
	data = ','.join((data, rangeList[shipCard["range"]]))
	#shipton
	data = ','.join((data, shipTonList[shipCard["shipTon"]]))
	#EquipNum
	data = ','.join((data, str(shipCard["equipmentNum"])))
	#Equipments
	equip = shipCard["equipment"]
	equipName = []
	for eqp in equip:
		equipName.append(equipDic.get(eqp))
	equipment = '|'.join(equipName)
	data = ','.join((data, equipment))
	#Oil
	data = ','.join((data, str(shipCard["maxOil"])))
	#Ammo
	data = ','.join((data, str(shipCard["maxAmmo"])))
	#repairOil
	data = ','.join((data, str(shipCard["repairOilModulus"])))
	#repairSteel
	data = ','.join((data, str(shipCard["repairSteelModulus"])))
	#repairTime
	data = ','.join((data, str(shipCard["repairTime"])))
	#dismantle
	dismantle = []
	dismantle.append(str(shipCard["dismantle"]["2"]))
	dismantle.append(str(shipCard["dismantle"]["3"]))
	dismantle.append(str(shipCard["dismantle"]["4"]))
	dismantle.append(str(shipCard["dismantle"]["9"]))
	disman = '|'.join(dismantle)
	data = ','.join((data, disman))
	#supplyExp
	supplyExp = []
	supplyExp.append(str(shipCard["strengthenSupplyExp"]["atk"]))
	supplyExp.append(str(shipCard["strengthenSupplyExp"]["torpedo"]))
	supplyExp.append(str(shipCard["strengthenSupplyExp"]["def"]))
	supplyExp.append(str(shipCard["strengthenSupplyExp"]["air_def"]))
	supply = '|'.join(supplyExp)
	data = ','.join((data, supply))

	printList.append(data)

out = codecs.open(outF,'w','utf_8_sig');
for line in printList:
	print(line, file=out)
out.close()
