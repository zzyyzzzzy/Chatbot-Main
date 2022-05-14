# chatbot

A restaurant chatbot developed using RASA framework

## To connect to the Chatbot user interface [Chatbot UI](https://github.com/zzyyzzzzy/Chatbot-UI)

0. Setup environment

```
conda create --name myenv
```

1. Install rasa (make sure python3.7 or 3.8)

```
pip install rasa
```

2. Run action server

```
rasa run actions --cors "*" --debug
```

3. Run duckling server provided by RASA for number handling (make sure you have docker installed)

```
docker run -p 8000:8000 rasa/duckling
```

4. Run models with api enabled

```
rasa run -m models --enable-api --cors "*" --debug
```

5. Head to [Chatbot UI](https://github.com/zzyyzzzzy/Chatbot-UI) and run front-end server and You are good to go!!

## To setup and test the current model in iteractive mode

0. Setup environment

```
conda create --name myenv
```

1. Install rasa (make sure python3.7 or 3.8)

```
pip install rasa
```

2. Run the model in production

```
rasa shell
```

3. If error encountered due to import form sanic, try

```
pip install sanic==21.9.3
```

## To train

1. Add more data in stories/rules folder
2. Run the following command

```
rasa train
```
