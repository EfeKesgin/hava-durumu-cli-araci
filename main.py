#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Hava Durumu CLI Aracı
---------------------
Bu program, komut satırından hava durumu bilgilerini sorgulamanızı sağlar.
OpenWeatherMap API kullanarak güncel hava durumu verilerini çeker ve
güzel bir tablo formatında gösterir.
"""

import os
import sys
import requests
from datetime import datetime
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

# Rich konsol nesnesi
console = Console()

API_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_api_key():
    """
    API anahtarını .env dosyasından (veya ortam değişkeninden) okur.

    Returns:
        str: OpenWeatherMap API anahtarı

    Raises:
        SystemExit: API anahtarı bulunamazsa
    """
    # .env dosyasını betiğin bulunduğu klasörden yükle
    load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))
    api_key = os.getenv('OPENWEATHER_API_KEY', '').strip()
    if not api_key:
        console.print("[red]Hata: OPENWEATHER_API_KEY bulunamadı![/red]")
        console.print("Lütfen .env.example dosyasını .env olarak kopyalayıp API anahtarınızı yazın.")
        sys.exit(1)
    return api_key

def get_weather(city, api_key):
    """
    OpenWeatherMap API'den hava durumu bilgilerini alır.

    Args:
        city (str): Hava durumu bilgisi alınacak şehir adı
        api_key (str): OpenWeatherMap API anahtarı

    Returns:
        dict | None: API'den gelen hava durumu verileri, hata olursa None

    Raises:
        SystemExit: API anahtarı geçersizse
    """
    # API isteği için parametreleri hazırla
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Sıcaklık birimi: Celsius
        'lang': 'tr'        # Dil: Türkçe
    }

    try:
        # API'ye istek gönder
        response = requests.get(API_URL, params=params, timeout=10)
    except requests.exceptions.RequestException as e:
        console.print("[red]Hata: API isteği başarısız oldu![/red]")
        console.print(f"[red]Detay: {str(e)}[/red]")
        return None

    if response.status_code == 401:
        console.print("[red]Hata: API anahtarı geçersiz![/red]")
        sys.exit(1)
    if response.status_code == 404:
        console.print(f"[yellow]'{city}' adında bir şehir bulunamadı.[/yellow]")
        return None
    if not response.ok:
        console.print(f"[red]Hata: API {response.status_code} döndürdü.[/red]")
        return None
    return response.json()

def display_weather(data):
    """
    Hava durumu verilerini güzel bir tablo formatında gösterir.
    
    Args:
        data (dict): API'den gelen hava durumu verileri
    """
    # Tablo başlığını oluştur
    table = Table(title=f"\n{data['name']} için Hava Durumu")
    
    # Tablo sütunlarını ekle
    table.add_column("Özellik", style="cyan")
    table.add_column("Değer", style="green")

    # Ana hava durumu bilgilerini al
    weather_desc = data['weather'][0]['description'].capitalize()
    temp = f"{data['main']['temp']}°C"
    feels_like = f"{data['main']['feels_like']}°C"
    humidity = f"%{data['main']['humidity']}"
    wind_speed = f"{data['wind']['speed']} m/s"
    
    # Zaman bilgisini formatla
    timestamp = datetime.fromtimestamp(data['dt'])
    time_str = timestamp.strftime("%d/%m/%Y %H:%M")

    # Tabloya verileri ekle
    table.add_row("Durum", weather_desc)
    table.add_row("Sıcaklık", temp)
    table.add_row("Hissedilen", feels_like)
    table.add_row("Nem", humidity)
    table.add_row("Rüzgar Hızı", wind_speed)
    table.add_row("Son Güncelleme", time_str)

    # Tabloyu ekrana yazdır
    console.print(table)

def main():
    """
    Ana program fonksiyonu.
    Kullanıcıdan şehir adı alır, hava durumu bilgisini gösterir ve sürekli çalışır.
    Çıkmak için pencereyi kapatmak yeterlidir.
    """
    console.print("[bold cyan]\nHava Durumu Sorgulama Uygulamasına Hoş Geldin![/bold cyan]")
    console.print("[green]Şehir adını yaz ve Enter'a bas. (Çıkmak için Ctrl+C)[/green]\n")
    api_key = get_api_key()
    while True:
        try:
            city = input("Şehir adı: ").strip()
            if not city:
                console.print("[yellow]Lütfen bir şehir adı gir.[/yellow]")
                continue
            weather_data = get_weather(city, api_key)
            if weather_data:
                display_weather(weather_data)
            print()  # Boş satır
        except (KeyboardInterrupt, EOFError):
            console.print("\n[red]Uygulama kapatılıyor...[/red]")
            break

if __name__ == "__main__":
    main() 