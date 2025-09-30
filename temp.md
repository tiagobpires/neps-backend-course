## Adicionar o projeto no GitHub

Utilizaremos a Vercel em conjunto com o GitHub. A Vercel se conecta ao seu repositório e, a cada atualização que você envia (`git push`), ela automaticamente faz um novo deploy da sua aplicação. Portanto, o primeiro passo é ter seu projeto em um repositório no GitHub.

O processo completo de como usar o Git e o GitHub está detalhado no curso [**Git na Prática**](https://neps.academy/br/course/git-na-pratica). A seguir, vamos mostrar os passos essenciais para preparar seu projeto.

### 1\. Preparando os Arquivos

Antes de enviar seu código, precisamos garantir que dois arquivos importantes estejam corretos.

**Atualize as dependências**

O arquivo `requirements.txt` lista todos os pacotes Python que seu projeto precisa para funcionar. A Vercel usará este arquivo para instalar tudo corretamente. Para garantir que ele está atualizado, execute o comando no seu terminal:

```sh
pip freeze > requirements.txt
```

**Crie o arquivo `.gitignore`**

Este arquivo diz ao Git quais arquivos e pastas devem ser ignorados. Isso é crucial para não enviar segredos (como senhas no arquivo `.env`) ou pastas desnecessárias para o seu repositório público. Crie um arquivo chamado `.gitignore` e adicione o seguinte conteúdo:

```git
# Arquivo com segredos e variáveis de ambiente
.env

# Pasta do ambiente virtual
venv/

# Pasta de cache do Python
__pycache__/
```

> O arquivo ".env", a pasta "venv" e as pastas de cache do Python não serão enviados para o GitHub.

### 2\. Comandos Iniciais do Git

Com os arquivos prontos, você pode iniciar o processo de versionamento com o Git.

1.  **Inicialize um repositório Git** na pasta do seu projeto:

    ```sh
    git init
    ```

2.  **Adicione todos os arquivos** para o controle do Git:

    ```sh
    git add .
    ```

3.  **Crie o "commit" inicial**, que é um "ponto de salvamento" do seu projeto:

    ```sh
    git commit -m "Commit inicial da API"
    ```

> A partir daqui, os próximos passos são: criar um repositório vazio no site do GitHub, conectar seu projeto local a ele e enviar suas alterações (`git push`). Você pode ver o passo a passo detalhado de como fazer isso na [aula do curso de Git](https://neps.academy/br/course/git-na-pratica).
