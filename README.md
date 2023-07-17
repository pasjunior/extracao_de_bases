# Tratamento de Dados
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/pasjunior/tratamento_de_dados_python/blob/main/licence)

# Extração de dados de sistema web
## Descrição
Este código em Python é projetado para automatizar o processo de extração de dados de relatórios completos de duas páginas diferentes do sistema web. O código utiliza a biblioteca Selenium para controlar o navegador Chrome, preencher formulários, clicar em botões e efetuar o download dos relatórios. Ele também usa a biblioteca pySmartDL para monitorar o progresso do download e renomear os arquivos baixados de acordo com a empresa e o período especificado.
## Pré-requisitos
Antes de executar o código, certifique-se de ter instalado o Python e as seguintes bibliotecas:

* selenium: para automação de navegação no navegador Chrome
* pySmartDL: para monitoramento de downloads
* pwinput: para entrada segura da senha (não exibe a senha na tela)
* auto-py-to-exe: para criar um executável a partir do código Python (opcional, caso deseje transformar o código em um executável)

Você pode instalar as bibliotecas usando o comando pip install:
```python
pip install selenium pySmartDL pwinput auto-py-to-exe
```
## Como usar
1. Abra um terminal ou prompt de comando e navegue até o diretório em que o código está localizado.
2. Crie um ambiente virtual (opcional, mas recomendado) e ative-o usando os comandos:
```python
python -m venv venv
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```
3. Execute o código Python usando o comando:
```python
python extracao_versao_final.py
```
O código irá solicitar as seguintes informações ao usuário:

* Login: Insira o nome de usuário para acessar o sistema web da Energisa.
* Senha: Digite a senha de acesso ao sistema (a senha não será exibida na tela).
* Data inicial: Insira a data de início do período desejado no formato "dd.mm.aaaa".
* Data final: Insira a data de término do período desejado no formato "dd.mm.aaaa".

O código então iniciará o processo de extração dos dados dos relatórios completos das páginas para cada empresa. Os arquivos serão baixados no diretório de exportação escolhido pelo usuário.

## Funções principais
1. realizar_extracao_SACTK(url, caminho_exportacao, login, senha, data_inicial, data_final): Essa função realiza a extração dos dados da página SACTK do sistema web da Energisa. Ela recebe os parâmetros necessários para o processo de extração, incluindo a URL da página, o caminho de exportação dos arquivos baixados, o login e a senha do usuário, bem como as datas inicial e final do período desejado. A função automatiza o preenchimento do formulário, a seleção de datas e a exportação dos dados em formato CSV.

2. realizar_extracao_SAC(url, caminho_exportacao, login, senha, data_inicial, data_final): Essa função é semelhante à anterior, mas realiza a extração de dados da página SAC do sistema web da Energisa.

3. arquivo_completo(caminho_arquivo): Esta função verifica se o arquivo no caminho especificado está completamente baixado. Retorna True se o arquivo existe e não possui a extensão ".crdownload" (indicando que o download foi concluído), caso contrário, retorna False.

4. excluir_arquivos_nao_csv(caminho_exportacao): Essa função é responsável por excluir todos os arquivos no diretório de exportação que não possuem a extensão ".csv".

## Observações
* O código faz uso de algumas estruturas de repetição para lidar com possíveis problemas durante a extração dos dados, como falhas na página ou falhas no download. Essas estruturas de repetição podem ser otimizadas para melhorar a eficiência e a legibilidade do código.
* O código assume que o navegador Chrome e o respectivo driver do Chrome estão corretamente instalados no sistema. Caso contrário, é necessário instalar o Chrome e baixar o driver correspondente para a versão do Chrome instalada. O driver do Chrome pode ser baixado no seguinte link: https://sites.google.com/a/chromium.org/chromedriver/downloads

# Contribuições
Contribuições para o projeto são sempre bem-vindas! Caso você queira sugerir melhorias, correções de bugs ou novas funcionalidades, por favor, abra uma issue ou pull request.

## Nota de isenção de responsabilidade
Este código é fornecido apenas para fins educacionais e não possui garantias ou suporte. O uso deste código é de responsabilidade do usuário. É importante ressaltar que a automação de navegação em páginas da web pode violar os termos de serviço de alguns sites e ser considerada uma atividade não autorizada. Portanto, recomenda-se obter permissão do proprietário do site antes de automatizar qualquer processo. O autor deste código não se responsabiliza por qualquer uso inadequado ou ilegal deste código.
