import pytest
import os
from datetime import datetime
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from conftest import abort_test

class TestRegisterAndLogin:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.register_page = RegisterPage(driver)
        self.login_page = LoginPage(driver)
        # Criar diretório para screenshots se não existir
        self.screenshot_dir = "screenshots"
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def take_screenshot(self, name):
        """Tira screenshot com timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.screenshot_dir}/{name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        return filename

    def test_register_and_login_flow(self):
        """Teste que combina o fluxo de registro e login"""
        try:
            # Dados de teste
            test_name = "Teste Automatizado"
            test_email = f"teste_{datetime.now().strftime('%Y%m%d%H%M%S')}@exemplo.com"
            test_password = "Senha@123"

            # 1. Navegar para a página de registro
            self.register_page.navigate()
            self.take_screenshot("pagina_registro_inicial")

            # 2. Preencher formulário de registro
            self.register_page.register(test_name, test_email, test_password, test_password)
            self.take_screenshot("formulario_registro_preenchido")

            # 3. Verificar se o registro foi bem sucedido
            # Aqui você pode adicionar uma verificação específica baseada no comportamento da sua aplicação
            # Por exemplo, verificar se foi redirecionado para a página de login

            # 4. Navegar para a página de login
            self.login_page.navigate()
            self.take_screenshot("pagina_login")

            # 5. Realizar login com as credenciais recém-cadastradas
            self.login_page.login(test_email, test_password)
            self.take_screenshot("login_realizado")

            # 6. Verificar se o login foi bem sucedido
            # Aqui você pode adicionar uma verificação específica baseada no comportamento da sua aplicação
            # Por exemplo, verificar se foi redirecionado para a página principal

            # 7. Capturar screenshot final
            self.take_screenshot("fluxo_completo_finalizado")

        except Exception as e:
            # Em caso de erro, aborta o teste de forma limpa
            abort_test(self.driver, f"Erro durante o teste: {str(e)}")
