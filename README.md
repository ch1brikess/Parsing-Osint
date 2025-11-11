# -My-Pasing-Osint-Tools

## Languages
1. [EN](#EN)
2. [RU](#RU)
   
## EN
**A powerful collection of OSINT scripts curated and partially modified by ch1brikess.**

This repository serves as a personal toolkit, bundling some of the most effective open-source intelligence tools available, along with custom modifications and additions. It includes both third-party projects I've adapted for my workflow and original scripts developed by myself and collaborators.

## Table of Contents
1. [Introduction](#introduction)
2. [Included Tools](#included-tools)
3. [Installation & Setup](#installation--setup)
4. [Usage](#usage)
5. [Disclaimer](#disclaimer)
6. [Contributing](#contributing)
7. [License](#license)

---

## Introduction

This project is a compilation of essential OSINT utilities designed to streamline digital investigations. It combines powerful existing tools with custom enhancements and original creations, providing a comprehensive suite for gathering information from public sources. The included tools cover user account discovery, email tracing, social media profiling, and system utility functions for Windows environments.

---

## Included Tools

### **DaProfiler (custom edition)**
*Original Project:* https://github.com/daprofiler/DaProfiler  
*Description:* An advanced OSINT tool for tracing digital identities through social networks, public directories, and business listings. This version has been edited for improved usability and integration into this toolkit. It can also perform facial recognition on profile photos and generate potential email addresses based on names.
*Note:* Requires Python 3.8 and Mozilla Firefox.
<img width="865" height="101" alt="image" src="https://github.com/user-attachments/assets/a9cfca02-0eee-47f2-8d25-755e32dd918b" />

### **Blackbird (+2 my methods)**
*Original Project:* https://github.com/p1ngul1n0/blackbird  
*Description:* A robust OSINT tool for rapid searches across 600+ platforms using usernames or emails. My modifications enhance its reporting and integration capabilities. Features AI-powered NER for metadata extraction and export options (PDF, CSV, HTTP).
*Note:* Developed by P1ngul1n0; my edits are for personal use within this collection.
<img width="2048" height="2122" alt="image" src="https://github.com/user-attachments/assets/7eeafaaf-66cd-41a5-b9e0-d101eaa810d2" />


### **Osint-fantom**
*Description:* An original OSINT script written by me and a collaborator. This tool is unique to this repository and focuses on specialized data aggregation techniques not found in other tools. Its development continues here.
*Note:* Created exclusively for this project.

### **Tookie-osint (custom edition)**
*Original Project:* https://github.com/Alfredredbird/tookie-osint  
*Description:* A user-friendly OSINT tool similar to Sherlock, designed to discover user accounts across websites. My edits improve stability and add features like Tor support and detailed reporting. Optimized for Python 3.12.
*Note:* Created by Alfredredbird; my edits are for personal use within this collection.
<img width="952" height="1300" alt="image" src="https://github.com/user-attachments/assets/22b9a0bd-f5cb-4f11-b63a-5a5f5a70615a" />

### **Windows-utils**
*Description:* A collection of Linux-style command-line utilities ported or adapted for Windows environments. Includes tools for file management, text processing, and system monitoring to make Windows feel more like a Unix-based system.
*Note:* Original scripts developed by ch1brikess.

### **Clink**
*Description:* A utility that enhances the visual appearance and functionality of the Windows Command Prompt (cmd.exe), adding features like syntax highlighting, better tab completion, and a more modern look.

---

## Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/ch1brikess/-My-Parsing-Osint-Tools.git
   cd -My-Pasing-Osint-Tools
   ```

2. Install global dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Navigate to each tool's directory and install its specific requirements if needed:
   ```bash
   cd DaProfiler-edited && pip install -r requirements.txt
   cd ../blackbird+me && pip install -r requirements.txt
   cd ../tookie-osint-edited && pip install -r requirements.txt
   ```

4. For DaProfiler, configure LinkedIn credentials in `modules/linkedin_search/`.

5. Ensure you have Python 3.8+ and Firefox installed for DaProfiler.

---

## Usage

Each tool has its own command-line interface. Refer to their respective documentation for detailed usage instructions:

- **DaProfiler-edited**: Run `python da_profiler.py --help`
- **blackbird+me**: Run `python blackbird.py --help`
- **tookie-osint-edited**: Run `python tookie-osint --help`
- **osint-fantom**: Run `python osint_fantom.py --help`
- **windows-utils**: Add the folder to your PATH and use commands like `ls`, `grep`, etc., directly in cmd.

---

## Disclaimer

> **This collection is for educational purposes ONLY. Do not use it without permission.**

The author (ch1brikess) is not liable for any damages caused by direct or indirect use of these tools. All original authors (P1ngul1n0, Alfredredbird, etc.) disclaim responsibility for misuse. By using this toolkit, you accept full responsibility for your actions and any consequences thereof.

---

## Contributing

I welcome contributions! If you'd like to improve any of the tools or add new ones:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to the branch.
5. Open a Pull Request.

Please ensure your code follows the existing style and includes appropriate documentation.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

# -My-Pasing-Osint-Tools
## RU

**Мощнейшая коллекция OSINT скриптов, собранная и частично модифицированная ch1brikess.**

Этот репозиторий представляет собой личный инструментарий, объединяющий самые эффективные открытые инструменты для сбора информации, а также мои собственные модификации и дополнения. Включает как сторонние проекты, адаптированные мной под свой рабочий процесс, так и оригинальные скрипты, разработанные мной и моими коллегами.

## Содержание
1. [Введение](#введение)
2. [Включенные инструменты](#включенные-инструменты)
3. [Установка и настройка](#установка-и-настройка)
4. [Использование](#использование)
5. [Отказ от ответственности](#отказ-от-ответственности)
6. [Участие в разработке](#участие-в-разработке)
7. [Лицензия](#лицензия)

---

## Введение

Этот проект — это компиляция ключевых OSINT утилит, предназначенных для упрощения цифровых расследований. Он объединяет мощные существующие инструменты с кастомными улучшениями и оригинальными созданиями, предоставляя комплексный набор для сбора информации из публичных источников. Включенные инструменты охватывают поиск учетных записей пользователей, трассировку электронной почты, профилирование в социальных сетях и системные утилиты для среды Windows.

---

## Включенные инструменты

### **DaProfiler (Кастомизированная редакция)**
*Оригинальный проект:* https://github.com/daprofiler/DaProfiler  
*Описание:* Расширенный OSINT инструмент для трассировки цифровой идентичности через социальные сети, публичные каталоги и бизнес-листинги. Эта версия была отредактирована для улучшения удобства использования и интеграции в этот набор. Может также выполнять распознавание лиц на профильных фото и генерировать потенциальные адреса электронной почты на основе имен.
*Примечание:* Требует Python 3.8 и Mozilla Firefox.
<img width="865" height="101" alt="image" src="https://github.com/user-attachments/assets/a9cfca02-0eee-47f2-8d25-755e32dd918b" />

### **Blackbird (+2 моих метода)**
*Оригинальный проект:* https://github.com/p1ngul1n0/blackbird  
*Описание:* Мощный OSINT инструмент для быстрого поиска по 600+ платформам с использованием имени пользователя или электронной почты. Мои изменения улучшают его отчетность и возможности интеграции. Включает ИИ-модели для извлечения метаданных и экспорт в форматах PDF, CSV, HTTP.
*Примечание:* Разработан P1ngul1n0; мои правки предназначены для личного использования в этом наборе.
<img width="2048" height="2122" alt="image" src="https://github.com/user-attachments/assets/f274073b-8b18-4c15-ba36-8478a6574eef" />

### **Osint-fantom**
*Описание:* Оригинальный OSINT скрипт, написанный мной и моим соавтором. Этот инструмент уникален для данного репозитория и фокусируется на специализированных методах агрегации данных, не встречающихся в других инструментах. Его разработка продолжается здесь.
*Примечание:* Создан исключительно для этого проекта.

### **Tookie-osint (Кастомизированная редакция)**
*Оригинальный проект:* https://github.com/Alfredredbird/tookie-osint  
*Описание:* Удобный в использовании OSINT инструмент, похожий на Sherlock, предназначенный для поиска учетных записей пользователей на различных сайтах. Мои правки улучшают стабильность и добавляют такие функции, как поддержка Tor и детальные отчеты. Оптимизирован для Python 3.12.
*Примечание:* Создан Alfredredbird; мои правки предназначены для личного использования в этом наборе.
<img width="952" height="1300" alt="image" src="https://github.com/user-attachments/assets/22b9a0bd-f5cb-4f11-b63a-5a5f5a70615a" />

### **Windows-utils**
*Описание:* Набор утилит командной строки в стиле Linux, портированных или адаптированных для среды Windows. Включает инструменты для управления файлами, обработки текста и мониторинга системы, чтобы сделать Windows более похожей на Unix-подобную систему.
*Примечание:* Оригинальные скрипты разработаны ch1brikess.

### **Clink**
*Описание:* Утилита, улучшающая визуальный вид и функциональность командной строки Windows (cmd.exe), добавляя такие функции, как подсветка синтаксиса, улучшенное автодополнение и более современный внешний вид.

---

## Установка и настройка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ch1brikess/-My-Parsing-Osint-Tools.git
   cd -My-Pasing-Osint-Tools
   ```

2. Установите глобальные зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Перейдите в директорию каждого инструмента и установите его специфические зависимости при необходимости:
   ```bash
   cd DaProfiler-edited && pip install -r requirements.txt
   cd ../blackbird+me && pip install -r requirements.txt
   cd ../tookie-osint-edited && pip install -r requirements.txt
   ```

4. Для DaProfiler настройте учетные данные LinkedIn в `modules/linkedin_search/`.

5. Убедитесь, что у вас установлен Python 3.8+ и Firefox для DaProfiler.

---

## Использование

Каждый инструмент имеет свой интерфейс командной строки. Обратитесь к их соответствующей документации для подробных инструкций по использованию:

- **DaProfiler-edited**: Запустите `python da_profiler.py --help`
- **blackbird+me**: Запустите `python blackbird.py --help`
- **tookie-osint-edited**: Запустите `python tookie-osint --help`
- **osint-fantom**: Запустите `python osint_fantom.py --help`
- **windows-utils**: Добавьте папку в переменную окружения PATH и используйте команды, такие как `ls`, `grep` и т.д., непосредственно в cmd.

---

## Отказ от ответственности

> **Этот набор предназначен исключительно для образовательных целей. Не используйте его без разрешения.**

Автор (ch1brikess) не несет ответственности за любые убытки, вызванные прямым или косвенным использованием этих инструментов. Все оригинальные авторы (P1ngul1n0, Alfredredbird и др.) отказываются от ответственности за неправомерное использование. Используя этот набор, вы принимаете полную ответственность за свои действия и любые последствия.

---

## Участие в разработке

Я приветствую вклады! Если вы хотите улучшить любой из инструментов или добавить новые:
1. Форкните репозиторий.
2. Создайте ветку с новой функцией.
3. Зафиксируйте свои изменения.
4. Отправьте изменения в ветку.
5. Откройте Pull Request.

Пожалуйста, убедитесь, что ваш код соответствует существующему стилю и содержит соответствующую документацию.

---

## Лицензия

Этот проект лицензирован под MIT License. Подробнее см. в файле `LICENSE`.

---
