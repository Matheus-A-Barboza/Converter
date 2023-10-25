# Conversor de Notas Fiscais de XML para Excel e PDF

Este é um aplicativo Python de desktop que permite aos usuários converter arquivos XML de Notas Fiscais em Excel (XLSX) e PDF. É uma ferramenta útil para extrair informações de notas fiscais e salvá-las em um formato mais fácil de ler e compartilhar.

## Funcionalidades Principais

- **Seleção de Arquivos XML**: Os usuários podem selecionar múltiplos arquivos XML de notas fiscais através do botão "Selecionar Arquivos XML". Os arquivos selecionados são listados na interface do aplicativo.

- **Conversão para Excel**: Ao clicar no botão "Converter para Excel", o aplicativo extrai informações relevantes dos arquivos XML selecionados e cria um arquivo Excel (XLSX) chamado "NotasFiscais.xlsx". As informações incluem o número da nota, empresa emissora, nome do cliente, logradouro, bairro, município, UF, peso, valor da nota, valor do ICMS, valor do imposto, valor de desconto, COFINS e quantidade de produtos.

- **Conversão para PDF**: O aplicativo também permite a conversão dos arquivos XML em PDF. Isso é feito através do serviço online "onlineconvertfree.com". Os PDFs resultantes são abertos automaticamente no navegador padrão do usuário após a conversão.

## Como Usar

1. Execute o aplicativo.

2. Clique no botão "Selecionar Arquivos XML" para escolher os arquivos XML das notas fiscais que você deseja converter.

3. Após selecionar os arquivos XML, você pode clicar no botão "Converter para Excel" para criar um arquivo Excel com as informações das notas fiscais.

4. Se você preferir converter para PDF, clique no botão "Converter para PDF". Os PDFs serão abertos automaticamente em seu navegador padrão após a conversão.

## Requisitos

- Python 3.x
- Bibliotecas Python: requests, PySide6, xmltodict, pandas, tempfile, os, webbrowser

## Notas

- Certifique-se de ter todas as bibliotecas Python necessárias instaladas antes de executar o aplicativo.

- Este aplicativo foi desenvolvido como uma ferramenta de conversão simples para notas fiscais em XML. Alterações ou melhorias adicionais podem ser implementadas de acordo com suas necessidades.

- Este aplicativo foi desenvolvido por [Matheus]. Você é livre para usar, modificar e distribuir de acordo com os termos da licença aplicável.

- Qualquer problema ou sugestão de melhoria pode ser relatado [aqui](https://github.com/Matheus-A-Barboza/Converter/issues).

Divirta-se convertendo suas notas fiscais em Excel e PDF!
