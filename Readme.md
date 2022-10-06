# Microsserviço para fazer Scraping em Sites

## Pré-requisitos
É Necessario criar um ambiente virtual com o seguinte comando:

> python -m venv venv

Em seguida ativar o ambiente virtual

Windows:
> venv/Scripts/Activate

Unix:
> source venv/bin/activate

Instalar as libs que iremos utilizar neste projeto:
> pip install -r requirements.txt

## Execução

Caso precise executar os logs no modo debug, basta setar a env "debug": "true".

> python main.py


## Execução do Unittest

> python test/test.py

## Formatação de código

Foi utilizado o formatador de códigos black==22.8.0

Para formatar:
> black ./  
> ou o path do arquivo que precisa formatar

## VS Code

Caso esteja utilizando o Visual Studio Code para executar o projeto, segue uma configuração do launch.json

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid": "830387
    "version": "0.1.0",
    "configurations": [
        {
            "name": "Web Scraping - Service",
            "type": "python",
            "request": "launch",
            "program": "main.py",
            "console": "integratedTerminal",
            "env": {
                "debug": "false"
            }
        }
    ]
}
```