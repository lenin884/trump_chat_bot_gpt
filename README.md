# Chatbot imitating Donald Trump

## Overview selected method
The transformers approach was chosen to implement the chatbot. 
To implement the sequence to sequence task (our chat bot), a pre-trained DialoGPT-small model was selected.

## Need requirements
Create local environment
```
python3 -m venv venv
```

Setup requirements
```
python3 -m pip install -r requirements.txt
```

## Download and prepare dataset
To form a dataset, we use the proposed site. Parse the data and create a DataFrame with the fields: response, context
```
python prepare_dataset.py
```

## Train and evaluate model
We will train and evaluate the model
```
python train.py
```

## Run chatting

### Loading the trained model
Check url "" and download this archive in output-small folder in project

Next command with archive
```shell
unzip archive.zip
rm archive.zip
```

Script to start the chat. To exit the chat, you need to enter "exit"
```
python run.py
```