DROP SCHEMA IF EXISTS `ktv_db`;
CREATE SCHEMA IF NOT EXISTS `ktv_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `ktv_db`;

-- drop table C_Song;
-- drop table Client;
-- drop table Comment;
-- drop table Song;
-- drop table Star;

create table Star(
	StarID Varchar(20),
	StarName Varchar(50),
	StarStyle varChar(10),
	StarRegion Varchar(50),
	StarNameAbridge Varchar(10),
	RouteStartID Varchar(50),
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
	SongRoute Varchar(100),
	primary key(SongID),
	foreign key(StarID) references Star(StarID)
);

create table Comment(
	C_ID Varchar(20),
	C_content Varchar(80),
	SongID Varchar(20),
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
	C_Order int,
	primary key(SongID,ClientID),
	foreign key(SongID) references Song(SongID),
	foreign key(ClientID) references Client(ClientID)
);

-- delimiter //
-- CREATE TRIGGER ktv_csong_delete Before Delete ON C_Song FOR EACH ROW Begin Update C_Song Set C_Order = C_Order - 1 Where C_Order > old.C_Order; End//
-- delimiter ;

-- delimiter //
-- CREATE TRIGGER ktv_csong_insert Before Insert ON C_Song FOR EACH ROW Update C_Song Set C_Order = C_Order + 1 Where C_Song.C_Order >= old.C_Order;//
-- delimiter ;

insert into Star values('1','2NE1','组合','韩国','2','2NE1.jpg');
insert into Star values('2','Adele','女','欧美','A','Adele.jpg');
insert into Star values('3','A Pink','组合','韩国','AP','A Pink.jpg');
insert into Star values('4','阿桑','女','中国台湾','AS','阿桑.jpg');
insert into Star values('5','Beyond','组合','中国香港','B','Beyond.jpg');
insert into Star values('6','Bigbang','组合','韩国','B','Bigbang.jpg');
insert into Star values('7','Blue','组合','欧美','B','Blue.jpg');
insert into Star values('8','Backstreet Boys','组合','欧美','BB','Backstreet Boys.jpg');
insert into Star values('9','本兮','女','内地','BX','本兮.jpg');
insert into Star values('10','Colbie Caillat','女','欧美','CC	Colbie','Caillat.jpg');
insert into Star values('11','曹格','男','马来西亚','CG','曹格.jpg');
insert into Star values('12','蔡国权','男','中国香港','CGQ','蔡国权.jpg');
insert into Star values('13','陈慧娴','女','中国香港','CHX','陈慧娴.jpg');
insert into Star values('14','Chris Medina','男','欧美','CM','Chris Medina.jpg');
insert into Star values('15','陈少华','男','内地','CSH','陈少华.jpg');
insert into Star values('16','陈淑桦','女','中国台湾','CSH','陈淑桦.jpg');
insert into Star values('17','蔡依林','女','中国台湾','CYL','蔡依林.jpg');
insert into Star values('18','陈奕迅','男','中国香港','CYX','陈奕迅.jpg');
insert into Star values('19','刀郎','男','内地','DL','刀郎.jpg');
insert into Star values('20','邓丽君','女','中国台湾','DLJ','邓丽君.jpg');
insert into Star values('21','DJ Samuel Kimko','组合','欧美','DSK','DJ Samuel Kimko.jpg');
insert into Star values('22','董文华','女','内地','DWH','董文华.jpg');
insert into Star values('23','邓紫棋','女','内地','DZQ','邓紫棋.jpg');
insert into Star values('24','大张伟','男','内地','DZW','大张伟.jpg');
insert into Star values('25','Eluveitie','组合','欧美','E','Eluveitie.jpg');
insert into Star values('26','Eminem','男','欧美','E','Eminem.jpg');
insert into Star values('27','EXO','组合','韩国','E','EXO.jpg');
insert into Star values('28','E Nomine ','组合','欧美','EN','E Nomine.jpg');
insert into Star values('29','Emma Re','女','欧美','ER','Emma Re.jpg');
insert into Star values('30','凤凰传奇','组合','内地','FHCQ','凤凰传奇.jpg');
insert into Star values('31','范玮琪','女','中国台湾','FWQ','范玮琪.jpg');
insert into Star values('32','费玉清','男','中国台湾','FYQ','费玉清.jpg');
insert into Star values('33','GALA乐队','组合','内地','G','GALA乐队.jpg');
insert into Star values('34','GIRLS GIRLS','组合','韩国','GG','GIRLS GIRLS.jpg');
insert into Star values('35','郭静','女','中国香港','GJ','郭静.jpg');
insert into Star values('36','光良','男','马来西亚','GL','光良.jpg');
insert into Star values('37','歌莉雅','女','中国香港','GLY','歌莉雅.jpg');
insert into Star values('38','关喆','男','内地','GZ','关喆.jpg');
insert into Star values('39','韩宝仪','女','中国台湾','HBY','韩宝仪.jpg');
insert into Star values('40','河图','男','内地','HT','河图.jpg');
insert into Star values('41','胡彦斌','男','内地','HYB','胡彦斌.jpg');
insert into Star values('42','鞠婧祎','女','内地','JJY','鞠婧祎.jpg');
insert into Star values('43','Jonas Kaufmann','男','欧美','JK','Jonas Kaufmann.jpg');
insert into Star values('44','贾玲','女','内地','JL','贾玲.jpg');
insert into Star values('45','金泰妍','女','韩国','JTY','金泰妍.jpg');
insert into Star values('46','玖月奇迹','组合','内地','JYCQ','玖月奇迹.jpg');
insert into Star values('47','Kara','组合','韩国','k','Kara.jpg');
insert into Star values('48','酷玩乐队','组合','欧美','KWYD','酷玩乐队.jpg');
insert into Star values('49','罗大佑','男','中国台湾','LDY','罗大佑.jpg');
insert into Star values('50','Lady Gaga','女','欧美','LG','Lady Gaga.jpg');
insert into Star values('51','林俊杰','男','新加坡','LJJ','林俊杰.jpg');
insert into Star values('52','梁静茹','女','马来西亚','LJR','梁静茹.jpg');
insert into Star values('53','冷漠','男','内地','LM','冷漠.jpg');
insert into Star values('54','Linkin Park','组合','欧美','LP','Linkin Park.jpg');
insert into Star values('55','李荣浩','男','内地','LRH','李荣浩.jpg');
insert into Star values('56','李日詹','男','内地','LRZ','李日詹.jpg');
insert into Star values('57','李宇春','女','内地','LYC','李宇春.jpg');
insert into Star values('58','林宥嘉','男','中国台湾','LYJ','林宥嘉.jpg');
insert into Star values('59','林子祥','男','中国台湾','LZX','林子祥.jpg');
insert into Star values('60','Maroon5','组合','欧美','M','Maroon5.jpg');
insert into Star values('61','Mariah Carey','女','欧美','MC','Mariah Carey.jpg');
insert into Star values('62','Michael Jackson','男','欧美','MJ','Michael Jackson.jpg');
insert into Star values('63','Michael Learns To Rock','组合','欧美','MLTR','Michael Learns To Rock.jpg');
insert into Star values('64','莫文蔚','女','中国香港','MWW','莫文蔚.jpg');
insert into Star values('65','NCT','组合','韩国','NCT','NCT.jpg');
insert into Star values('66','那英','女','内地','NY','那英.jpg');
insert into Star values('67','彭佳慧','女','中国台湾','PJH','彭佳慧.jpg');
insert into Star values('68','朴树','男','内地','PS','朴树.jpg');
insert into Star values('69','祁隆','男','内地','QL','祁隆.jpg');
insert into Star values('70','齐秦','男','内地','QQ','齐秦.jpg');
insert into Star values('71','曲婉婷','女','内地','QWT','曲婉婷.jpg');
insert into Star values('72','Roxette','组合','欧美','R','Roxette.jpg');
insert into Star values('73','Secret','组合','韩国','S','Secret.jpg');
insert into Star values('74','SNH48','组合','内地','S','SNH48.jpg');
insert into Star values('75','Soler','组合','中国澳门','S','Soler.jpg');
insert into Star values('76','Steelheart','组合','欧美','S','Steelheart.jpg');
insert into Star values('77','苏打绿','组合','中国台湾','SDL','苏打绿.jpg');
insert into Star values('78','宋冬野','男','内地','SDY','宋冬野.jpg');
insert into Star values('79','Secret Garden','组合','欧美','SG','Secret Garden.jpg');
insert into Star values('80','屠洪刚','男','内地','SHG','屠洪刚.jpg');
insert into Star values('81','Super Junior','组合','韩国','SJ','Super Junior.jpg');
insert into Star values('82','孙丽英','女','内地','SLY','孙丽英.jpg');
insert into Star values('83','Selwyn Pretorius','组合','欧美','SP','Selwyn Pretorius.jpg');
insert into Star values('84','苏芮','女','中国台湾','SR','苏芮.jpg');
insert into Star values('85','TFBOYS','组合','内地','T','TFBOYS.jpg');
insert into Star values('86','Trademark','组合','欧美','T','Trademark.jpg');
insert into Star values('87','谭咏麟','男','中国香港','TYL','谭咏麟.jpg');
insert into Star values('88','Westlife','组合','欧美','W','Westlife.jpg');
insert into Star values('89','魏晨','男','内地','WC','魏晨.jpg');
insert into Star values('90','王力宏','男','欧美','WLH','王力宏.jpg');
insert into Star values('91','伍思凯','男','中国台湾','WSK','伍思凯.jpg');
insert into Star values('92','王心凌','女','中国台湾','WXL','王心凌.jpg');
insert into Star values('93','五月天','组合','中国台湾','WYT','五月天.jpg');
insert into Star values('94','小曲儿','男','内地','XQE','小曲儿.jpg');
insert into Star values('95','许嵩','男','内地','XS','许嵩.jpg');
insert into Star values('96','许巍','男','内地','XW','许巍.jpg');
insert into Star values('97','信乐团','组合','中国台湾','XYT','信乐团.jpg');
insert into Star values('98','薛之谦','男','内地','XZQ','薛之谦.jpg');
insert into Star values('99','杨丞琳','女','中国台湾','YCL','杨丞琳.jpg');
insert into Star values('100','庾澄庆','男','中国台湾','YCQ','庾澄庆.jpg');
insert into Star values('101','音频怪物','男','内地','YPGW','音频怪物.jpg');
insert into Star values('102','杨钰莹','女','内地','YYY','杨钰莹.jpg');
insert into Star values('103','杨宗纬','男','中国台湾','YZW','杨宗纬.jpg');
insert into Star values('104','张柏芝','女','中国香港','ZBZ','张柏芝.jpg');
insert into Star values('105','周华健','男','中国香港','ZHJ','周华健.jpg');
insert into Star values('106','张惠妹','女','中国台湾','ZHM','张惠妹.jpg');
insert into Star values('107','张杰','男','内地','ZJ','张杰.jpg');
insert into Star values('108','周杰伦','男','中国台湾','ZJL','周杰伦.jpg');
insert into Star values('109','张敬轩','男','中国台湾','ZJX','张敬轩.jpg');
insert into Star values('110','张靓颖','女','内地','ZLY','张靓颖.jpg');
insert into Star values('111','张韶涵','女','中国台湾','ZSH','张韶涵.jpg');
insert into Star values('112','张信哲','男','中国台湾','ZXZ','张信哲.jpg');
insert into Star values('113','卓依婷','女','中国台湾','ZYT','卓依婷.jpg');
insert into Star values('114','朱主爱','女','马来西亚','ZZA','朱主爱.jpg');



insert into Song values('1','爱你','流行','中文','AN','92','21','67','751','爱你_标清.flv');
insert into Song values('2','爱你却要说分手','流行','中文','ANQYSFS','53','35','112','921','爱你却要说分手_标清.flv');
insert into Song values('3','爱是你我','流行','中文','ANSW','19','33','151','982','爱是你我_标清.flv');
insert into Song values('4','倍儿爽','摇滚','中文','BES','24','15','116','1211','倍儿爽_标清.flv');
insert into Song values('5','斑马斑马','民谣','中文','BMBM','78','44','182','1332','斑马斑马_标清.flv');
insert into Song values('6','别那么骄傲','流行','中文','BNMJA','56','22','157','891','别那么骄傲_标清.flv');
insert into Song values('7','不息之河','流行','中文','BXZH','85','25','200','1053','不息之河_标清.flv');
insert into Song values('8','不装饰你的梦','流行','粤语','BZSNDM','12','8','28','298','不装饰你的梦_标清.flv');
insert into Song values('9','长城','摇滚','中文','CC','5','7','21','219','长城_标清.flv');
insert into Song values('10','踩踩踩','流行','中文','CCC','46','2','90','821','踩踩踩_标清.flv');
insert into Song values('11','初次尝到寂寞','流行','粤语','CCCDJM','20','20','48','401','初次尝到寂寞_标清.flv');
insert into Song values('12','Chewing Gum','流行','韩语','CG','65','11','31','211','Chewing Gum 舞蹈版_标清.flv');
insert into Song values('13','曾经的你','摇滚','中文','CJDN','96','31','201','1512','曾经的你_标清.flv');
insert into Song values('14','Call Me Baby','流行','中文','CMB','27','12','80','1000','Call Me Baby 中文版_标清.flv');
insert into Song values('15','潮湿的心','流行','中文','CSDX','113','12','32','333','潮湿的心_标清.flv');
insert into Song values('16','春天的故事','流行','中文','CTDGS','22','5','56','322','春天的故事_标清.flv');
insert into Song values('17','点豆豆','流行','中文','DDD','33','12','55','841','点豆豆_标清.flv');
insert into Song values('18','大地','摇滚','粤语','DD','5','21','48','416','大地_标清.flv');
insert into Song values('19','等你等了那么久','流行','中文','DNDLNMJ','69','21','121','931','等你等了那么久_标清.flv');
insert into Song values('20','东南西北风','流行','中文','DNXBF','113','22','98','511','东南西北风_标清.flv');
insert into Song values('21','董小姐','民谣','中文','DXJ','78','50','184','1652','董小姐 巡演版_标清.flv');
insert into Song values('22','大约在冬季','流行','中文','DYZDJ','70','44','177','1521','大约在冬季_标清.flv');
insert into Song values('23','Expection','摇滚','英文','E','37','9','32','311','Expection_标清.flv');
insert into Song values('24','Espiritu del Aire','流行','西班牙语','EDA','28','15','79','144','E Nomine - Espiritu del Aire_标清.flv');
insert into Song values('25','Endless Love','流行','英文','EL','59','8','15','122','Endless Love_标清.flv');
insert into Song values('26','E lucevan le stelle','蓝调','意大利语','ELLS','43','5','10','100','E lucevan le stelle  (Jonas Kaufmann) 2010_标清.flv');
insert into Song values('27','E TU COME STAI ','流行','意大利语','ETCS','29','6','101','244','E TU COME STAI_标清.flv');
insert into Song values('28','风含情水含笑','流行','中文','FHQSHX','102','11','51','516','风含情水含笑_标清.flv');
insert into Song values('29','翻篇','流行','中文','FP','9','33','98','521','翻篇_标清.flv');
insert into Song values('30','浮诛','古风','中文','FZ','107','33','121','1021','浮诛 官方版2_标清.flv');
insert into Song values('31','干杯','摇滚','中文','GB','93','19','59','511','干杯_标清.flv');
insert into Song values('32','刚刚好','流行','中文','GGH','98','98','459','2661','刚刚好_标清.flv');
insert into Song values('33','滚滚红尘','流行','中文','GGHC','16','12','31','291','滚滚红尘_标清.flv');
insert into Song values('34','感觉自己萌萌哒','流行','中文','GJZJMMD','44','14','69','641','感觉自己萌萌哒_标清.flv');
insert into Song values('35','高山青','乡村','中文','GSQ','39','3','18','200','高山青_标清.flv');
insert into Song values('36','怪胎秀','流行','中文','GTX','106','19','69','706','怪胎秀 官方版1_标清.flv');
insert into Song values('37','观众','流行','中文','GZ','99','66','189','1022','观众_标清.flv');
insert into Song values('38','公主披风','流行','中文','GZPF	','74','9','41','313','公主披风_标清.flv');
insert into Song values('39','花儿为什么这样红','乡村','中文','HEWSMZYH','82','7','23','211','花儿为什么这样红_标清.flv');
insert into Song values('40','皇后大道东','流行','粤语','HHDDD','49','2','15','121','皇后大道东_标清.flv');
insert into Song values('41','海阔天空','流行','粤语','HKTK','5','39','151','1599','海阔天空_标清.flv');
insert into Song values('42','何日君再来','流行','中文','HRJZL','20','12','39','411','何日君再来_标清.flv');
insert into Song values('43','荷塘月色','流行','中文','HTYS','30','11','41','511','荷塘月色_标清.flv');
insert into Song values('44','好想你','流行','中文','HXN','114','24','79','983','好想你_标清.flv');
insert into Song values('45','海洋之心','流行','中文','HYZX','17','22','98','896','海洋之心_标清.flv');
insert into Song values('46','I','流行','韩语','I','45','10','34','288','I_标清.flv');
insert into Song values('47','I Believe','流行','中文','IB','112','27','212','1009','I Believe_标清.flv');
insert into Song values('48','I Do','流行','英文','ID','10','15','80','120','Colbie Caillat - I Do_标清.flv');
insert into Song values('49','I Do I Do','流行','韩语','IDID','73','3','121','981','I Do I Do 韩语版_标清.flv');
insert into Song values('50','In My Mind','摇滚','英文','IMM','21','12','21','177','In My Mind_标清.flv');
insert into Song values('51','酒干倘卖无','流行','中文','JGTMW','84','13','45','467','酒干倘卖无 电影版_标清.flv');
insert into Song values('52','Juicy Secret','流行','韩语','JS','34','14','31','189','Juicy Secret_标清.flv');
insert into Song values('53','今天是你的生日','流行','中文','JTSNDSR','22','4','21','198','今天是你的生日_标清.flv');
insert into Song values('54','九月九的酒','乡村','中文','JYJDJ','15','10','38','403','九月九的酒_标清.flv');
insert into Song values('55','精忠报国','流行','中文','JZBG','80','6','31','412','精忠报国_标清.flv');
insert into Song values('56','卡比巴拉的海','民谣','中文','KBBLDH','78','24','101','962','卡比巴拉的海_标清.flv');
insert into Song values('57','空白格','流行','中文','KBG','103','52','201','2051','空白格MV_标清.flv');
insert into Song values('58','开不了心','流行','粤语','KBLX','18','14','48','571','开不了心_标清.flv');
insert into Song values('59','看我72变','流行','中文','KW72B','17','32','111','901','看我72变标清.flv');
insert into Song values('60','狼','摇滚','中文','L','70','10','31','299','狼_标清.flv');
insert into Song values('61','李白','流行','中文','LB','55','45','170','1823','李白_标清.flv');
insert into Song values('62','兰花草','民谣','中文','LHC','113','14','41','302','兰花草_标清.flv');
insert into Song values('63','烈火神盾','流行','中文','LHSD','89','38','144','1211','烈火神盾_标清.flv');
insert into Song values('64','恋西游','古风','中文','LXY','85','39','133','1011','恋西游_标清.flv');
insert into Song values('65','Monster','摇滚','韩语','M','6','35','151','1521','Monster 舞蹈练习版_标清.flv');
insert into Song values('66','模特','流行','中文','MT','55','69','233','1958','模特_标清.flv');
insert into Song values('67','梦驼铃','流行','中文','MTL','32','9','28','188','梦驼铃_标清.flv');
insert into Song values('68','Mi Vida','摇滚','西班牙语','MV','21','6','19','69','Mi Vida_标清.flv');
insert into Song values('69','梦想岛','流行','中文','MXD','74','29','100','901','梦想岛 舞蹈版_标清.flv');
insert into Song values('70','你把我灌醉','流行','中文','NBWGZ','23','51','198','2012','你把我灌醉_标清.flv');
insert into Song values('71','你不知道的事','流行','中文','NBZDDS','90','49','203','2310','王力宏-你不知道的事.mp4');
insert into Song values('72','难念的经','流行','粤语','NLDJ','105','9','26','189','难念的经_标清.flv');
insert into Song values('73','暖暖','流行','中文','NNN','52','24','134','1543','梁静茹-暖暖.mp4');
insert into Song values('74','NoNoNo','流行','韩语','NNN','3','9','31','91','NoNoNo  _标清.flv');
insert into Song values('75','恋曲1990','流行','中文','NQ1990','49','8','21','214','恋曲1990_标清.flv');
insert into Song values('76','你是我的眼','流行','中文','NSWDY','58','23','165','1990','林宥嘉-你是我的眼 .mp4');
insert into Song values('77','negative things','R&B(蓝调）','英文','NT','83','8','36','400','Selwyn Pretorius-Negative Things.mp4');
insert into Song values('78','那些花儿','民谣','中文','NXHE','68','28','127','1667','朴树-那些花儿.mp4');
insert into Song values('79','逆战','摇滚','中文','NZ','107','27','129','1701','张杰-逆战.mp4');
insert into Song values('80','Obsessed','R&B','英文','O','61','3','10','103','Mariah Carey-Obsessed.mp4');
insert into Song values('81','only love','流行','英文','OL','86','11','40','478','Trademark-Only Love.mp4');
insert into Song values('82','one love','R&B','英文','OL','7','13','45','533','Blue-One Love.mp4');
insert into Song values('83','偶尔','流行','中文','OR','23','20','91','1000','邓紫棋-偶尔.mp4');
insert into Song values('84','欧若拉','流行','中文','ORL','111','25','105','1228','张韶涵-欧若拉.mp4');
insert into Song values('85','payphone','摇滚','英文','P','60','8','32','372','Maroon5-payphone.mp4');
insert into Song values('86','漂浮地铁','流行','中文','PFDT','57','9','50','588','李宇春-漂浮地铁.mp4');
insert into Song values('87','pretty girl ','流行','韩语','PG','47','2','7','87','Kara-pretty girl.mp4');
insert into Song values('88','朋友','流行','中文','PY','105','23','121','1330','周华健-朋友.mp4');
insert into Song values('89','披着羊皮的狼','流行','中文','PZYPDL','87','20','80','899','披着羊皮的狼-谭咏麟.mp4');
insert into Song values('90','倾尽天下','古风','中文','QJTX','40','8','32','356','河图-倾尽天下.mp4');
insert into Song values('91','清明雨上','流行','中文','QMYS','95','8','47','543','许嵩-清明雨上.mp4');
insert into Song values('92','Queen Of Rain','流行','英文','QOR','72','6','31','371','Roxette-Queen Of Rain.mp4');
insert into Song values('93','千千阙歌','流行','中文','QQQG','13','20','97','1007','陈慧娴-千千阙歌.mp4');
insert into Song values('94','牵手','流行','中文','QS','84','23','105','1333','苏芮-牵手.mp4');
insert into Song values('95','晴天','流行','中文','QT','108','26','112','1249','周杰伦-晴天.mp4');
insert into Song values('96','日不落','流行','中文','RBL','17','40','189','2200','蔡依林-日不落.mp4');
insert into Song values('97','如果没有你','流行','中文','RGMYN','64','26','120','1445','莫文蔚-如果没有你.mp4');
insert into Song values('98','如果这就是爱情','流行','中文','RGZJSAQ','110','22','100','1199','张靓颖-如果这就是爱情.mp4');
insert into Song values('99','如花','古风','中文','RH','40','5','18','207','河图-如花.mp4');
insert into Song values('100','Rolling in the deep','摇滚','英文','RITD','2','15','78','900','Adele-Rolling In The Deep.mp4');
insert into Song values('101','热情的沙漠','摇滚','中文','RQDSM','100','22','95','1134','热情的沙漠.mp4');
insert into Song values('102','是非题','流行','中文','SFT','31','24','91','992','是非题.mp4');
insert into Song values('103','shes gone','摇滚','英文','SG','76','12','43','521','shes gone.mp4');
insert into Song values('104','世界唯一的你','流行','中文','SJWYDN','11','28','114','1442','世界唯一的你.mp4');
insert into Song values('105','死了都要爱','摇滚','中文','SLDYA','97','37','191','2199','死了都要爱.mp4');
insert into Song values('106','someone like you','流行','英文','SLY','2','15','67','789','someone like you.mp4');
insert into Song values('107','上邪','古风','中文','SY','94','12','52','634','上邪.mp4');
insert into Song values('108','Thousandfold','摇滚','英文','T','25','3','10','98','Thousandfold.mp4');
insert into Song values('109','特别的爱给特别的你','流行','中文','TBDAGTBDN','91','11','50','578','特别的爱给特别的你.mp4');
insert into Song values('110','童话','流行','中文','TH','36','29','138','1552','童话.mp4');
insert into Song values('111','take me to your heart ','流行','英文','TMTYH','63','18','71','801','take me to your heart.mp4');
insert into Song values('112','她说','流行','中文','TS','51','20','96','1120','她说.mp4');
insert into Song values('113','天下','流行','中文','TX','107','29','132','1445','天下.mp4');
insert into Song values('114','u','流行','韩语','U','81','2','5','56','u.mp4');
insert into Song values('115','ugly ','流行','韩语','U','1','3','9','92','ugly .mp4');
insert into Song values('116','unbelievable','摇滚','英文','U','75','1','4','45','unbelievable.mp4');
insert into Song values('117','unmistakable','流行','英文','U','8','5','19','200','unmistakable.mp4');
insert into Song values('118','Us Against The World','pop','英文','UATW','88','6','30','344','Us Against The World.mp4');
insert into Song values('119','venus','pop','英文','V','50','3','17','198','venus.mp4');
insert into Song values('120','Valentines Day','流行','英文','VD','54','5','19','276','Valentines Day.mp4');
insert into Song values('122','vision of love','R＆B','英文','VOL','61','4','20','231','vision of love.mp4');
insert into Song values('123','问','流行','中文','W','16','29','142','1600','问.mp4');
insert into Song values('124','What are words','流行','英文','WAW','14','10','47','513','What are words.mp4');
insert into Song values('125','我的歌声里','流行','中文','WDGSL','71','36','160','1890','我的歌声里.mp4');
insert into Song values('126','吻得太逼真','流行','中文','WDTBZ','109','24','100','1240','吻得太逼真.mp4');
insert into Song values('127','无关风月','古风','中文','WGFY','101','11','50','598','无关风月.mp4');
insert into Song values('128','想把你写成一首歌','流行','中文','XBNXCYSG','93','26','89','981','好好(想把你写成一首歌)_标清.flv');
insert into Song values('129','喜欢你','流行','中文','XHN','5','25','110','1222','喜欢你.mp4');
insert into Song values('130','相见恨晚','流行','中文','XJHW','67','34','145','1511','相见恨晚.mp4');
insert into Song values('131','想你的夜','流行','中文','XNDY','38','25','103','1100','想你的夜.mp4');
insert into Song values('132','小情歌','流行','中文','XQG','77','39','189','2000','小情歌.mp4');
insert into Song values('133','下一个天亮','流行','中文','XYGTL','35','31','143','1602','下一个天亮.mp4');
insert into Song values('134','星语心愿','流行','中文','XYXY','104','41','200','2432','星语心愿.mp4');
insert into Song values('135','You Are Not Alone','流行','英文','YANA','62','23','90','1002','You Are Not Alone.mp4');
insert into Song values('136','洋葱','流行','中文','YC','103','29','122','1432','洋葱.mp4');
insert into Song values('137','月光','古风','中文','YG','41','23','87','992','月光.mp4');
insert into Song values('138','烟花易冷','流行','中文','YHYL','108','25','111','1334','烟花易冷.mp4');
insert into Song values('139','YOU RAISE ME UP','流行','英文','YRMU','79','18','75','883','YOU RAISE ME UP.mp4');
insert into Song values('140','一直很安静','流行','中文','YZHAJ','4','26','132','1553','一直很安静.mp4');
insert into Song values('141','左边','流行','中文','ZB','99','23','128','1449','左边.mp4');
insert into Song values('142','最初的梦想','流行','中文','ZCDMX','31','35','171','2080','最初的梦想.mp4');
insert into Song values('143','真的爱你','摇滚','中文','ZDAN','5','28','115','1378','真的爱你.mp4');
insert into Song values('144','征服','流行','中文','ZF','66','23','101','1120','征服.mp4');
insert into Song values('145','醉飞霜','古风','中文','ZFS','42','12','54','670','醉飞霜.mp4');
insert into Song values('146','最重要的决定','流行','中文','ZZYDJD','31','30','120','1578','最重要的决定.mp4');






insert into Comment values('1','好听','1');
insert into Comment values('2','我爱你','2');
insert into Comment values('3','歌曲的开头令人有听下去的感觉','3');
insert into Comment values('4','每个人都有自己喜欢的风格','4');
insert into Comment values('5','我想你啦','5');
insert into Comment values('6','么么哒','6');
insert into Comment values('7','爱你是我的荣幸','7');
insert into Comment values('8','他在灯火阑珊处','8');
insert into Comment values('9','有一个人在等我','9');
insert into Comment values('10','喜欢你','10');
insert into Comment values('11','歌曲是我的灵魂','11');
insert into Comment values('12','.我想在五十年之后我一定还是像现在一样爱你','12');
insert into Comment values('13','我不要短暂的温存，只要你一世的陪伴','13');
insert into Comment values('14','只因你太美好令我无法坦白说出我爱你','14');
insert into Comment values('15','好听','15');
insert into Comment values('16','我爱你','16');
insert into Comment values('17','歌曲的开头令人有听下去的感觉','17');
insert into Comment values('18','每个人都有自己喜欢的风格','18');
insert into Comment values('19','我想你啦','19');
insert into Comment values('20','么么哒','20');
insert into Comment values('21','爱你是我的荣幸','21');
insert into Comment values('22','他在灯火阑珊处','22');
insert into Comment values('23','有一个人在等我','23');
insert into Comment values('24','喜欢你','24');

insert into Client values('1','北京','a','联想');
insert into Client values('2','上海','b','戴尔');
insert into Client values('3','上海','c','惠普');

insert into C_Song values('1','1','1');
insert into C_Song values('2','1','2');
insert into C_Song values('3','1','3');
insert into C_Song values('4','1','4');
insert into C_Song values('5','1','5');
insert into C_Song values('6','1','6');
insert into C_Song values('7','1','7');
insert into C_Song values('8','1','8');
insert into C_Song values('9','1','9');
insert into C_Song values('10','2','10');
insert into C_Song values('11','2','1');
insert into C_Song values('12','2','2');
insert into C_Song values('13','2','3');
insert into C_Song values('14','2','4');
insert into C_Song values('15','2','5');
insert into C_Song values('16','2','6');
insert into C_Song values('17','2','7');
insert into C_Song values('18','2','8');
insert into C_Song values('19','2','9');
insert into C_Song values('20','2','10');
insert into C_Song values('21','3','1');
insert into C_Song values('22','3','2');
insert into C_Song values('23','3','3');
insert into C_Song values('24','3','4');
