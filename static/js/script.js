

document.getElementById("submitBtn").addEventListener("click", function(event) {
    var viloyat = document.querySelector("input[name='viloyat']").value.trim();
    var shahar = document.querySelector("input[name='shahar']").value.trim();
    var mahalla = document.querySelector("input[name='mahalla']").value.trim();
    var izoh = document.querySelector("input[name='izoh']").value.trim();
    var uy = document.querySelector("input[name='uy']").value.trim();

    if (viloyat === '' || shahar === '' || mahalla === '' || izoh === '' || uy === '') {
        alert("Iltimos, barcha maydonlarni to'ldiring !");
        event.preventDefault();
    }
    var order = document.getElementById("savat_id");
    var pValue = order.textContent.trim();

    if (pValue === "0 UZS"){
        alert("Iltimos mahsulot harid qilib joylashuvni yozing");
        event.preventDefault();
    }
});
document.getElementById("searchForm").addEventListener("submit", function(event) {
    var query = document.querySelector("input[name='q']").value.trim();
    if (query !== '') {
        window.location.href = "/qidiruv/?q=" + encodeURIComponent(query);
    }
    else{
        window.location.href = "/qidiruv/?q=";
    }
});
