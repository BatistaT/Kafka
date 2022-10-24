Primeiramente acessar a pasta docker

cd docker

rodar o docker para subir os containers do kafka

docker-compose up -d

volte para a raiz do projeto

cd ..

rodar consumer.py para acompanhar a chegada de mensagens

py ./consumer.py

deixe o terminal do consumer aberto e abra outro terminal para rodar o producer para fazer o envio das mensagens

py ./producer.py
