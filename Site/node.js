let tg = window.Telegram.WebApp;
tg.expand();
tg.MainButton.hide();
tg.MainButton.textColor = "#FFFFFF"; //изменяем цвет текста кнопки
tg.MainButton.color = "#2cab37"; //изменяем цвет бэкграунда кнопки
tg.MainButton.setText("Отправить форму");
tg.MainButton.show();

Telegram.WebApp.onEvent("mainButtonClicked", function(){
    let data = {};

    var e = document.getElementById("Home_model");
    var text = e.options[e.selectedIndex].text;
    data["Home_model"] = text

    
    e = document.getElementById("mont_type");
    text = e.options[e.selectedIndex].text;
    data["mont_type"] = text;


    e = document.getElementById("obr_type");
    text = e.options[e.selectedIndex].text;
    data["obr_type"] = text;

    

    data["user"] = document.getElementById("user").value;


    data["worker"] = document.getElementById("worker").value;


    data["mounter"] = document.getElementById("mounter").value;


    data["adress"] = document.getElementById("adress").value;


    data["obr_type"] = document.getElementById("obr_type").value;


    data["comm"] = document.getElementById("comm").value;

    e = document.getElementById("KS_month");
    text = e.options[e.selectedIndex].text;
    var KS_date = document.getElementById("KS_day").value + "-" + text + "-" + document.getElementById("KS_year").value;
    data["KS_date"] = KS_date;

    e = document.getElementById("Drive_month");
    text = e.options[e.selectedIndex].text;
    var Drive_date = document.getElementById("Drive_day").value + "-" + text + "-" + document.getElementById("Drive_year").value;
    data["drive_date"] = Drive_date;
    
    
    // tg.sendData(data);
    let s = "";
    s += data["user"] + '\n' + data["worker"] + '\n' + data["mounter"] + '\n' + data["drive_date"] + '\n' + data["KS_date"] + '\n' + data["Home_model"] + '\n' + data["mont_type"] + '\n' + data["adress"] + '\n' + data["obr_type"] + '\n' + data["comm"];
    tg.sendData(s);
    // alert(s);
    tg.close();
    

});