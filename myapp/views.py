from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Это главная страница моего сайта.</p>
    """
    return HttpResponse(html)

def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Я - разработчик веб-приложений, использующий Django.</p>
    """
    return HttpResponse(html)


import logging

# Создайте объект логгера
logger = logging.getLogger(__name__)

def home(request):
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Это главная страница моего сайта.</p>
    """
    # Запишите данные о посещении страницы в лог-файл
    logger.info('Посещение главной страницы')
    return HttpResponse(html)

def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Я - разработчик веб-приложений, использующий Django.</p>
    """
    # Запишите данные о посещении страницы в лог-файл
    logger.info('Посещение страницы "О себе"')
    return HttpResponse(html)