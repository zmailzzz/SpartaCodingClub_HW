// 상황에 따라 변경되는 내용을 변수로 지정
// let apiKey = 'AIzaSyBJ0MaYkFDktW9Hbr-vVvtptbhgZlSXKTw';
// let playlistId = 'PLuQtmaviIuYqxtcFGjtECU_vHQSDRStIj';
// let url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='+playlistId+'&key='+apiKey+'&maxResults=50';
let apiKey = "AIzaSyAqeOM2ZmHdwI8lgV75x5D3oplIN_Iw1eo";
let playlistId = "PL3g4-ArZ2i-_HGN_h3xty5rZYxeljb3Xp";
let url =
  "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=" +
  playlistId +
  "&key=" +
  apiKey +
  "&maxResults=50";

// 최대 50개밖에 출력이 안되기 때문에 자동으로 50개 단위로 재접속해서 가져올 수 있도록 설정
function call(nextToken) {
  // (XMLHttpRequest 객체 이용) 페이지를 전환하지 않고 브라우저한테 몰래 이 주소로 접속해서 정보를 가져오라고 시킴
  let req = new XMLHttpRequest();
  let pageToken = "";
  // nextToken이 있으면 토큰명 변경
  if (nextToken) {
    pageToken = "&pageToken=" + nextToken;
  }
  // 변수로 지정한 url 주소로 접속하라고 요청
  req.open("GET", url + pageToken, true);
  // 접속이 끝나고 뭘 해야되는지 정의
  req.onreadystatechange = function(aEvt) {
    // 접속이 끝나면
    if (req.readyState == 4) {
      // 접속이 성공했다면
      if (req.status == 200) {
        // 이 코드 실행. JSON.parse로 만든 객체를 result에 저장
        let result = JSON.parse(req.responseText);
        let items = result.items;
        for (let i = 0; i < items.length; i++) {
          // 비디오아이디를 변수로 지정
          let vid = items[i].snippet.resourceId.videoId;
          // 비디오 아이디 이용 영상 url을 변수로 지정
          let vurl =
            "https://www.youtube.com/watch?v=" +
            vid +
            "&t=2s&index=1&list=PL3g4-ArZ2i-_HGN_h3xty5rZYxeljb3Xp";
          // 영상 제목과 변수로 놓은 url을 쭉 가져옴.
          // '\t': tap 키만큼의 공백
          console.log(items[i].snippet.title + "\t" + vurl);
        }
        // token 하나 다 돌린 뒤 다음페이지 토큰이 있으면 또 다시 콜해서 두번째 토큰 돌림.
        if (result.nextPageToken) {
          call(result.nextPageToken);
        }
        // 접속이 실패하면 이 코드 실행
      } else {
        alert("Error loading page\n");
      }
    }
  };
  // 접속 시작
  req.send(null);
}
