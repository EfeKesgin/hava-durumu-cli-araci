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
from rich.console import Console
from rich.table import Table

# Rich konsol nesnesi
console = Console()

def get_weather(city):
    """
    OpenWeatherMap API'den hava durumu bilgilerini alır.
    
    Args:
        city (str): Hava durumu bilgisi alınacak şehir adı
    
    Returns:
        dict: API'den gelen hava durumu verileri
    
    Raises:
        SystemExit: API anahtarı bulunamazsa veya API isteği başarısız olursa
    """
    # .env dosyasını doğrudan oku
    try:
        with open('.env', 'r') as f:
            api_key = f.read().strip().split('=')[1]
    except (FileNotFoundError, IndexError):
        console.print("[red]Hata: .env dosyası bulunamadı veya API anahtarı eksik![/red]")
        console.print("Lütfen .env dosyasında API anahtarınızı tanımlayın.")
        sys.exit(1)
    
    if not api_key:
        console.print("[red]Hata: API anahtarı boş![/red]")
        console.print("Lütfen .env dosyasında geçerli bir API anahtarı tanımlayın.")
        sys.exit(1)

    # API isteği için parametreleri hazırla
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Sıcaklık birimi: Celsius
        'lang': 'tr'        # Dil: Türkçe
    }

    try:
        # API'ye istek gönder
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # HTTP hatalarını kontrol et
        return response.json()
    except requests.exceptions.RequestException as e:
        console.print(f"[red]Hata: API isteği başarısız oldu![/red]")
        console.print(f"[red]Detay: {str(e)}[/red]")
        sys.exit(1)

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
    console.print("[green]Şehir adını yaz ve Enter'a bas. (Çıkmak için pencereyi kapatabilirsin)[/green]\n")
    while True:
        try:
            city = input("Şehir adı: ").strip()
            if not city:
                console.print("[yellow]Lütfen bir şehir adı gir.[/yellow]")
                continue
            weather_data = get_weather(city)
            display_weather(weather_data)
            print()  # Boş satır
        except KeyboardInterrupt:
            console.print("\n[red]Uygulama kapatılıyor...[/red]")
            break

if __name__ == "__main__":
    main() 