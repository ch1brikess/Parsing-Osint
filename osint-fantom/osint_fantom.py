import requests
import json
import time
import sys
from urllib.parse import quote
import os

class OSINTInvestigator:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.results = {}
    
    def check_phone(self, phone):
        """Проверка номера телефона через открытые источники"""
        print(f"[+] Проверяем номер: {phone}")
        
        # Очистка номера от лишних символов
        clean_phone = ''.join(filter(str.isdigit, phone))
        
        try:
            # Проверка через API (примеры сервисов)
            sources = [
                f"https://api.numverify.com/{clean_phone}",
                f"https://htmlweb.ru/geo/api.php?json&telcod={clean_phone}",
            ]
            
            for source in sources:
                try:
                    response = self.session.get(source, timeout=10)
                    if response.status_code == 200:
                        data = response.json()
                        self.results['phone'] = data
                        break
                except:
                    continue
            
            # Поиск в социальных сетях по номеру
            self.search_social_media(clean_phone, 'phone')
            
        except Exception as e:
            print(f"[-] Ошибка при проверке телефона: {e}")
    
    def check_email(self, email):
        """Проверка email через открытые источники"""
        print(f"[+] Проверяем email: {email}")
        
        try:
            # Проверка на утечки (используем публичные API)
            breach_check = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
            response = self.session.get(breach_check, timeout=10)
            
            if response.status_code == 200:
                breaches = response.json()
                self.results['breaches'] = breaches
                print(f"[+] Найдено утечек: {len(breaches)}")
            
            # Поиск по социальным сетям
            self.search_social_media(email, 'email')
            
        except Exception as e:
            print(f"[-] Ошибка при проверке email: {e}")
    
    def search_social_media(self, query, query_type):
        """Поиск в социальных сетях"""
        print(f"[+] Ищем в социальных сетях...")
        
        social_networks = {
            'VK': f"https://vk.com/people/{quote(query)}",
            'Telegram': f"https://t.me/{query}",
            'Instagram': f"https://www.instagram.com/{query}/",
            'Facebook': f"https://www.facebook.com/public/{query}",
        }
        
        found_profiles = {}
        
        for network, url in social_networks.items():
            try:
                response = self.session.get(url, timeout=8, allow_redirects=True)
                
                if response.status_code == 200:
                    # Простая проверка наличия профиля
                    if network == 'VK' and 'id' in response.url:
                        found_profiles[network] = response.url
                    elif network == 'Telegram' and response.url.startswith('https://t.me/'):
                        found_profiles[network] = response.url
                    elif 'instagram.com' in response.url and response.url.count('/') >= 4:
                        found_profiles[network] = response.url
                
                time.sleep(1)  # Задержка между запросами
                
            except Exception as e:
                print(f"[-] Ошибка при проверке {network}: {e}")
        
        self.results['social_media'] = found_profiles
    
    def check_username(self, username):
        """Проверка username across platforms"""
        print(f"[+] Проверяем username: {username}")
        
        platforms = {
            'GitHub': f'https://github.com/{username}',
            'Twitter': f'https://twitter.com/{username}',
            'Reddit': f'https://www.reddit.com/user/{username}',
            'YouTube': f'https://www.youtube.com/@{username}',
            'Twitch': f'https://www.twitch.tv/{username}',
        }
        
        found_accounts = {}
        
        for platform, url in platforms.items():
            try:
                response = self.session.head(url, timeout=5)
                if response.status_code == 200:
                    found_accounts[platform] = url
                    print(f"[+] Найден аккаунт на {platform}")
                
                time.sleep(0.5)
                
            except:
                continue
        
        self.results['username_search'] = found_accounts
    
    def google_search(self, query):
        """Поиск через Google (имитация)"""
        print(f"[+] Ищем в поисковых системах: {query}")
        
        # Используем сервисы для поиска
        search_urls = [
            f"https://www.google.com/search?q={quote(query)}",
            f"https://yandex.ru/search/?text={quote(query)}",
        ]
        
        search_results = []
        
        for url in search_urls:
            try:
                response = self.session.get(url, timeout=10)
                if response.status_code == 200:
                    # Здесь можно добавить парсинг результатов
                    search_results.append(f"Результаты по запросу: {query}")
            except:
                continue
        
        self.results['search_engines'] = search_results
    
    def generate_report(self):
        """Генерация отчета"""
        print("\n" + "="*60)
        print("ОТЧЕТ OSINT-ИССЛЕДОВАНИЯ")
        print("="*60)
        
        for category, data in self.results.items():
            print(f"\n--- {category.upper()} ---")
            if isinstance(data, dict):
                for key, value in data.items():
                    print(f"{key}: {value}")
            elif isinstance(data, list):
                for item in data:
                    print(f"- {item}")
            else:
                print(data)
        
        # Сохранение отчета
        timestamp = int(time.time())
        filename = f"osint_report_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("OSINT Report\n")
            f.write("="*50 + "\n")
            for category, data in self.results.items():
                f.write(f"\n{category}:\n")
                f.write(str(data) + "\n")
        
        print(f"\n[+] Отчет сохранен в файл: {filename}")

def show_banner():
    banner = """
    ██████╗ ███████╗██╗███╗   ██╗████████╗
    ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
    ██║   ██║███████╗██║██╔██╗ ██║   ██║   
    ██║   ██║╚════██║██║██║╚██╗██║   ██║   
    ╚██████╔╝███████║██║██║ ╚████║   ██║   
     ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                                             
    """
    print(banner)

def main():
    show_banner()
    
    investigator = OSINTInvestigator()
    
    while True:
        print("\n" + "="*50)
        print("OSINT INVESTIGATOR v2.0")
        print("="*50)
        print("1. Проверить номер телефона")
        print("2. Проверить email")
        print("3. Проверить username")
        print("4. Полная проверка")
        print("5. Выход")
        print("="*50)
        
        choice = input("Выберите опцию (1-5): ")
        
        if choice == "1":
            phone = input("Введите номер телефона: ")
            investigator.check_phone(phone)
            investigator.generate_report()
            
        elif choice == "2":
            email = input("Введите email: ")
            investigator.check_email(email)
            investigator.generate_report()
            
        elif choice == "3":
            username = input("Введите username: ")
            investigator.check_username(username)
            investigator.google_search(username)
            investigator.generate_report()
            
        elif choice == "4":
            print("\n[+] Запуск полной проверки...")
            phone = input("Телефон (опционально): ")
            email = input("Email (опционально): ")
            username = input("Username (опционально): ")
            
            if phone:
                investigator.check_phone(phone)
            if email:
                investigator.check_email(email)
            if username:
                investigator.check_username(username)
                investigator.google_search(username)
            
            investigator.generate_report()
            
        elif choice == "5":
            print("Выход...")
            break
            
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()