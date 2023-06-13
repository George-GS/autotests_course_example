"""
Тест со звездочкой
1 Перейти на  https://sbis.ru/
2 В Footer'e найти "Скачать СБИС"
3 Перейти по ней
4 Скачать СБИС Плагин для вашей ОС в папку с данным тестом
5 Убедиться, что плагин скачался
6 Вывести на печать размер скачанного файла в мегабайтах
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path

opt = webdriver.ChromeOptions()
opt.add_experimental_option("prefs", {"download.default_directory": r"D:\PyCharm\PycharmProjects\Homework\Вебинар11",
                                      "safebrowsing.enabled": True})
driver = webdriver.Chrome(options=opt)
driver.maximize_window()

try:
    driver.get('https://sbis.ru/')
    download = driver.find_element(By.CSS_SELECTOR, '[href="/download?tab=ereport&innerTab=ereport25"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", download)
    download.click()
    sleep(2)
    plugin = driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"]')
    plugin.click()
    set_plugin = driver.find_element(By.CSS_SELECTOR, '[href="/help/plugin/sbis3plugin/install"]')
    set_plugin.click()
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    plugin_loc = '[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]'
    download_plugin = driver.find_element(By.CSS_SELECTOR, plugin_loc)
    download_plugin.click()
    sleep(6)
    file = 'sbisplugin-setup-web.exe'
    assert Path(file).exists(), 'Плагин не скачался!'
    print(f'Размер скачанного файла в Мб: {round(Path(file).stat().st_size / 1048576, 2)}')
    print('Тест пройден!')
finally:
    driver.quit()
