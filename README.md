<div align="center">

# 🌤️ Hava Durumu CLI

**Terminalden çıkmadan istediğin şehrin hava durumunu renkli bir tabloda gösteren Python aracı.**
Şehir adını yaz, Enter'a bas; sıcaklık, hissedilen, nem ve rüzgar anında ekranda.

![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![OpenWeatherMap](https://img.shields.io/badge/veri-OpenWeatherMap-EB6E4B)
[![Lisans: MIT](https://img.shields.io/badge/lisans-MIT-blue)](LICENSE)

</div>

```
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
```

## Neler yapabilir?

| | |
| --- | --- |
| **Sınırsız sorgu** | Uygulama açık kalır; istediğin kadar şehri art arda sorgula. |
| **Ayrıntılı bilgi** | Hava durumu, sıcaklık, hissedilen sıcaklık, nem, rüzgar hızı ve ölçüm zamanı. |
| **Türkçe** | Hava durumu açıklamaları Türkçe gelir ("Parçalı bulutlu", "Hafif yağmur"...). |
| **Renkli tablo** | [Rich](https://github.com/Textualize/rich) ile okunaklı, renkli terminal çıktısı. |
| **Hataya dayanıklı** | Yanlış yazılan şehir ya da kopan bağlantı uygulamayı kapatmaz; yeni şehir sormaya devam eder. |

## Hızlı başlangıç

1. Projeyi indir ve gerekli paketleri kur:

   ```bash
   git clone https://github.com/EfeKesgin/hava-durumu-cli-araci.git
   cd hava-durumu-cli-araci
   pip install -r requirements.txt
   ```

2. [OpenWeatherMap](https://openweathermap.org/api)'ten ücretsiz bir hesap açıp API anahtarını kopyala.
   *(Yeni anahtarların etkinleşmesi birkaç saat sürebilir.)*

3. `.env.example` dosyasını `.env` adıyla kopyala ve anahtarını içine yaz:

   ```bash
   cp .env.example .env
   ```

   ```
   OPENWEATHER_API_KEY=buraya_api_anahtarini_yapistir
   ```

4. Çalıştır:

   ```bash
   python main.py
   ```

Şehir adını yazıp Enter'a bas. Çıkmak için **Ctrl+C**.

## API anahtarın güvende mi?

Evet. `.env` dosyası `.gitignore` içinde olduğu için yanlışlıkla GitHub'a yüklenmez. Anahtar
yalnızca senin bilgisayarından OpenWeatherMap'e yapılan isteklerde (HTTPS) kullanılır. Projeyi
başkası kullanacaksa kendi `.env` dosyasını oluşturup kendi anahtarını eklemelidir.

## English

**Hava Durumu CLI** is a small Python command-line tool that shows the current weather for any
city in a colorful table (condition, temperature, feels-like, humidity, wind speed), using the
OpenWeatherMap API. It keeps running so you can query as many cities as you like; a misspelled
city or network error does not close it. Put your API key in a `.env` file (see `.env.example`).
The output is in Turkish.

---

## Geliştiriciler için

### Gereksinimler

- Python 3.8 veya üzeri
- [requests](https://requests.readthedocs.io/): API istekleri
- [python-dotenv](https://github.com/theskumar/python-dotenv): `.env` dosyasını okuma
- [rich](https://github.com/Textualize/rich): renkli tablo çıktısı

### Nasıl çalışır?

`main.py` açılışta API anahtarını `.env` dosyasından (ya da `OPENWEATHER_API_KEY` ortam
değişkeninden) bir kez okur. Her sorgu, OpenWeatherMap'in
[Current Weather](https://openweathermap.org/current) uç noktasına `units=metric` ve `lang=tr`
parametreleriyle, 10 saniyelik zaman aşımıyla gönderilir. Geçersiz anahtar (401) uygulamayı
kapatır; bulunamayan şehir (404) ve ağ hataları yalnızca uyarı gösterir.

## Lisans

Hava Durumu CLI [MIT Lisansı](LICENSE) ile dağıtılır.
