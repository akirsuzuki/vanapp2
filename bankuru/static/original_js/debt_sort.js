<script type="text/javascript">

	$(function() {
		// リストの初期化
		var arrId = [];		// ID
		var arrTr = [];		// DOM要素
		var arrBankname = [];	// 銀行名
		var arrBalance = [];	// 残高（現在）

		// リストに値を格納
		$("#debt_list tr").each(function(i) {
			// ID（元の順番）を格納
			arrId.push(i);

			// DOM要素を格納
			arrTr.push($(this));

			// 銀行（tdの0番目の文字列）を格納
			arrBankname.push($(this).find("td").eq(0).text());

			// 残高（tdの5番目の文字列の数値化）を格納
			arrBalance.push($(this).find("td").eq(5).text() * 1);
		});

		// 名前でソート
		var sortBankname = function(a, b) {
			var aBankname = arrBankname[a];
			var bBankname = arrBankname[b];
			return aBankname > bBankname ? 1 : -1;
		};

		// 残高でソート
		var sortBalance = function(a, b) {
			var aBalance = arrBalance[a];
			var bBalance = arrBalance[b];
			return aBalance < bBalance ? 1 : -1;
		};

		// ソートを反映
		var reflect = function() {
			// tbody を空に
			$("#debt_list").empty();

			// tr を id の順に追加
			$.each(arrId, function(i, id) {
				$("#debt_list").append(arrTr[id]);
			});
		};

		// ［銀行名でソート］ボタンのイベントを登録
		$("#btnSortBankname").click(function() {
			arrId.sort(sortBankname);	// 名前でソート
			reflect();	// ソートを反映
		});

		// ［残高でソート］ボタンのイベントを登録
		$("#btnSortBalance").click(function() {
			arrId.sort(sortBalance);	// 残高でソート
			reflect();	// ソートを反映
		});
	});
</script>
