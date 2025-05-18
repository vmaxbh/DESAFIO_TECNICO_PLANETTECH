# Projeto de Automação de Testes - PlanetTech

## 📋 Descrição
Projeto de automação de testes para o sistema PlanetTech, utilizando Selenium WebDriver com Python e Pytest. O projeto implementa testes automatizados para os fluxos de registro e login do sistema.

## 🏗️ Arquitetura do Projeto

```
dt_planettech/
│
├── tests/                      # Diretório de testes
│   ├── test_register_and_login.py  # Teste combinado de registro e login
│   └── conftest.py            # Configurações do Pytest
│
├── pages/                      # Page Objects
│   ├── base_page.py           # Classe base com métodos comuns
│   ├── register_page.py       # Page Object para registro
│   └── login_page.py          # Page Object para login
│
├── screenshots/               # Diretório para capturas de tela
│   └── [arquivos de screenshot]  # Screenshots com timestamp
│
├── reports/                   # Diretório para relatórios HTML
│   └── report.html           # Relatório de execução dos testes
│
├── requirements.txt           # Dependências do projeto
└── README.md                 # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Selenium WebDriver
- Pytest
- ChromeDriver (gerenciado automaticamente)
- Pytest-HTML (para relatórios)

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/vmaxbh/DESAFIO_TECNICO_PLANETTECH.git
cd dt_planettech
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Instale o pytest-html:
```bash
pip install pytest-html
```

## 🚀 Executando os Testes

### Modo Normal (com interface gráfica)
```bash
pytest tests/test_register_and_login.py -v --html=reports/report.html
```

### Modo Headless (sem interface gráfica)
```bash
pytest tests/test_register_and_login.py -v --headless --html=reports/report.html
```

## 📊 Relatórios HTML

O projeto utiliza o pytest-html para gerar relatórios detalhados da execução dos testes. Os relatórios incluem:

- Resumo da execução
- Detalhes dos testes executados
- Status de cada teste (passou/falhou)
- Tempo de execução
- Capturas de tela (quando disponíveis)
- Stack trace de erros (quando ocorrem)

Os relatórios são gerados no diretório `reports/` com o nome `report.html`. Para visualizar o relatório, basta abrir o arquivo HTML em qualquer navegador web.

## 📸 Capturas de Tela

O projeto captura automaticamente screenshots em momentos-chave do teste:
- Página inicial de registro
- Formulário de registro preenchido
- Página de login
- Após realizar o login
- Final do fluxo

Os screenshots são salvos no diretório `screenshots/` com timestamp no nome do arquivo.

## 🏗️ Estrutura do Código

### Page Objects
- **BasePage**: Classe base com métodos comuns para interação com elementos
- **RegisterPage**: Implementa ações específicas da página de registro
- **LoginPage**: Implementa ações específicas da página de login

### Configurações (conftest.py)
- Gerenciamento do WebDriver
- Configurações do Chrome (headless/normal)
- Fixtures do Pytest
- Logging

### Testes
- Teste combinado de registro e login
- Geração de dados de teste dinâmicos
- Captura de screenshots
- Tratamento de erros

## 🔧 Configurações do Chrome

### Modo Normal
- Interface gráfica visível
- Janela maximizada
- Ideal para debug e desenvolvimento

### Modo Headless
- Sem interface gráfica
- Configurações otimizadas:
  - `--no-sandbox`
  - `--disable-dev-shm-usage`
  - `--disable-gpu`
  - Resolução: 1920x1080
- Ideal para CI/CD e execução rápida

## 📝 Logging

O projeto utiliza logging para:
- Rastrear a execução dos testes
- Registrar erros e exceções
- Monitorar a configuração do WebDriver
- Acompanhar a limpeza do cache

## 🔄 Fluxo de Teste

1. Configuração do ambiente
2. Navegação para página de registro
3. Preenchimento do formulário de registro
4. Verificação do registro
5. Navegação para página de login
6. Realização do login
7. Verificação do login
8. Captura de screenshots em cada etapa
9. Limpeza e finalização
10. Geração do relatório HTML

## 🤝 Contribuição

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).

## 👨‍💻 Autor

**Maxwell Viana** - [GitHub](https://github.com/vmaxbh?tab=repositories)

Desenvolvedor de Automação de Testes | QA Engineer
