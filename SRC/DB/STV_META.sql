DROP SCHEMA IF EXISTS `stv_db`;
CREATE SCHEMA IF NOT EXISTS `stv_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `stv_db`;

create table Star(
	StarID Varchar(20),
	StarName Varchar(50),
	StarStyle varChar(10),
	StarRegion Varchar(50),
	StarNameAbridge Varchar(10),
	primary key(StarID)
);

create table Song(
	SongID Varchar(20),
	SongName Varchar(50),
	SongType Varchar(20),
	SongLanguage Varchar(10),
	SongNameAbridge Varchar(10),
	StarID Varchar(20),
	SongWeek BigInt,
	SongMonth BigInt,
	SongYear BigInt,
	SongDate date,
	primary key(SongID),
	foreign key(StarID) references Star(StarID)
);

create table Comment(
	C_ID BigInt,
	C_Content Varchar(80),
	SongID Varchar(20),
	C_TimeStamp TimeStamp,
	primary key(C_ID),
	foreign key(SongID) references Song(SongID)
);

create table Client(
	ClientID Varchar(20),
	ClientArea Varchar(20),
	ClientType Varchar(20),
	ClientBrand Varchar(20),
	primary key(ClientID)
);

create table C_Song(
	SongID Varchar(20),
	ClientID Varchar(20),
	S_Order int,
	S_Upvalue int,
	primary key(SongID,ClientID),
	foreign key(SongID) references Song(SongID),
	foreign key(ClientID) references Client(ClientID)
);

create table History(
       ClientID Varchar(20),
       SongID Varchar(20),
       primary key(SongID, ClientID),
       foreign key(SongID) references Song(SongID),
       foreign key(ClientID) references Client(ClientID)
);

insert into Star values('1','2NE1','组合','韩国','2');
insert into Star values('2','Adele','女','欧美','A');
insert into Star values('3','A Pink','组合','韩国','AP');
insert into Star values('4','阿桑','女','中国台湾','AS');
insert into Star values('5','Beyond','组合','中国香港','B');
insert into Star values('6','Bigbang','组合','韩国','B');
insert into Star values('7','Blue','组合','欧美','B');
insert into Star values('8','Backstreet Boys','组合','欧美','BB');
insert into Star values('9','本兮','女','内地','BX');
insert into Star values('10','Colbie Caillat','女','欧美','CC');
insert into Star values('11','曹格','男','马来西亚','CG');
insert into Star values('12','蔡国权','男','中国香港','CGQ');
insert into Star values('13','陈慧娴','女','中国香港','CHX');
insert into Star values('14','Chris Medina','男','欧美','CM');
insert into Star values('15','陈少华','男','内地','CSH');
insert into Star values('16','陈淑桦','女','中国台湾','CSH');
insert into Star values('17','蔡依林','女','中国台湾','CYL');
insert into Star values('18','陈奕迅','男','中国香港','CYX');
insert into Star values('19','刀郎','男','内地','DL');
insert into Star values('20','邓丽君','女','中国台湾','DLJ');
insert into Star values('21','DJ Samuel Kimko','组合','欧美','DSK');
insert into Star values('22','董文华','女','内地','DWH');
insert into Star values('23','邓紫棋','女','内地','DZQ');
insert into Star values('24','大张伟','男','内地','DZW');
insert into Star values('25','Eluveitie','组合','欧美','E');
insert into Star values('26','Eminem','男','欧美','E');
insert into Star values('27','EXO','组合','韩国','E');
insert into Star values('28','E Nomine ','组合','欧美','EN');
insert into Star values('29','Emma Re','女','欧美','ER');
insert into Star values('30','凤凰传奇','组合','内地','FHCQ');
insert into Star values('31','范玮琪','女','中国台湾','FWQ');
insert into Star values('32','费玉清','男','中国台湾','FYQ');
insert into Star values('33','GALA乐队','组合','内地','G');
insert into Star values('34','GIRLS GIRLS','组合','韩国','GG');
insert into Star values('35','郭静','女','中国香港','GJ');
insert into Star values('36','光良','男','马来西亚','GL');
insert into Star values('37','歌莉雅','女','中国香港','GLY');
insert into Star values('38','关喆','男','内地','GZ');
insert into Star values('39','韩宝仪','女','中国台湾','HBY');
insert into Star values('40','河图','男','内地','HT');
insert into Star values('41','胡彦斌','男','内地','HYB');
insert into Star values('42','鞠婧祎','女','内地','JJY');
insert into Star values('43','Jonas Kaufmann','男','欧美','JK');
insert into Star values('44','贾玲','女','内地','JL');
insert into Star values('45','金泰妍','女','韩国','JTY');
insert into Star values('46','玖月奇迹','组合','内地','JYCQ');
insert into Star values('47','Kara','组合','韩国','k');
insert into Star values('48','酷玩乐队','组合','欧美','KWYD');
insert into Star values('49','罗大佑','男','中国台湾','LDY');
insert into Star values('50','Lady Gaga','女','欧美','LG');
insert into Star values('51','林俊杰','男','新加坡','LJJ');
insert into Star values('52','梁静茹','女','马来西亚','LJR');
insert into Star values('53','冷漠','男','内地','LM');
insert into Star values('54','Linkin Park','组合','欧美','LP');
insert into Star values('55','李荣浩','男','内地','LRH');
insert into Star values('56','李日詹','男','内地','LRZ');
insert into Star values('57','李宇春','女','内地','LYC');
insert into Star values('58','林宥嘉','男','中国台湾','LYJ');
insert into Star values('59','林子祥','男','中国台湾','LZX');
insert into Star values('60','Maroon5','组合','欧美','M');
insert into Star values('61','Mariah Carey','女','欧美','MC');
insert into Star values('62','Michael Jackson','男','欧美','MJ');
insert into Star values('63','Michael Learns To Rock','组合','欧美','MLTR');
insert into Star values('64','莫文蔚','女','中国香港','MWW');
insert into Star values('65','NCT','组合','韩国','NCT');
insert into Star values('66','那英','女','内地','NY');
insert into Star values('67','彭佳慧','女','中国台湾','PJH');
insert into Star values('68','朴树','男','内地','PS');
insert into Star values('69','祁隆','男','内地','QL');
insert into Star values('70','齐秦','男','内地','QQ');
insert into Star values('71','曲婉婷','女','内地','QWT');
insert into Star values('72','Roxette','组合','欧美','R');
insert into Star values('73','Secret','组合','韩国','S');
insert into Star values('74','SNH48','组合','内地','S');
insert into Star values('75','Soler','组合','中国澳门','S');
insert into Star values('76','Steelheart','组合','欧美','S');
insert into Star values('77','苏打绿','组合','中国台湾','SDL');
insert into Star values('78','宋冬野','男','内地','SDY');
insert into Star values('79','Secret Garden','组合','欧美','SG');
insert into Star values('80','屠洪刚','男','内地','SHG');
insert into Star values('81','Super Junior','组合','韩国','SJ');
insert into Star values('82','孙丽英','女','内地','SLY');
insert into Star values('83','Selwyn Pretorius','组合','欧美','SP');
insert into Star values('84','苏芮','女','中国台湾','SR');
insert into Star values('85','TFBOYS','组合','内地','T');
insert into Star values('86','Trademark','组合','欧美','T');
insert into Star values('87','谭咏麟','男','中国香港','TYL');
insert into Star values('88','Westlife','组合','欧美','W');
insert into Star values('89','魏晨','男','内地','WC');
insert into Star values('90','王力宏','男','欧美','WLH');
insert into Star values('91','伍思凯','男','中国台湾','WSK');
insert into Star values('92','王心凌','女','中国台湾','WXL');
insert into Star values('93','五月天','组合','中国台湾','WYT');
insert into Star values('94','小曲儿','男','内地','XQE');
insert into Star values('95','许嵩','男','内地','XS');
insert into Star values('96','许巍','男','内地','XW');
insert into Star values('97','信乐团','组合','中国台湾','XYT');
insert into Star values('98','薛之谦','男','内地','XZQ');
insert into Star values('99','杨丞琳','女','中国台湾','YCL');
insert into Star values('100','庾澄庆','男','中国台湾','YCQ');
insert into Star values('101','音频怪物','男','内地','YPGW');
insert into Star values('102','杨钰莹','女','内地','YYY');
insert into Star values('103','杨宗纬','男','中国台湾','YZW');
insert into Star values('104','张柏芝','女','中国香港','ZBZ');
insert into Star values('105','周华健','男','中国香港','ZHJ');
insert into Star values('106','张惠妹','女','中国台湾','ZHM');
insert into Star values('107','张杰','男','内地','ZJ');
insert into Star values('108','周杰伦','男','中国台湾','ZJL');
insert into Star values('109','张敬轩','男','中国台湾','ZJX');
insert into Star values('110','张靓颖','女','内地','ZLY');
insert into Star values('111','张韶涵','女','中国台湾','ZSH');
insert into Star values('112','张信哲','男','中国台湾','ZXZ');
insert into Star values('113','卓依婷','女','中国台湾','ZYT');
insert into Star values('114','朱主爱','女','马来西亚','ZZA');
insert into Star values('115','Chrissy Costanza','女','欧美','CC');
insert into Star values('116','Christina Grimmiea','女','欧美','CG');




insert into Song values('1','Heart Attack - feat Sam Tsui','流行','英文','HA','115','21','67','751', CURDATE());
insert into Song values('2','Just A Dream - feat Sam Tsui','流行','英文','JAD','116','35','112','921',CURDATE());
insert into Song values('3','Beauty And A Beat - feat Alex Goot','流行','英文','BAAB','115','33','151','982',CURDATE());
insert into Song values('4','Red - Against the Current Cover','摇滚','英文','RED','115','15','116','1211',CURDATE());
insert into Song values('5','斑马斑马','民谣','中文','BMBM','78','44','182','1332',CURDATE());
insert into Song values('6','别那么骄傲','流行','中文','BNMJA','56','22','157','891',CURDATE());
insert into Song values('7','不息之河','流行','中文','BXZH','85','25','200','1053',CURDATE());
insert into Song values('8','不装饰你的梦','流行','粤语','BZSNDM','12','8','28','298',CURDATE());
insert into Song values('9','长城','摇滚','中文','CC','5','7','21','219',CURDATE());
insert into Song values('10','踩踩踩','流行','中文','CCC','46','2','90','821',CURDATE());

insert into Song values('11','初次尝到寂寞','流行','粤语','CCCDJM','20','20','48','401',CURDATE());
insert into Song values('12','Chewing Gum','流行','韩语','CG','65','11','31','211',CURDATE());
insert into Song values('13','曾经的你','摇滚','中文','CJDN','96','31','201','1512',CURDATE());
insert into Song values('14','Call Me Baby','流行','中文','CMB','27','12','80','1000',CURDATE());
insert into Song values('15','潮湿的心','流行','中文','CSDX','113','12','32','333',CURDATE());
insert into Song values('16','春天的故事','流行','中文','CTDGS','22','5','56','322',CURDATE());
insert into Song values('17','点豆豆','流行','中文','DDD','33','12','55','841',CURDATE());
insert into Song values('18','大地','摇滚','粤语','DD','5','21','48','416',CURDATE());
insert into Song values('19','等你等了那么久','流行','中文','DNDLNMJ','69','21','121','931',CURDATE());
insert into Song values('20','东南西北风','流行','中文','DNXBF','113','22','98','511',CURDATE());
insert into Song values('21','董小姐','民谣','中文','DXJ','78','50','184','1652',CURDATE());
insert into Song values('22','大约在冬季','流行','中文','DYZDJ','70','44','177','1521',CURDATE());
insert into Song values('23','Expection','摇滚','英文','E','37','9','32','311',CURDATE());
insert into Song values('24','Espiritu del Aire','流行','西班牙语','EDA','28','15','79','144',CURDATE());
insert into Song values('25','Endless Love','流行','英文','EL','59','8','15','122',CURDATE());
insert into Song values('26','E lucevan le stelle','蓝调','意大利语','ELLS','43','5','10','100',CURDATE());
insert into Song values('27','E TU COME STAI ','流行','意大利语','ETCS','29','6','101','244',CURDATE());
insert into Song values('28','风含情水含笑','流行','中文','FHQSHX','102','11','51','516',CURDATE());
insert into Song values('29','翻篇','流行','中文','FP','9','33','98','521',CURDATE());
insert into Song values('30','浮诛','古风','中文','FZ','107','33','121','1021',CURDATE());
insert into Song values('31','干杯','摇滚','中文','GB','93','19','59','511',CURDATE());
insert into Song values('32','刚刚好','流行','中文','GGH','98','98','459','2661',CURDATE());
insert into Song values('33','滚滚红尘','流行','中文','GGHC','16','12','31','291',CURDATE());
insert into Song values('34','感觉自己萌萌哒','流行','中文','GJZJMMD','44','14','69','641',CURDATE());
insert into Song values('35','高山青','乡村','中文','GSQ','39','3','18','200',CURDATE());
insert into Song values('36','怪胎秀','流行','中文','GTX','106','19','69','706',CURDATE());
insert into Song values('37','观众','流行','中文','GZ','99','66','189','1022',CURDATE());
insert into Song values('38','公主披风','流行','中文','GZPF	','74','9','41','313',CURDATE());
insert into Song values('39','花儿为什么这样红','乡村','中文','HEWSMZYH','82','7','23','211',CURDATE());
insert into Song values('40','皇后大道东','流行','粤语','HHDDD','49','2','15','121',CURDATE());
insert into Song values('41','海阔天空','流行','粤语','HKTK','5','39','151','1599',CURDATE());
insert into Song values('42','何日君再来','流行','中文','HRJZL','20','12','39','411',CURDATE());
insert into Song values('43','荷塘月色','流行','中文','HTYS','30','11','41','511',CURDATE());
insert into Song values('44','好想你','流行','中文','HXN','114','24','79','983',CURDATE());
insert into Song values('45','海洋之心','流行','中文','HYZX','17','22','98','896',CURDATE());
insert into Song values('46','I','流行','韩语','I','45','10','34','288',CURDATE());
insert into Song values('47','I Believe','流行','中文','IB','112','27','212','1009',CURDATE());
insert into Song values('48','I Do','流行','英文','ID','10','15','80','120',CURDATE());
insert into Song values('49','I Do I Do','流行','韩语','IDID','73','3','121','981',CURDATE());
insert into Song values('50','In My Mind','摇滚','英文','IMM','21','12','21','177',CURDATE());
insert into Song values('51','酒干倘卖无','流行','中文','JGTMW','84','13','45','467',CURDATE());
insert into Song values('52','Juicy Secret','流行','韩语','JS','34','14','31','189',CURDATE());
insert into Song values('53','今天是你的生日','流行','中文','JTSNDSR','22','4','21','198',CURDATE());
insert into Song values('54','九月九的酒','乡村','中文','JYJDJ','15','10','38','403',CURDATE());
insert into Song values('55','精忠报国','流行','中文','JZBG','80','6','31','412',CURDATE());
insert into Song values('56','卡比巴拉的海','民谣','中文','KBBLDH','78','24','101','962',CURDATE());
insert into Song values('57','空白格','流行','中文','KBG','103','52','201','2051',CURDATE());
insert into Song values('58','开不了心','流行','粤语','KBLX','18','14','48','571',CURDATE());
insert into Song values('59','看我72变','流行','中文','KW72B','17','32','111','901',CURDATE());
insert into Song values('60','狼','摇滚','中文','L','70','10','31','299',CURDATE());
insert into Song values('61','李白','流行','中文','LB','55','45','170','1823',CURDATE());
insert into Song values('62','兰花草','民谣','中文','LHC','113','14','41','302',CURDATE());
insert into Song values('63','烈火神盾','流行','中文','LHSD','89','38','144','1211',CURDATE());
insert into Song values('64','恋西游','古风','中文','LXY','85','39','133','1011',CURDATE());
insert into Song values('65','Monster','摇滚','韩语','M','6','35','151','1521',CURDATE());
insert into Song values('66','模特','流行','中文','MT','55','69','233','1958',CURDATE());
insert into Song values('67','梦驼铃','流行','中文','MTL','32','9','28','188',CURDATE());
insert into Song values('68','Mi Vida','摇滚','西班牙语','MV','21','6','19','69',CURDATE());
insert into Song values('69','梦想岛','流行','中文','MXD','74','29','100','901',CURDATE());
insert into Song values('70','你把我灌醉','流行','中文','NBWGZ','23','51','198','2012',CURDATE());
insert into Song values('71','你不知道的事','流行','中文','NBZDDS','90','49','203','2310',CURDATE());
insert into Song values('72','难念的经','流行','粤语','NLDJ','105','9','26','189',CURDATE());
insert into Song values('73','暖暖','流行','中文','NNN','52','24','134','1543',CURDATE());
insert into Song values('74','NoNoNo','流行','韩语','NNN','3','9','31','91',CURDATE());
insert into Song values('75','恋曲1990','流行','中文','NQ1990','49','8','21','214',CURDATE());
insert into Song values('76','你是我的眼','流行','中文','NSWDY','58','23','165','1990',CURDATE());
insert into Song values('77','negative things','R&B(蓝调）','英文','NT','83','8','36','400',CURDATE());
insert into Song values('78','那些花儿','民谣','中文','NXHE','68','28','127','1667',CURDATE());
insert into Song values('79','逆战','摇滚','中文','NZ','107','27','129','1701',CURDATE());
insert into Song values('80','Obsessed','R&B','英文','O','61','3','10','103',CURDATE());
insert into Song values('81','only love','流行','英文','OL','86','11','40','478',CURDATE());
insert into Song values('82','one love','R&B','英文','OL','7','13','45','533',CURDATE());
insert into Song values('83','偶尔','流行','中文','OR','23','20','91','1000',CURDATE());
insert into Song values('84','欧若拉','流行','中文','ORL','111','25','105','1228',CURDATE());
insert into Song values('85','payphone','摇滚','英文','P','60','8','32','372',CURDATE());
insert into Song values('86','漂浮地铁','流行','中文','PFDT','57','9','50','588',CURDATE());
insert into Song values('87','pretty girl ','流行','韩语','PG','47','2','7','87',CURDATE());
insert into Song values('88','朋友','流行','中文','PY','105','23','121','1330',CURDATE());
insert into Song values('89','披着羊皮的狼','流行','中文','PZYPDL','87','20','80','899',CURDATE());
insert into Song values('90','倾尽天下','古风','中文','QJTX','40','8','32','356',CURDATE());
insert into Song values('91','清明雨上','流行','中文','QMYS','95','8','47','543',CURDATE());
insert into Song values('92','Queen Of Rain','流行','英文','QOR','72','6','31','371',CURDATE());
insert into Song values('93','千千阙歌','流行','中文','QQQG','13','20','97','1007',CURDATE());
insert into Song values('94','牵手','流行','中文','QS','84','23','105','1333',CURDATE());
insert into Song values('95','晴天','流行','中文','QT','108','26','112','1249',CURDATE());
insert into Song values('96','日不落','流行','中文','RBL','17','40','189','2200',CURDATE());
insert into Song values('97','如果没有你','流行','中文','RGMYN','64','26','120','1445',CURDATE());
insert into Song values('98','如果这就是爱情','流行','中文','RGZJSAQ','110','22','100','1199',CURDATE());
insert into Song values('99','如花','古风','中文','RH','40','5','18','207',CURDATE());
insert into Song values('100','Rolling in the deep','摇滚','英文','RITD','2','15','78','900',CURDATE());
insert into Song values('101','热情的沙漠','摇滚','中文','RQDSM','100','22','95','1134',CURDATE());
insert into Song values('102','是非题','流行','中文','SFT','31','24','91','992',CURDATE());
insert into Song values('103','shes gone','摇滚','英文','SG','76','12','43','521',CURDATE());
insert into Song values('104','世界唯一的你','流行','中文','SJWYDN','11','28','114','1442',CURDATE());
insert into Song values('105','死了都要爱','摇滚','中文','SLDYA','97','37','191','2199',CURDATE());
insert into Song values('106','someone like you','流行','英文','SLY','2','15','67','789',CURDATE());
insert into Song values('107','上邪','古风','中文','SY','94','12','52','634',CURDATE());
insert into Song values('108','Thousandfold','摇滚','英文','T','25','3','10','98',CURDATE());
insert into Song values('109','特别的爱给特别的你','流行','中文','TBDAGTBDN','91','11','50','578',CURDATE());
insert into Song values('110','童话','流行','中文','TH','36','29','138','1552',CURDATE());
insert into Song values('111','take me to your heart ','流行','英文','TMTYH','63','18','71','801',CURDATE());
insert into Song values('112','她说','流行','中文','TS','51','20','96','1120',CURDATE());
insert into Song values('113','天下','流行','中文','TX','107','29','132','1445',CURDATE());
insert into Song values('114','u','流行','韩语','U','81','2','5','56',CURDATE());
insert into Song values('115','ugly ','流行','韩语','U','1','3','9','92',CURDATE());
insert into Song values('116','unbelievable','摇滚','英文','U','75','1','4','45',CURDATE());
insert into Song values('117','unmistakable','流行','英文','U','8','5','19','200',CURDATE());
insert into Song values('118','Us Against The World','pop','英文','UATW','88','6','30','344',CURDATE());
insert into Song values('119','venus','pop','英文','V','50','3','17','198',CURDATE());
insert into Song values('120','Valentines Day','流行','英文','VD','54','5','19','276',CURDATE());
insert into Song values('122','vision of love','R＆B','英文','VOL','61','4','20','231',CURDATE());
insert into Song values('123','问','流行','中文','W','16','29','142','1600',CURDATE());
insert into Song values('124','What are words','流行','英文','WAW','14','10','47','513',CURDATE());
insert into Song values('125','我的歌声里','流行','中文','WDGSL','71','36','160','1890',CURDATE());
insert into Song values('126','吻得太逼真','流行','中文','WDTBZ','109','24','100','1240',CURDATE());
insert into Song values('127','无关风月','古风','中文','WGFY','101','11','50','598',CURDATE());
insert into Song values('128','想把你写成一首歌','流行','中文','XBNXCYSG','93','26','89','981',CURDATE());
insert into Song values('129','喜欢你','流行','中文','XHN','5','25','110','1222',CURDATE());
insert into Song values('130','相见恨晚','流行','中文','XJHW','67','34','145','1511',CURDATE());
insert into Song values('131','想你的夜','流行','中文','XNDY','38','25','103','1100',CURDATE());
insert into Song values('132','小情歌','流行','中文','XQG','77','39','189','2000',CURDATE());
insert into Song values('133','下一个天亮','流行','中文','XYGTL','35','31','143','1602',CURDATE());
insert into Song values('134','星语心愿','流行','中文','XYXY','104','41','200','2432',CURDATE());
insert into Song values('135','You Are Not Alone','流行','英文','YANA','62','23','90','1002',CURDATE());
insert into Song values('136','洋葱','流行','中文','YC','103','29','122','1432',CURDATE());
insert into Song values('137','月光','古风','中文','YG','41','23','87','992',CURDATE());
insert into Song values('138','烟花易冷','流行','中文','YHYL','108','25','111','1334',CURDATE());
insert into Song values('139','YOU RAISE ME UP','流行','英文','YRMU','79','18','75','883',CURDATE());
insert into Song values('140','一直很安静','流行','中文','YZHAJ','4','26','132','1553',CURDATE());
insert into Song values('141','左边','流行','中文','ZB','99','23','128','1449',CURDATE());
insert into Song values('142','最初的梦想','流行','中文','ZCDMX','31','35','171','2080',CURDATE());
insert into Song values('143','真的爱你','摇滚','中文','ZDAN','5','28','115','1378',CURDATE());
insert into Song values('144','征服','流行','中文','ZF','66','23','101','1120',CURDATE());
insert into Song values('145','醉飞霜','古风','中文','ZFS','42','12','54','670',CURDATE());
insert into Song values('146','最重要的决定','流行','中文','ZZYDJD','31','30','120','1578',CURDATE());


insert into Comment values(1,'好听','1', NOW());
insert into Comment values(2,'我爱你','2', NOW());
insert into Comment values(3,'歌曲的开头令人有听下去的感觉','3', NOW());
insert into Comment values(4,'每个人都有自己喜欢的风格','4', NOW());
insert into Comment values(5,'我想你啦','1', NOW());
insert into Comment values(6,'么么哒','2', NOW());
insert into Comment values(7,'爱你是我的荣幸','3', NOW());
insert into Comment values(8,'他在灯火阑珊处','4', NOW());
insert into Comment values(9,'有一个人在等我','1', NOW());
insert into Comment values(10,'喜欢你','2', NOW());
insert into Comment values(11,'歌曲是我的灵魂','3', NOW());
insert into Comment values(12,'.我想在五十年之后我一定还是像现在一样爱你','4', NOW());
insert into Comment values(13,'我不要短暂的温存，只要你一世的陪伴','3', NOW());
insert into Comment values(14,'只因你太美好令我无法坦白说出我爱你','4', NOW());
insert into Comment values(15,'好听','1', NOW());
insert into Comment values(16,'我爱你','1', NOW());
insert into Comment values(17,'歌曲的开头令人有听下去的感觉','3', NOW());
insert into Comment values(18,'每个人都有自己喜欢的风格','2', NOW());
insert into Comment values(19,'我想你啦','1', NOW());
insert into Comment values(20,'么么哒','2', NOW());
insert into Comment values(21,'爱你是我的荣幸','2', NOW());
insert into Comment values(22,'他在灯火阑珊处','2', NOW());
insert into Comment values(23,'有一个人在等我','3', NOW());
insert into Comment values(24,'喜欢你','4', NOW());

insert into Client values('1','北京','a','联想');
insert into Client values('2','上海','b','戴尔');
insert into Client values('3','上海','c','惠普');
