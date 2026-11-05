Projeto Prático: Gerenciamento de Configuração de Software (Docker + Kubernetes)

Este repositório contém a infraestrutura e a aplicação de demonstração desenvolvidas para a avaliação da disciplina de Gerenciamento da Configuração de Software (GCS). O projeto ilustra o ciclo de vida completo de uma aplicação moderna conteinerizada, desde o versionamento de código e build de imagens até a orquestração local com Kubernetes (Minikube), contemplando escalabilidade, rolling updates e balanceamento de carga.

🛠️ Stack Tecnológica

Linguagem: Python (Flask)

Conteinerização: Docker (Dockerfile)

Orquestração Local: Kubernetes / Minikube

Controle de Versão: Git e GitHub

📋 0. Instalação Inicial do Ambiente (Windows com Winget)

Caso ainda não tenha as ferramentas necessárias instaladas no seu computador, é possível efetuar a instalação de forma rápida e automatizada no Windows utilizando o gerenciador de pacotes winget por meio do PowerShell (executado como Administrador):

Instalar o Docker Desktop:

winget install -e --id Docker.DockerDesktop



Instalar o Minikube:

winget install -e --id Kubernetes.minikube



Instalar o kubectl:

winget install -e --id Kubernetes.kubectl



Nota Importante (Virtualização e WSL2): Certifique-se de que a virtualização de hardware está ativa na BIOS/UEFI do seu computador e de que o suporte ao WSL2 (Windows Subsystem for Linux) ou ao Hyper-V está ativado nos Recursos do Windows. Sem a virtualização habilitada, o Docker Desktop e o cluster Minikube não conseguirão inicializar os contêineres.

📥 0.1. Como Obter e Baixar o Projeto do GitHub

Antes de avançar para a execução da aplicação e gestão dos contêineres, clone o repositório do projeto para a sua máquina local utilizando o Git no seu terminal:

git clone https://github.com/edug15/trabalho-docker-kubernetes.git



Após baixar o repositório, acesse a pasta do projeto antes de prosseguir com os passos de configuração:

cd trabalho-docker-kubernetes



🚀 1. Passo a Passo para Execução da Demonstração

Com o projeto já descarregado no seu computador e o terminal aberto na pasta raiz (trabalho-docker-kubernetes), siga a sequência abaixo:

Passo 1: Iniciar o Cluster Kubernetes Local

Inicie o ambiente virtualizado do Kubernetes através do Minikube. Isso criará o nó de trabalho necessário dentro do Docker Desktop.

minikube start



Passo 2: Construir a Imagem Docker da Aplicação

Construa a imagem da aplicação utilizando o Dockerfile presente na pasta do projeto. Atribua a tag correspondente à versão atual (ex: app:2.0):

docker build -t app:2.0 .



Passo 3: Carregar a Imagem para dentro do Minikube

Como o Minikube roda isolado em um contêiner próprio, é necessário injetar a imagem construída localmente para que o cluster consiga utilizá-la:

minikube image load app:2.0



Passo 4: Aplicar os Manifestos de Infraestrutura (Deployment e Service)

Utilize o kubectl para ler os arquivos de configuração localizados na pasta kubernetes/ e criar os recursos de deployment (gerenciamento das réplicas) e o service (balanceamento de carga interno):

kubectl apply -f kubernetes/



Passo 5: Escalar a Aplicação (Validação de Escalabilidade)

Para demonstrar o conceito de escalabilidade em tempo real e o balanceamento de carga, escale o número de instâncias (Pods) da aplicação para 5:

kubectl scale deployment demo-gcs --replicas=5



Confirme se todos os pods estão ativos e em execução com sucesso:

kubectl get pods



Passo 6: Aceder à Aplicação no Navegador

Para expor o serviço do Kubernetes de forma segura e interativa no seu computador (evitando problemas de cache do navegador), execute o comando de túnel do Minikube:

minikube service demo-gcs



O que acontece: O Minikube irá gerar automaticamente um endereço dinâmico local (por exemplo, http://127.0.0.1:xxxxx) e abrir a página web no seu navegador padrão.

Demonstração do Balanceamento: Se abrir o link em uma nova janela anônima ou recarregar várias vezes, você verá o identificador do Pod alternando dinamicamente na interface gráfica, comprovando que o tráfego está sendo distribuído uniformemente pelas 5 réplicas.

🔄 2. Como Atualizar a Aplicação após Alterações no Código

Caso faça alguma modificação no código-fonte em Python ou no HTML da página, execute os seguintes comandos para atualizar o ambiente sem perder a estrutura:

Reconstruir a imagem Docker:

docker build -t app:2.0 .



Recarregar a imagem no Minikube:

minikube image load app:2.0



Aplicar a atualização no cluster (Rolling Update):

kubectl apply -f kubernetes/deployment.yaml



🧹 3. Procedimento de Encerramento e Limpeza do Ambiente

Após concluir a avaliação ou os testes, utilize os comandos abaixo para excluir os recursos do Kubernetes e desligar o cluster, liberando os recursos da sua máquina:

kubectl delete -f kubernetes/
minikube stop

