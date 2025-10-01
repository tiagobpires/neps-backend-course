Ótima ideia\! Adicionar os comandos de conexão torna o guia muito mais prático.

Vamos atualizar a seção `### 2. Comandos Iniciais do Git` para incluir esses passos.

---

### 2\. Comandos do Git para Enviar o Projeto

Com os arquivos prontos, você pode iniciar o processo de versionamento e enviar seu código para o GitHub pela primeira vez.

1.  **Inicialize um repositório Git** na pasta do seu projeto (caso ainda não tenha feito):

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

4.  **Conecte seu projeto local ao repositório do GitHub.** Para este passo, você primeiro precisa **criar um repositório novo e vazio no site do GitHub**. Após criá-lo, o GitHub te dará uma URL (que termina em `.git`). Copie essa URL e use os comandos abaixo:

    - (Opcional, mas recomendado) Renomeie sua branch principal para `main`, que é o padrão atual:
      ```sh
      git branch -M main
      ```
    - Adicione o endereço do seu repositório remoto (do GitHub) ao seu projeto local. **Substitua `<URL_DO_SEU_REPOSITORIO>` pela URL que você copiou.**
      ```sh
      git remote add origin <URL_DO_SEU_REPOSITORIO>
      ```

5.  **Envie seus arquivos para o GitHub:**
    Agora, envie seu commit para o repositório no GitHub.

    ```sh
    git push -u origin main
    ```

    > O comando `-u` faz a ligação entre sua branch local e a do GitHub. Nas próximas vezes que for enviar atualizações, você só precisará usar `git push`.

Pronto\! Seu código agora está no GitHub, pronto para ser conectado à Vercel. Para um aprofundamento em todos esses comandos, não deixe de consultar o curso [**Git na Prática**](https://neps.academy/br/course/git-na-pratica).
