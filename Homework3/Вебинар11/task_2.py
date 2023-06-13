# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
sleep(1)
browser.maximize_window()

site1 = 'https://fix-online.sbis.ru/'

try:
    browser.get('https://fix-online.sbis.ru/')
    sleep(3)

    login = browser.find_element(By.CSS_SELECTOR, '[name="Login"]')
    # login.clear()
    login.send_keys('Карета', Keys.ENTER)
    assert login.get_attribute('value') == 'Карета'
    sleep(3)

    password = browser.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys('Карета123', Keys.ENTER)
    assert password.get_attribute('value') == 'Карета123'
    sleep(5)

    btn_cont1 = browser.find_element(By.CSS_SELECTOR, '[name="item-contacts"]')
    btn_cont1.click()
    sleep(3)

    btn_cont2 = browser.find_element(By.CSS_SELECTOR,
                                     '[class="NavigationPanels-SubMenu__head  NavigationPanels-SubMenu__head_default ws-flex-shrink-0"]')
    btn_cont2.click()
    sleep(1)

    plus = browser.find_element(By.CSS_SELECTOR,
                                '[class="controls-Button__icon controls-BaseButton__icon controls-icon_size-m controls-icon_style-default controls-icon icon-RoundPlus"]')
    plus.click()
    sleep(5)

    search = browser.find_element(By.CSS_SELECTOR,
                                  '.controls-StackTemplate__top-area-content .controls-Search__nativeField_caretEmpty')
    search.send_keys('Никитин Михаил')
    sleep(3)

    btn3 = browser.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"][title="Никитин Михаил"]')
    btn3.click()
    sleep(3)

    mess1 = browser.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    mess1.send_keys('Привет 13.06')
    sleep(3)

    send = browser.find_element(By.CSS_SELECTOR, '.controls-BaseButton__wrapper .icon-BtArrow')
    send.click()
    sleep(3)

    mess2 = browser.find_element(By.CSS_SELECTOR, '.msg-entity-text')
    assert mess2.text == 'Привет 13.06'

    action_chains = ActionChains(browser)
    action_chains.move_to_element(mess2)
    action_chains.perform()
    btn4 = browser.find_element(By.CSS_SELECTOR, '.controls-Button__icon.icon-Erase')
    btn4.click()
    sleep(3)

    mess3 = browser.find_element(By.CSS_SELECTOR, '.msg-entity-text')
    assert mess3 != 'Привет 13.06'

    print('Все ок')

finally:
    browser.quit()
