# 🎓 Akademik İş Birliği Grafiği ve Algoritmalar (Veri Yapıları Projesi)

Bu proje, akademik bir veri seti kullanılarak yazarlar arasındaki iş birliği ilişkilerini modelleyen bir **graf yapısı** oluşturmayı ve bu graf üzerinde çeşitli veri yapısı ile algoritma konseptlerini uygulamayı amaçlamaktadır. Yazarların düğümleri temsil ettiği ve iş birliğinin kenarlarla gösterildiği bir graf yapısı oluşturulmuştur.

Proje, akademik iş birliği gibi somut bir senaryo üzerinden veri yapılarını uygulamalı bir şekilde öğrenme fırsatı sunmuştur.

## ✨ Temel Özellikler ve Uygulanan İşlevler

Projenin ana veri yapısı graf olup, bu yapı üzerinde Nesneye Yönelik Programlama (OOP) mantığı kullanılarak gerekli algoritmalar geliştirilmiştir.

### 📊 Graf Yapısı ve Veri İşleme

* **Düğümler (Node):** Yazarları temsil eder. Ana yazar düğümleri mavi ile gösterilmiş olup, kendisine yardımcı yazar düğümleri bağlıdır.
* **Kenarlar (Edge):** Yazarlar arasındaki iş birliğini gösterir.
* **Ağırlık (Weight):** Kenar ağırlığı, Ana yazar ve yardımcı yazar arasında kaç adet ortak makale yazıldığı analiz edilerek belirlenmiştir.
* **Kullanılan Sınıflar:** Projede 'Node', 'Edge', 'Graph' sınıfları ve veri setindeki bilgileri tutan 'Yazarlar' sınıfı tanımlanmıştır.

### ⚙️ Uygulanan Analiz ve Algoritmalar

Proje kapsamında graf üzerinde aşağıdaki temel analiz ve algoritmalar uygulanmıştır:

* **En Kısa Yol Bulma:** İki yazar arasındaki en kısa yol, ağırlıklara bakılarak **Dijkstra Algoritması** yardımıyla bulunur. Algoritma hazır kütüphane yardımıyla tasarlanmamıştır.
* **Yazar İş Birlikleri:** Verilen ID'ye ait yazarın tüm yardımcı yazarları listelenir. Ayrıca bir yazarın sahip olduğu kenar (iş birliği) sayısı hesaplanır.
* **En Çok İş Birliği:** Tüm yazarlar arasında dolaşılarak en çok yardımcı yazara sahip olan yazar bulunur.
* **En Uzun Yol Bulma:** Belirlenen başlangıç noktasından (yazar ID) gidilebilecek en uzun yol sürekli tutulur ve bulunur. En uzun yol webde kırmızı ile boyanır.

## 💻 Kullanılan Teknolojiler

Proje, temel programlama dilleri olarak Python ve JavaScript tercih edilerek : 151], web tabanlı görselleştirme için HTML ve CSS kullanılmıştır: 151, 153].

| Kategori | Teknoloji | Açıklama |
| :--- | :--- | :--- |
| **Backend / Veri İşleme** | **Python** | Graf yapısının oluşturulması, verinin işlenmesi ve algoritma mantığı. |
| **Veri Aktarımı** | **Pandas** Kütüphanesi | Excel dosyasındaki verilerin (ID, yazar adı, makaleler) okunması ve sınıflara aktarılması. |
| **Grafiksel Görselleştirme** | **Pyvis** Kütüphanesi | Web tabanlı grafiğin oluşturulması ve çıktının HTML dosyası olarak kaydedilmesi. |
| **Frontend / Arayüz** | **HTML** ve **CSS** | Butonlar, çıktı ekranı, textboxlar kodlandı; sade ve estetik bir tasarım elde edildi. |
| **Etkileşim / Hareket** | **JavaScript** | Görselleştirmelerin mantıksal bağlantısı ve animasyonların gerçekleştirilmesi. |

## ⚙️ Kurulum ve Çalıştırma

Bu projenin genel çalışma mantığı: Python kısmından gerekli bilgileri alır, HTML/CSS kısmında kullanıcıya gösterir ve Javascript kısmında ise hareketlendirir.

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
    * Oluşan HTML dosyasını herhangi bir web tarayıcısında açarak görselleştirmeye erişebilir ve JavaScript ile hazırlanan butonlar üzerinden analizleri gerçekleştirebilirsiniz.

## ✍️ Yazar Katkıları

| Geliştirici | Katkı Alanı |
| :--- | :--- |
| **Çağatay ALTINTOPAÇ** | Frontend çalışmaları (HTML, CSS) genel itibariyle yürütülmüştür. |
| **Ali KILINÇ** | Projenin Backend tarafı, gerekli isterlerin yerine getirilmesi ve sonuçların kontrolü görevi üstlenilmiştir. |
| **Ortak Çalışma** | Veri setinin okunması ve işlenmesi. Projenin çoğu aşamasında ortak çalışmalar yapılmıştır. |

