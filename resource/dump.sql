BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text,      phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Kim','Kim@naver.com','010-0000-0000','Kim.com','2021-03-18 22:29:23');
INSERT INTO "users" VALUES(2,'Park','Park@daum.net','010-1111-1111','Park.com','2021-03-18 22:29:23');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com',' 010-2222-2222','Lee.com','2021-03-18 22:29:23');
INSERT INTO "users" VALUES(4,'Cho','Cho@naver.com',' 010-2222-2222','Cho.com','2021-03-18 22:29:23');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@naver.com',' 010-2222-2222','Yoo.com','2021-03-18 22:29:23');
COMMIT;
