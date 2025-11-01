# 🎓 Akademik İş Birliği Grafiği ve Algoritmalar (Veri Yapıları Projesi)

[cite_start]Bu proje, akademik bir veri seti kullanılarak yazarlar arasındaki iş birliği ilişkilerini modelleyen bir **graf yapısı** oluşturmayı ve bu graf üzerinde çeşitli veri yapısı ile algoritma konseptlerini uygulamayı amaçlamaktadır[cite: 148, 149]. [cite_start]Yazarların düğümleri temsil ettiği ve iş birliğinin kenarlarla gösterildiği bir graf yapısı oluşturulmuştur[cite: 149].

[cite_start]Proje, akademik iş birliği gibi somut bir senaryo üzerinden veri yapılarını uygulamalı bir şekilde öğrenme fırsatı sunmuştur[cite: 150].

## ✨ Temel Özellikler ve Uygulanan İşlevler

[cite_start]Projenin ana veri yapısı graf olup [cite: 166][cite_start], bu yapı üzerinde Nesneye Yönelik Programlama (OOP) mantığı kullanılarak gerekli algoritmalar geliştirilmiştir[cite: 165, 166].

### 📊 Graf Yapısı ve Veri İşleme

* [cite_start]**Düğümler (Node):** Yazarları temsil eder[cite: 149]. [cite_start]Ana yazar düğümleri mavi ile gösterilmiş olup [cite: 157][cite_start], kendisine yardımcı yazar düğümleri bağlıdır[cite: 157].
* [cite_start]**Kenarlar (Edge):** Yazarlar arasındaki iş birliğini gösterir[cite: 149].
* [cite_start]**Ağırlık (Weight):** Kenar ağırlığı, Ana yazar ve yardımcı yazar arasında kaç adet ortak makale yazıldığı analiz edilerek belirlenmiştir[cite: 158].
* [cite_start]**Kullanılan Sınıflar:** Projede 'Node', 'Edge', 'Graph' sınıfları ve veri setindeki bilgileri tutan 'Yazarlar' sınıfı tanımlanmıştır[cite: 169, 171].

### ⚙️ Uygulanan Analiz ve Algoritmalar

Proje kapsamında graf üzerinde aşağıdaki temel analiz ve algoritmalar uygulanmıştır:

* [cite_start]**En Kısa Yol Bulma:** İki yazar arasındaki en kısa yol, ağırlıklara bakılarak **Dijkstra Algoritması** yardımıyla bulunur[cite: 184]. [cite_start]Algoritma hazır kütüphane yardımıyla tasarlanmamıştır[cite: 186].
* [cite_start]**Yazar İş Birlikleri:** Verilen ID'ye ait yazarın tüm yardımcı yazarları listelenir[cite: 187, 188]. [cite_start]Ayrıca bir yazarın sahip olduğu kenar (iş birliği) sayısı hesaplanır[cite: 190, 191].
* [cite_start]**En Çok İş Birliği:** Tüm yazarlar arasında dolaşılarak en çok yardımcı yazara sahip olan yazar bulunur[cite: 192].
* [cite_start]**En Uzun Yol Bulma:** Belirlenen başlangıç noktasından (yazar ID) gidilebilecek en uzun yol sürekli tutulur ve bulunur[cite: 194, 195]. [cite_start]En uzun yol webde kırmızı ile boyanır[cite: 196].

## 💻 Kullanılan Teknolojiler

[cite_start]Proje, temel programlama dilleri olarak Python ve JavaScript tercih edilerek [cite: 151][cite_start], web tabanlı görselleştirme için HTML ve CSS kullanılmıştır[cite: 151, 153].

| Kategori | Teknoloji | Açıklama |
| :--- | :--- | :--- |
| **Backend / Veri İşleme** | **Python** | [cite_start]Graf yapısının oluşturulması, verinin işlenmesi ve algoritma mantığı[cite: 151]. |
| **Veri Aktarımı** | **Pandas** Kütüphanesi | [cite_start]Excel dosyasındaki verilerin (ID, yazar adı, makaleler) okunması ve sınıflara aktarılması[cite: 172]. |
| **Grafiksel Görselleştirme** | **Pyvis** Kütüphanesi | [cite_start]Web tabanlı grafiğin oluşturulması ve çıktının HTML dosyası olarak kaydedilmesi[cite: 173]. |
| **Frontend / Arayüz** | **HTML** ve **CSS** | [cite_start]Butonlar, çıktı ekranı, textboxlar kodlandı; sade ve estetik bir tasarım elde edildi[cite: 175, 176]. |
| **Etkileşim / Hareket** | **JavaScript** | [cite_start]Görselleştirmelerin mantıksal bağlantısı ve animasyonların gerçekleştirilmesi[cite: 153, 179]. |

## ⚙️ Kurulum ve Çalıştırma

[cite_start]Bu projenin genel çalışma mantığı: Python kısmından gerekli bilgileri alır, HTML/CSS kısmında kullanıcıya gösterir ve Javascript kısmında ise hareketlendirir[cite: 168].

1.  **Depoyu Klonlayın:**
    ```bash
    git clone [depo-adresiniz]
    cd [depo-adiniz]
    ```
2.  **Gerekli Python Kütüphanelerini Kurun:**
    ```bash
    pip install pandas pyvis
    ```
3.  **Proje Çalıştırma:**
    * Python betiğini çalıştırın. Bu, veri setini işleyip grafiği oluşturacak ve bir HTML dosyası olarak kaydedecektir.
    * [cite_start]Oluşan HTML dosyasını herhangi bir web tarayıcısında açarak görselleştirmeye erişebilir ve JavaScript ile hazırlanan butonlar üzerinden analizleri gerçekleştirebilirsiniz[cite: 160, 162].

## ✍️ Yazar Katkıları

| Geliştirici | Katkı Alanı |
| :--- | :--- |
| **Çağatay ALTINTOPAÇ** | [cite_start]Frontend çalışmaları (HTML, CSS) genel itibariyle yürütülmüştür[cite: 304]. |
| **Ali KILINÇ** | [cite_start]Projenin Backend tarafı, gerekli isterlerin yerine getirilmesi ve sonuçların kontrolü görevi üstlenilmiştir[cite: 305]. |
| **Ortak Çalışma** | Veri setinin okunması ve işlenmesi. [cite_start]Projenin çoğu aşamasında ortak çalışmalar yapılmıştır[cite: 304, 306]. |

## 🔗 Kaynakça (Raporun İçinden)

* [cite_start]Hata ayıklama için: `https://chatgpt.com/` [cite: 308]
