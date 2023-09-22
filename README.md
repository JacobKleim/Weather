# Weather forecast

## Project Description
 - This program allows you to get a weather forecast.

## Technologies and tools
 - Python

## How to use
 
1. Clone this repository and go to the project folder:
   ```bash
   cd /c/project_folder # for example

   git clone git@github.com:JacobKleim/Weather.git
   
   cd /c/project_folder/Weather
   ```
2. Сreate and activate a virtual environment:
   ```bash
   python -m venv venv 
   
   source venv/Scripts/activate
   ```

3. Install dependencies:
   ```bash
   python -m pip install --upgrade pip

   pip install -r requirements.txt
   ```

4. Start the project:
   ```bash
   python weather.py
   ```

## Example of work
    
    $ python weather.py

      \   /     Солнечно
       .-.      +22(24) °C
    ― (   ) ―   ↑ 6 м/c
       `-’      10 км
      /   \     0.0 мм
                        ┌─────────────┐
┌───────────────────────┤ Пт. 22 сент.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │     \   /     Ясно           │
│      .-.      +22(24) °C     │      .-.      18 °C          │
│   ― (   ) ―   ↑ 6 м/c        │   ― (   ) ―   ↑ 5-9 м/c      │
│      `-’      10 км          │      `-’      10 км          │
│     /   \     0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Сб. 23 сент.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │      .-.      Небольшой дожд…│
│      .-.      +24(25) °C     │     (   ).    19 °C          │
│   ― (   ) ―   ↑ 6-8 м/c      │    (___(__)   ↑ 6-10 м/c     │
│      `-’      10 км          │     ‘ ‘ ‘ ‘   9 км           │
│     /   \     0.0 мм | 0%    │    ‘ ‘ ‘ ‘    1.5 мм | 83%   │
└──────────────────────────────┴──────────────────────────────┘
Местоположение: Санкт-Петербург, Центральный район, Санкт-Петербург, Северо-Западный федеральный округ, 190000, РФ [59.9387318,30.3162286]

