import pandas as pd
from pyvis.network import Network

class Node:
    def __init__(self, node_id, label, size, color, title):
        self.node_id = node_id
        self.label = label
        self.size = size
        self.color = color
        self.title = title


class Edge:
    def __init__(self, source, target, weight, title, color="#2253B5"):
        self.source = source
        self.target = target
        self.weight = weight
        self.title = title
        self.color = color


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node_id, label, size, color, title):
        node = Node(node_id, label, size, color, title)
        self.nodes.append(node)

    def add_edge(self, source, target, weight, title, color="#2253B5"):
        edge = Edge(source, target, weight, title, color)
        self.edges.append(edge)

    def visualize(self, filename):
        net = Network(height="770px", width="1600px", directed=True, bgcolor="#0b1d35", font_color="white")
        
        for node in self.nodes:
            net.add_node(node.node_id, label=node.label, size=node.size, color=node.color, title=node.title)

        for edge in self.edges:
            net.add_edge(edge.source, edge.target, width=edge.weight, title=edge.title, color=edge.color)

        net.write_html(filename)


class Yazarlar:
    def __init__(self, yazar_id, yazar_adi, makaleler, makale_sayisi, ortak_yazarlar, ortak_sayisi, dizi):
        self.yazar_id = yazar_id
        self.yazar_adi = yazar_adi
        self.makale_sayisi = makale_sayisi
        self.makaleler = list(makaleler)
        self.ortak_yazarlar = list(ortak_yazarlar)
        self.ortak_sayisi = ortak_sayisi
        self.dizi = dizi

yazarlar_listesi = []
yazar_id_set = {}

dosya_yolu = "PROLAB 3 - GÜNCEL DATASET.xlsx"
df = pd.read_excel(dosya_yolu, header=0)

graph = Graph()

for indeks, satir in df.iterrows():
    yazar_id = satir[0]
    yazar_adi = satir[3]
    makale_adi = satir[5]
    
    if pd.notna(satir[4]):
        string_temiz = satir[4].strip("[]").replace("'", "").strip()
        isim_listesi = string_temiz.split(",")
        isim_listesi.pop(satir[2] - 1)
        isim_listesi = [isim.strip() for isim in isim_listesi if isim.strip()]
    else:
        isim_listesi = []

    if yazar_id not in yazar_id_set:
        yazar = Yazarlar(
            yazar_id=yazar_id,
            yazar_adi=yazar_adi,
            makaleler=[makale_adi],
            makale_sayisi=1,
            ortak_yazarlar=list(set(isim_listesi)),
            ortak_sayisi=len(set(isim_listesi)),
            dizi=isim_listesi
        )
        yazarlar_listesi.append(yazar)
        yazar_id_set[yazar_id] = yazar
    else:
        mevcut_yazar = yazar_id_set[yazar_id]
        mevcut_yazar.makaleler.append(makale_adi)
        mevcut_yazar.makale_sayisi += 1
        yeni_ortaklar = set(isim_listesi) - set(mevcut_yazar.ortak_yazarlar)
        mevcut_yazar.ortak_yazarlar.extend(yeni_ortaklar)
        mevcut_yazar.ortak_sayisi = len(mevcut_yazar.ortak_yazarlar)
        mevcut_yazar.dizi.extend(isim_listesi)

for i in yazarlar_listesi:
    title_list = (
       f"{i.yazar_adi} yazarının bilgileri:\n"
       f"Yazarın id    : {i.yazar_id}\n"
       f"Makale sayısı : {i.makale_sayisi}\n"
       f"Ortak sayısı  : {i.ortak_sayisi}\n"
       f"Makaleler:\n"
       f"{chr(10).join(i.makaleler)}\n"
    )
    boyut = 50 if i.makale_sayisi <= 6 else (100 if i.makale_sayisi <= 9 else 200)
    graph.add_node(i.yazar_id, i.yazar_adi + "\n" + i.yazar_id, boyut, "#2253B5", title_list)

    for j in i.ortak_yazarlar:
        for k in yazarlar_listesi:
            if j == k.yazar_adi:
                ortak_makale_sayisi = i.dizi.count(j)
                graph.add_edge(i.yazar_id, k.yazar_id, ortak_makale_sayisi * 2, f"Ortak Makale Sayısı: {ortak_makale_sayisi}")

        # Ana yazar ile yardımcı yazarların bağlandığı kısım
        yardimci_node_id = f"{j}"
        if yardimci_node_id not in [node.node_id for node in graph.nodes]:
            graph.add_node(yardimci_node_id, j, 20, "#F77808", f"Yardımcı Yazar: {j}")
        yardimci_count = i.dizi.count(j)
        graph.add_edge(i.yazar_id, yardimci_node_id, yardimci_count * 2, f"Yardımcı Bağlantısı: {yardimci_count}", "#F77808")


