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

insert into Client values('1','北京','a','联想');
insert into Client values('2','上海','b','戴尔');
insert into Client values('3','上海','c','惠普');
