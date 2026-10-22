# 🌤️ Hava Durumu CLI Aracı

![Python](https://img.shields.io/badge/python-3.8%2B-3776AB?logo=python&logoColor=white)
[![Lisans: MIT](https://img.shields.io/badge/lisans-MIT-blue.svg)](LICENSE)

Komut satırından istediğin kadar şehir adı girerek güncel hava durumunu renkli bir tabloda görmeni sağlayan, sürekli açık kalan bir Python uygulaması. Veriler [OpenWeatherMap](https://openweathermap.org/) API’sinden gelir.

## 👨‍💻 Geliştirici
[Efe Kesgin](https://github.com/EfeKesgin)

## 📸 Ekran Görüntüsü
```
Hava Durumu Sorgulama Uygulamasına Hoş Geldin!
Şehir adını yaz ve Enter'a bas. (Çıkmak için pencereyi kapatabilirsin)

Şehir adı: İstanbul

      İstanbul için Hava Durumu      
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Özellik        ┃ Değer            ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ Durum          │ Açık             │
│ Sıcaklık       │ 18.42°C          │
│ Hissedilen     │ 18.46°C          │
│ Nem            │ %82              │
│ Rüzgar Hızı    │ 4.12 m/s         │
│ Son Güncelleme │ 14/06/2025 05:28 │
└────────────────┴──────────────────┘

Şehir adı: Frankfurt

     Frankfurt için Hava Durumu      
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Özellik        ┃ Değer            ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ Durum          │ Parçalı bulutlu  │
│ Sıcaklık       │ 15.12°C          │
│ Hissedilen     │ 14.80°C          │
│ Nem            │ %70              │
│ Rüzgar Hızı    │ 3.50 m/s         │
│ Son Güncelleme │ 14/06/2025 05:28 │
└────────────────┴──────────────────┘
```

## ✨ Özellikler
- İstediğin kadar şehir ismi girerek hava durumu sorgulama
- Sıcaklık, nem, rüzgar hızı gibi detaylı bilgiler
- Renkli ve kullanıcı dostu arayüz
- Türkçe hava durumu açıklamaları
- Yanlış yazılan şehirde uygulama kapanmaz, yeni şehir sormaya devam eder
- Uygulama sürekli açık kalır, çıkmak için `Ctrl+C` yeterli

## 🚀 Kurulum
1. Projeyi bilgisayarına indir:
```bash
git clone https://github.com/EfeKesgin/hava-durumu-cli-araci.git
cd hava-durumu-cli-araci
```
2. Gerekli paketleri yükle:
```bash
pip install -r requirements.txt
```
3. OpenWeatherMap'ten ücretsiz bir API anahtarı al:
   - https://openweathermap.org/api adresine git
   - Ücretsiz hesap oluştur
   - API anahtarını kopyala
4. `.env.example` dosyasını `.env` olarak kopyala ve API anahtarını yaz:
```bash
cp .env.example .env
```
```
OPENWEATHER_API_KEY=buraya_api_anahtarini_yapistir
```
> `.env` dosyası `.gitignore` içindedir; API anahtarın yanlışlıkla GitHub’a gitmez.
> Yeni oluşturulan anahtarların etkinleşmesi birkaç saat sürebilir.

## 💻 Kullanım
```bash
python main.py
```
- Şehir adını yazıp Enter'a bas.
- Sonuç ekrana gelir, yeni şehir ismi girebilirsin.
- Çıkmak için `Ctrl+C` tuşlarına bas.

## 🛠️ Gereksinimler
- Python 3.8 veya üstü
- requests (API istekleri için)
- python-dotenv (Çevre değişkenleri için)
- rich (Güzel görünümlü çıktılar için)

## 🤝 Katkıda Bulunma
Eğer projeye katkıda bulunmak istersen:
1. Bu projeyi fork et
2. Yeni bir branch oluştur (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerini commit et (`git commit -am 'Yeni özellik: X'`)
4. Branch'ini push et (`git push origin feature/yeniOzellik`)
5. Pull Request oluştur

## 📝 Lisans
MIT Lisansı altında dağıtılmaktadır. Detaylar için `LICENSE` dosyasına bakabilirsin.

## ⚠️ Dikkat: .env Dosyası Gizli Olmalıdır
- `.env` dosyası API anahtarını içerdiği için gizli tutulmalıdır.
- Bu dosya `.gitignore` sayesinde GitHub'a yüklenmez.
- Projeyi başkası kullanacaksa, kendi `.env` dosyasını oluşturmalı ve kendi API anahtarını eklemelidir.
