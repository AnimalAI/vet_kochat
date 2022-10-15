var mysql = require("mysql"); // mysql 모듈을 불러옵니다.

// 커넥션을 정의합니다.
// RDS Console 에서 본인이 설정한 값을 입력해주세요.
var connection = mysql.createConnection({
    host: 'aai-rds.cicyr4glvvx9.ap-northeast-2.rds.amazonaws.com',
    user: 'admin',
    port: '3306',
    password: 'abcd1234',
    database: 'aai'
});

//connection.connect(function(err) {
//  if (err) {
//    throw err; // 접속에 실패하면 에러를 throw 합니다.
//  } else {
//    // 접속시 쿼리를 보냅니다.
//    var sql = "SELECT * FROM expect_diagnoses"
//    connection.query(sql, function(err, rows, fields) {
//      console.log(rows); // 결과를 출력합니다!
//    });
//    connection.end();
//  }
//});

    var today = new Date();
    var year = today.getFullYear();
    var month = ('0' + (today.getMonth() + 1)).slice(-2);
    var day = ('0' + today.getDate()).slice(-2);
    var dateString = year + '-' + month  + '-' + day;

    var hours = ('0' + today.getHours()).slice(-2);
    var minutes = ('0' + today.getMinutes()).slice(-2);
    var seconds = ('0' + today.getSeconds()).slice(-2);
    var timeString = hours + ':' + minutes  + ':' + seconds
    var diagnose = "바보"

    connection.connect(function(err) {
      if (err) {
        throw err; // 접속에 실패하면 에러를 throw 합니다.
      } else {
        // 접속시 쿼리를 보냅니다.
        var sql = "INSERT INTO expect_diagnoses (pets_pet_serial, pets_members_member_serial, diag_date, diag_time, diag_ds_name)";
        sql += " VALUES (8,1,"
        sql += "'" + dateString + "'"
        sql += ",'" + timeString + "',"
        sql += "'"+diagnose+"');"

        connection.query(sql, function(err, rows, fields) {
          console.log(rows); // 결과를 출력합니다!
        });
        connection.end();
      }
    });