graph.visualize("graph.html")

with open("graph.html", "r", encoding="utf-8") as file:
    html_content = file.read()


#Web kısmı burada başlıyor
ui_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Graph Visualization</title>
    <style>
        * {
            margin: -1;
            margin-bottom: 10px;
            top: -10px;
            padding: 0;
            box-sizing: border-box;
        }
        html, body {
            height: 100%;
            width: 100%;
            overflow: hidden;
            background-color: #0b1d35;
        }
        .button-container {
            position: fixed;
            top: 10px;
            right: 10px;
            background: rgba(0, 0, 0, 0.6);
            padding: 20px;
            height: 412px;
            border-radius: 15px;
            z-index: 1000;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.4);
            width: 180px;
            color: rgb(255, 255, 255,0.75);
        }
        .button-container label {
            font-size: 17px;
            font-weight: bold;
            color: rgb(255, 255, 255,0.90);
            display: block;
            margin-bottom: 0px;
            text-align: center;
        }
        .button-container button {
            width: 162px;
            padding: 10px;
            margin-bottom: 7px;
            height : 45px;
            border: none;
            border-radius: 10px;
            color: rgb(255, 255, 255,0.90);
            font-size: 14px;
            font-weight: bold;
            background: rgba(255, 99, 71, 0.65);
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            margin-left: -10px;
        }
        .button-container button:hover {
            transform: scale(1.05);
            box-shadow: 0px 6px 8px rgba(255, 99, 71, 0.5);
        }
        .message-box {
            position: fixed;
            top: 10px;
            left: 10px;
            background: rgba(0, 0, 0, 0.6);
            padding: 20px;
            border-radius: 15px;
            z-index: 1000;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.4);
            width: 320px;
            height: 500px;
            overflow-y: auto;
            color: rgb(255, 255, 255,0.75);
            scrollbar-width: thin;
            scrollbar-color: #555 transparent;
        }
        #messageBox {
            height: 410px; 
            overflow-y: auto;
        }
        .message-box::-webkit-scrollbar {
            width: 10px;
        }
        .message-box::-webkit-scrollbar-track {
            background: transparent;
        }
        .message-box::-webkit-scrollbar-thumb {
            background-color: #555;
            border-radius: 10px;
            border: 2px solid transparent;
        }
        .message-box label {
            font-size: 16px;
            font-weight: bold;
            color: rgb(255, 255, 255,0.90);
            display: block;
            margin-bottom: 10px;
            text-align: center;
        }
        .message-box p {
            font-size: 14px;
            margin: 5px 0;
            color: rgb(255, 255, 255,0.75);
        }
        .clear-button {
           position: fixed;
           margin-top: 480px;
           margin-left: 0px;
           width: 280px;
           weight : 20px
           padding: 10px;
           border: none;
           border-radius: 10px;
           background: rgba(0, 128, 128, 0.65);
           color: rgb(255, 255, 255,0.75);
           font-size: 14px;
           font-weight: bold;
           cursor: pointer;
           transition: transform 0.2s, box-shadow 0.2s;
        }
        .clear-button:hover {
           transform: scale(1.05);
           box-shadow: 0px 6px 8px rgba(0, 128, 128, 0.65);
        }
        .controls-container {
            position: fixed;
            right: 10px;
            margin-top: 435px;
            background: rgba(0, 0, 0, 0.6);
            padding: 10px;
            height: 298px;
            border-radius: 15px;
            z-index: 1000;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.4);
            width: 180px;
            color: rgb(255, 255, 255,0.75);
        }
        .controls-container label {
            font-size: 14px;
            font-weight: bold;
            color: rgb(255, 255, 255,0.75);
            display: block;
            margin-bottom: 10px;
            text-align: center;
        }
        .controls-container div {
            margin-bottom: 10px;
        }
        .controls-container input[type="range"] {
            width: 100%;
        }
        .controls-container span {
            font-size: 12px;
            color: rgb(255, 255, 255,0.75);
        }
        .controls-container button {
            width: 100%;
            padding: 5px;
            margin-top: -5px;
            border: none;
            border-radius: 10px;
            color: rgb(255, 255, 255,0.75);
            font-size: 14px;
            font-weight: bold;
            background: rgba(0, 128, 0, 0.65);
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .controls-container button:hover {
            transform: scale(1.05);
            box-shadow: 0px 6px 8px rgba(0, 128, 0, 0.5);
        }
        .input-box {
            position: fixed;
            top: 513px;
            left: 10px;
            width: 320px;
            height: 209px;
            background: rgba(0, 0, 0, 0.6);
            padding: 20px;
            border-radius: 15px;
            z-index: 1000;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.4);
            color: rgba(255, 255, 255, 0.75);
            display: none;
        }
        .input-box input {
            width: 100%;
            margin-bottom: 10px;
            padding: 8px;
            border-radius: 5px;
            background: rgba(0, 0, 0, 0.3);
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.4);
            color: rgba(255, 255, 255, 0.75);
            border: none;
            font-size: 14px;
        }
        .input-box button {
            
            width: 100%;
            padding: 5px;
            border: none;
            margin-bottom: 15px;
            border-radius: 10px;
            background: rgba(0, 128, 128, 0.65);
            color: rgba(255, 255, 255, 0.75);
            font-size: 14px;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .input-box button:hover {
            transform: scale(1.05);
            box-shadow: 0px 6px 8px rgba(0, 128, 128, 0.65);
        }
    </style>
</head>
<body>
    <div class="button-container">
        <label>İsterler</label>
        <button onclick="ister1fonk()">İster 1</button>
        <button onclick="ister2fonk()">İster 2</button>
        <button onclick="ister3fonk()">İster 3</button>
        <button onclick="ister5fonk()">İster 5</button>
        <button onclick="ister6fonk()">İster 6</button>
        <button onclick="ister7fonk()">İster 7</button>        
        
    </div>

    <div class="message-box">
        <label>Çıktılar</label>
        <div id="messageBox"></div>
        <button class="clear-button" onclick="mesajlariTemizle()">Tümünü Temizle</button>
    </div>
    
    <div class="controls-container">
        <label>Fizik Kontrolleri</label>
        <div>
            <label for="centralGravityRange">Merkez Çekim:</label>
            <input type="range" id="centralGravityRange" min="-20" max="20" value="0" step="1" oninput="fizigiGuncelle('centralGravity', this.value)">
            <span id="centralGravityValue">0</span>
        </div>
        <div>
            <label for="springLengthRange">Yay Uzunluğu:</label>
            <input type="range" id="springLengthRange" min="10" max="3000" value="200" step="10" oninput="fizigiGuncelle('springLength', this.value)">
            <span id="springLengthValue">200</span>
        </div>
        <div>
            <label for="springConstantRange">Yay Sabiti:</label>
            <input type="range" id="springConstantRange" min="0.1" max="10" value="1" step="0.1" oninput="fizigiGuncelle('springConstant', this.value)">
            <span id="springConstantValue">1</span>
        </div>
        <button onclick="fizikAcKapa()">Hareketi Durdur</button> 
    </div>

    <div id="textInputContainer" class="input-box">
        <input type="text" id="input1" placeholder="Birinci Giriş">
        <input type="text" id="input2" placeholder="İkinci Giriş">
        <button onclick="inputOnayla()">Gönder</button>
        <button onclick="inputKapat()">Vazgeç</button>
    </div>

    <script>
    
        function mesajlariTemizle() {
            const messageBox = document.getElementById('messageBox');
            messageBox.innerHTML = '';
            updateMessage('Tüm mesajlar silindi.');
        }
        
        let fizikDurumu = true;

        function fizikAcKapa() {
            fizikDurumu = !fizikDurumu;
            network.setOptions({
                physics: {
                    enabled: fizikDurumu
                }
            });
            const button = document.querySelector(".controls-container button");
            button.textContent = fizikDurumu ? "Hareketi Durdur" : "Hareketi Başlat";
        }
        
        function fizigiGuncelle(setting, value) {
            document.getElementById(setting + 'Value').textContent = value;

            network.setOptions({
                physics: {
                    forceAtlas2Based: {
                        [setting]: parseFloat(value)
                    },
                    solver: 'forceAtlas2Based'
                }
            });
        }
        

        let aktifFonk = '';
        
        function inputGoster(singleInput = false) {
            const container = document.getElementById('textInputContainer');
            container.style.display = 'block';
            
            if (singleInput) {
                document.getElementById('input2').style.display = 'none';
            } else {
                document.getElementById('input2').style.display = 'block';
            }
        }
        
        function inputKapat() {
            document.getElementById('textInputContainer').style.display = 'none';
            inputTemizle()
        }
        
        function inputTemizle() {
            document.getElementById('input1').value = '';
            document.getElementById('input2').value = '';
        }
        
        function inputOnayla() {
            const input1 = document.getElementById('input1').value;
            const input2 = document.getElementById('input2').value;
            const messageBox = document.getElementById('messageBox');
            const newMessage = document.createElement('p');
        
            
if (aktifFonk === 'ister1') {

    const mesafe = {};
    const onceki = {};
    const gecilenler = new Set();

    nodes.forEach(node => {
        mesafe[node.id] = Infinity;
        onceki[node.id] = null;
    });
    mesafe[input1] = 0;

    while (gecilenler.size < nodes.length) {
        let gecilmeyenler = Object.keys(mesafe).filter(n => !gecilenler.has(n));
        if (gecilmeyenler.every(n => mesafe[n] === Infinity)) {
            break; // Tüm kalan düğümler ulaşılamaz durumda
        }
        
        let mevcutDugum = gecilmeyenler.reduce((a, b) => mesafe[a] < mesafe[b] ? a : b);
        gecilenler.add(mevcutDugum);

        edges.forEach(edge => {
            // Hem yönleri kontrol et (çift yönlü kenarlar)
            if (edge.from === mevcutDugum || edge.to === mevcutDugum) {
                const komsular = edge.from === mevcutDugum ? edge.to : edge.from;
                if (!gecilenler.has(komsular)) {
                    const agirlik = edge.weight || 1; // Kenar ağırlığı varsayılan olarak 1
                    const alt = mesafe[mevcutDugum] + agirlik;
                    if (alt < mesafe[komsular]) {
                        mesafe[komsular] = alt;
                        onceki[komsular] = mevcutDugum;
                    }
                }
            }
        });
    }

    // Hedef düğüm kontrolü (ulaşılamazsa)
    if (mesafe[input2] === Infinity) {
        newMessage.textContent = `İster 1 girdiler: ${input1}, ${input2}. Hedef düğüme ulaşılamıyor.`;
        return;
    }

    let gidilenYol = [];
    let adimlar = input2;
    while (adimlar !== null && adimlar !== undefined) { // Sonsuz döngüyü önlemek için kontrol
        gidilenYol.unshift(adimlar);
        adimlar = onceki[adimlar];
    }

    const degisenKenar = [];
    edges.forEach(edge => {
        if (
            (gidilenYol.includes(edge.from) && gidilenYol.includes(edge.to)) &&
            (onceki[edge.to] === edge.from || onceki[edge.from] === edge.to)
        ) {
            degisenKenar.push({ id: edge.id, color: { color: 'red' }, width: edge.weight * 2 });
        }
    });
    edges.update(degisenKenar);
    network.redraw();

    newMessage.textContent = `İster 1 girdiler: ${input1}, ${input2}. En kısa yol kırmızı olarak gösterildi.\nEn kısa yol düğümleri: ${gidilenYol.join(' -> ')}`;
}



          else if (aktifFonk === 'ister2') {
                newMessage.textContent = `İster 2 girdiler: ${input1}`;
                nodes.forEach((node) => {
    if (node.id === input1) {
        const bagliDugumler = [];
        edges.forEach((edge) => {
            if (edge.from === node.id) {
                bagliDugumler.push(edge.to);
            } else if (edge.to === node.id) {
                bagliDugumler.push(edge.from);
            }
        });

        let message = `Bulundu: ${node.id}<br>Bağlı düğümler:<br>`;
        bagliDugumler.forEach((baglanmisDugum) => {
            message += `${baglanmisDugum}<br>`;
        });

        newMessage.innerHTML = message;
        kontrol = true;
    }
});


            } else if (aktifFonk === 'ister3') {
                newMessage.textContent = `İster 3 girdiler: ${input1}`;
            }
            else if (aktifFonk === 'ister5') {
                newMessage.textContent = `İster 5 girdiler: ${input1}`;
                            nodes.forEach((node) => {
             if (node.id=== input1) {
                     const kenarSayisi = edges.get({
                filter: (edge) => edge.from === node.id || edge.to === node.id
                  }).length;
            newMessage.textContent = `Bulundu:${node.id} Kenar sayısı: ${kenarSayisi}`;
            kontrol = true;
               }
             });
            }
            else if(aktifFonk === 'ister7')
            {
            nodes.forEach((node) => {
            if (node.id === input1) {
                // En uzun yolu bulmak için DFS (Derinlik Öncelikli Arama) fonksiyonu
                function enUzunYol(nodeId, gecilenler) {
                    gecilenler.add(nodeId);
                    let enUzun = 0;
                    let uzunYol = [nodeId];
        
                    edges.forEach((edge) => {
                        const neighbor = edge.from === nodeId ? edge.to : edge.to === nodeId ? edge.from : null;
                        if (neighbor && !gecilenler.has(neighbor)) {
                            const result = enUzunYol(neighbor, new Set(gecilenler));
                            if (result.length > enUzun) {
                                enUzun = result.length;
                                uzunYol = [nodeId, ...result];
                            }
                        }
                    });
        
                    return uzunYol;
                }
        
                const uzunYol = enUzunYol(node.id, new Set());
        
                const degisenKenar = [];
                edges.forEach((edge) => {
            if ((uzunYol.includes(edge.from) && uzunYol.includes(edge.to)) &&
                (uzunYol.indexOf(edge.from) === uzunYol.indexOf(edge.to) - 1 || 
                uzunYol.indexOf(edge.to) === uzunYol.indexOf(edge.from) - 1)) {
                    degisenKenar.push({ id: edge.id, color: { color: 'red' } ,width:15 });
            } 
        });
        edges.update(degisenKenar);
        
        // Ağ yapısını tekrar çiz
        network.redraw();
        
        // Mesaj kutusuna ekleyin
        let message = `Bulundu: ${node.id}<br>En Uzun Yol:<br>`;
        uzunYol.forEach((pathNode) => {
            message += `${pathNode}<br>`;
        });
        
        newMessage.innerHTML = message;
                kontrol = true;
            }
        });
            
            
            }            
        
            messageBox.appendChild(newMessage);
            inputTemizle();
            inputKapat();
        }
        
        function ister2fonk() {
            aktifFonk = 'ister2';
            inputGoster(true);
        }
        
        function ister3fonk() {
            aktifFonk = 'ister3';
            inputGoster(true);
        }
        
        function ister1fonk() {
            aktifFonk = 'ister1';
            inputGoster(false);
        }

        function ister5fonk() {
            aktifFonk = 'ister5';
            inputGoster(true);
        }
        function ister7fonk() {
            aktifFonk = 'ister7';
            inputGoster(true);
        }

                function ister6fonk() {
                    aktifFonk = 'ister6';
            enCokIsbirligi();
        }

        function enCokIsbirligi() {
            const isbirligi = {};
            
            edges.forEach(edge => {
                isbirligi[edge.from] = (isbirligi[edge.from] || 0) + 1;
                isbirligi[edge.to] = (isbirligi[edge.to] || 0) + 1;
            });

            let isbirligiSayisi = 0;
            let yazarinAdi = '';

            for (const nodeId in isbirligi) {
                if (isbirligi[nodeId] > isbirligiSayisi) {
                    isbirligiSayisi = isbirligi[nodeId];
                    const node = nodes.get(nodeId);
                    yazarinAdi = node ? node.label : 'Bilinmiyor';
                }
            }

            const newMessage = document.createElement('p');
            newMessage.textContent = `En çok ortağa sahip yazarın adı: ${yazarinAdi}, Ortak sayısı: ${isbirligiSayisi}`;
            document.getElementById('messageBox').appendChild(newMessage);
        }

    </script>
</body>
</html>

"""

# HTML kodlarını ekleme kısmı
html_content = html_content.replace("<body>", f"<body>{ui_html}")

#HTML dosyasını kaydetme kısmı
with open("graph.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("graph.html dosyasına kaydedildi.")