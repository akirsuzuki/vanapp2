<script type="text/javascript">
	{/* カンマ区切りをなくして数値として扱うためのスクリプト */}
  function removeComma(value) {
    var num = value.replace(/,/g, "");    
    return parseInt(num);
  }


  {/* //銀行別の小計を出すスクリプト */}
  window.onload = function(){
      //ターゲットとなるテーブルを取得
      var tbl = document.getElementsByTagName("table")[0];
      //初期化
      var sumBalance = 0;
      //次のループ内で使用する変数の宣言
      var nowID, nowName, nextID, nextName, newRow;
      //テーブルの1行目～最終行までに関するループ
      for(var r = 1; r <= tbl.rows.length-1; r++){
          //今走査中の行の要素を取得
          nowID = tbl.rows[r].cells[0].innerHTML;
          //次に走査する行が最終行以下であれば
          if(r+1 <= tbl.rows.length-1){
              //次に走査する行の ID と name を取得
              nextID = tbl.rows[r+1].cells[0].innerHTML;
              // nextName = tbl.rows[r+1].cells[1].innerHTML;
          //最終行の場合
          }else{
              //次の ID と name に長さ0の文字列でも代入
              // nextID = nextName = "";
              nextID = "";
          }
          //今走査中の行の Balance を合計金額 sumBalance に加算
          sumBalance += parseFloat(removeComma(tbl.rows[r].cells[5].innerHTML));
          //もし今と次の ID または name が違っていれば
          // if(nowID != nextID || nowName != nextName){
          if(nowID != nextID){
              //次の行に１行挿入
              newRow = tbl.insertRow(r+1);
              //挿入した行にセル(列)を挿入
              newRow.insertCell(0).innerHTML = nowID + "合計";
              newRow.insertCell(1);
              newRow.insertCell(2);
              newRow.insertCell(3);
              newRow.insertCell(4);
              newRow.insertCell(5).innerHTML = sumBalance;
              //合計金額 sumBalance を 0 に戻す
              sumBalance = 0;
              //走査行を１行進ませる(１行挿入したため)
              r++;
          }
      }
  };
</script>