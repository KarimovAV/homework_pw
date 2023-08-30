import requests
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
from base.url import URL
from base.values import Values


def test_open_page_gateway(page):
    # Открываем cloud.ru -> Сервисы -> Инфраструктура -> API Gateway
    page.goto(URL.base_url)
    page.get_by_role("navigation").get_by_text("Сервисы").click()
    page.get_by_text("Инфраструктура").nth(2).click()
    page.get_by_role("link", name="Product Icon API Gateway Высокопроизводительный, полностью управляемый хостинг API"). \
        first.click()

    # Берем значения для сравнения (url Gateway / заголовок страницы)
    element = page.locator('//h1[@class="Hero_title__0eNxo"]')
    element_value = element.inner_text()
    current_url = page.url

    # Проверяем, что URL страницы верный
    assert current_url == URL.page_api_gateway, f'URL {current_url} страницы API Gateway некорректен'

    # Проверяем по значению заголовка, что  страница загрузилась
    assert element_value == Values.HEADERS_API_GATEWAY.value, f'Заголовок {Values.HEADERS_API_GATEWAY.value} ' \
                                                              f'не обнаружен'

