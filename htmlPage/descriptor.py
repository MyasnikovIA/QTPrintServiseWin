svcdescription = """
Сервис предназначен для доступа к локальным ресурсам рабочей станции (Принтеры , сканеры , и.т.д),
через крос-доменные запросов на хоси 127.0.0.1 (localhost)
URL:  http://127.0.0.1:%s/
Пример обращение к сервису через JS:
BarsPySend= function(messageObject,FunCallBack ){
    var host = "http://127.0.0.1:51003/";
    var cspBindRequestCall = new XMLHttpRequest();
    cspBindRequestCall.timeout = 5000;
	cspBindRequestCall.ontimeout = function (e) {
       console.log("Print to QTPrintService time out")
    };
    cspBindRequestCall.open('GET',host, true);
    if (typeof FunCallBack === 'function'){ 
         cspBindRequestCall.onreadystatechange = function() {
         if (this.readyState == 4 && this.status == 200) {
            if (typeof FunCallBack === 'function'){
		    try {
				FunCallBack(JSON.parse(decodeURIComponent(this.responseText)));
			} catch (err) {
			    FunCallBack(decodeURIComponent(this.responseText));
			}
          }
         };
       };
    }
    cspBindRequestCall.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    if (typeof messageObject == "object"){
        for (var prop in messageObject) {
           cspBindRequestCall.setRequestHeader("X-My-"+prop, encodeURI(messageObject[prop]));
        }
    } else{
        cspBindRequestCall.setRequestHeader("X-My-message", encodeURI(messageObject));
    }
    cspBindRequestCall.send();
    return cspBindRequestCall; 
}
BarsPySend({"GetPrinterList":1},function(dat){console.log(dat);}) // получить список принтеров установленных в системе
BarsPySend({"Print":"<h1>Привет Мир-HelloWorld</h1>","widthPage":300,"heightPage":100,"PrinterName":"Brother QL-810W"},function(dat){console.log(dat);})
BarsPySend({"Print":"<h1>Привет Мир-HelloWorld</h1>"+Date(Date.now()).toString()}) // отправека на печать без получения ответа
BarsPySend({"Print":"<h1>Привет Мир-HelloWorld</h1>"+Date(Date.now()).toString(),"Filename":"C:/AppServ/www/QTPrintServiseWin/dist/ssss.pdf"}) // печать в файл
          

    """