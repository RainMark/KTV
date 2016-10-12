use chen;
DROP table C_Song;
drop table Client;
drop table Comment;
drop table Song;
drop table Star;
create table Star(
StarID Varchar(20),
StarName Varchar(50),
StarStyle Char(3),
StarRegion Varchar(50),
StarNameAbridge Varchar(10),
Route Varchar(20),
primary key(StarID)
);

create table Song(
SongID Varchar(20),
SongName Varchar(50),
SongType Varchar(20),
SongLanguage Varchar(10),
SongNameAbridge Varchar(10),
StarID Varchar(20),
SongWeek Long,
SongMonth Long,
SongYear Long,
primary key(SongID),
foreign key(StarID) references Star(StarID)
);

create table Comment(
C_ID Varchar(20),
C_content Varchar(80),
SongID Char(20),
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
