// 설치한 express 를 등록한다.
var express = require("express");
var app = express();

// localhost:3000 으로 접속하면 아래에서 받는다. (GET 방식만 유용)
app.get("/", function(req, res) {
  res.send("Hello World!!!!!!!!!!!!!!!!!!!!!");
});

// [출처] [Node.js] express 로 웹서버 생성 + 정적파일(css, js 등) 설정|작성자 demonic

// hello.all.js 참조
app.use("/lib", express.static(__dirname + "/Project/lib/"));
//
// 구글 인증 테스트 페이지
app.get("/auth/google", function(req, res) {
  res.sendFile(__dirname + "/Project/auth/google.html");
});

// 구글 인증 콜백
app.get("/auth/callbackGoogle", function(req, res) {
  res.sendFile(__dirname + "/Project/auth/google.html");
});
//

// 사용할 포트번호.
var port = 3000;
app.listen(port, function() {
  console.log("Example app listening on port 3000!");
});
