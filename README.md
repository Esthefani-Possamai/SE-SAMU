# Instruções para rodar o projeto - Ubunto
![image](https://github.com/user-attachments/assets/607352d3-d229-43fc-b985-d8115b349c92)

## Pré-requisitos

Certifique-se de ter o Python 3 instalado em seu sistema. Caso não tenha, instale o Python 3 e o `pip` (gerenciador de pacotes).

## Passos para Rodar o Projeto

### 1. Instalar o pacote `python3-venv`
O `python3-venv` é necessário para criar um ambiente virtual. Para instalá-lo, execute o seguinte comando:

```bash
sudo apt install python3-venv
```

A pasta venv deve estar dentro deste projeto, como abaixo:

![image](https://github.com/user-attachments/assets/2724935a-402e-4a0a-8579-a55eedf35564)


### 2. Inicializar
```bash
python3 -m venv venv
```

###3. Rodar o projeto na porta 5001
```bash
python3 app.py
```
