import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
import os
import shutil
from datetime import datetime

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Executar os testes em modo headless"
    )

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Configuração do pytest para gerar relatório HTML"""
    # Criar diretório para relatórios se não existir
    report_dir = "reports"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Configurar o relatório HTML
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(report_dir, f"report_{timestamp}.html")

    # Adicionar a opção de relatório HTML
    config.option.htmlpath = report_path
    config.option.self_contained_html = True

def abort_test(driver=None, message="Teste abortado"):
    """Função para abortar a execução do teste de forma limpa"""
    logger.error(message)
    if driver:
        try:
            driver.quit()
        except:
            pass
    pytest.exit(message)

@pytest.fixture(scope="function")
def driver(request):
    logger.info("Iniciando configuração do ChromeDriver...")

    # Configuração das opções do Chrome
    chrome_options = webdriver.ChromeOptions()

    # Verifica se deve rodar em modo headless
    if request.config.getoption("--headless"):
        logger.info("Executando em modo headless...")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
    else:
        logger.info("Executando em modo normal (com interface gráfica)...")
        chrome_options.add_argument("--start-maximized")

    try:
        # Limpar cache do webdriver-manager
        cache_dir = os.path.join(os.path.expanduser("~"), ".wdm")
        if os.path.exists(cache_dir):
            logger.info("Limpando cache do webdriver-manager...")
            shutil.rmtree(cache_dir)

        logger.info("Instalando ChromeDriver...")
        # Instalar e configurar o ChromeDriver
        service = Service(ChromeDriverManager().install())

        # Inicializar o driver com as opções configuradas
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(10)

        yield driver

    except Exception as e:
        logger.error(f"Erro durante a execução: {str(e)}")
        raise
    finally:
        if 'driver' in locals():
            logger.info("Fechando o navegador...")
            driver.quit()
