# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

site1 = 'https://sbis.ru/'
site2 = 'https://tensor.ru/'
site3 = 'https://tensor.ru/about'

browser = webdriver.Chrome()
sleep(2)
try:
    browser.get(site1)
    sleep(2)

    tabs_contacts = browser.find_element(By.CSS_SELECTOR, '[href="/contacts"].sbisru-Header__menu-link')
    tabs_contacts.click()
    sleep(2)

    ban_tens = browser.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor.mb-8:not(.sbisru-link) [alt="Разработчик системы СБИС — компания «Тензор»"]')
    ban_tens.click()
    sleep(2)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    sleep(2)
    assert browser.current_url == site2, 'Неверный адрес сайта'
    blok1 = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
    assert blok1.is_displayed(), 'Блок "Сила в людях" не отображается'
    assert blok1.text == 'Сила в людях', 'Не тот текст в блоке'
    blok1.location_once_scrolled_into_view
    sleep(5)

    tabs_podrobnee = browser.find_element(By.CSS_SELECTOR, '[href="/about"].tensor_ru-link.tensor_ru-Index__link')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", tabs_podrobnee)
    # sleep(5)
    tabs_podrobnee.location_once_scrolled_into_view
    tabs_podrobnee.click()
    sleep(5)
    assert browser.current_url == site3, 'Неверный адрес сайта'
    print('Все ок, АТ прошел')

finally:
    browser.quit()
