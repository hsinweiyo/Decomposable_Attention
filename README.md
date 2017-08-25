# Decompoasble Attention Model with Chinese Social Studties Question Answering

The code is modified from [here](https://github.com/erickrf/multiffn-nli), which is working on [A Decomposable Attention Model for Natural Language Inference] (https://arxiv.org/abs/1606.01933). While I am working on the Chinese project of Social Studies, we have to find out if its entailment relation between hypothesis and evidence search result is True or False. Thanks to [Eric] (https://github.com/erickrf), who replied my question patiently.

## Getting Started

Implemented by Tensorflow 1.2.0, so mainly you will need python 2.7.

### Prerequisites

You should have your own word embedding in the file you store your data.
[Download GloVe] (https://nlp.stanford.edu/projects/glove/) if you don't have it.

### Installing

Go to the file you want to store this code. Then clone it down.

```
git clone https://github.com/hsinweiyo/Decomposable_Attention.git
```

## Usage

Make sure that you have all the file that you should have mentioning in train.py.

```
python src/train.py -h
```

Make a empty file for your saved model

```
mkdir saved-model
```

For example you might want to train the model with mlp and with the suggested hyperparameters: 20 epochs, 4 batch size, 150 hidden units, 0.8 keep dropout, 0.001 rate, 0 l2 normalization, default algorithm.

```
python src/train.py glove.840B.300d.txt snli_1.0/snli_1.0_test.txt snli_1.0/snli_1.0_dev.txt saved-model mlp -e 20 -b 4 -u 150 -d 0.8 -r 0.001
```

Or an alternative way, you want to train models in Chinese, then you need to add a --chinese, for instance

```
python src/train.py chinese_glove.txt your_snli_train.txt your_snli_dev.txt saved-model mlp --chinese
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Python 2.7](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Tensorflow 1.2](https://maven.apache.org/) - Dependency Management
* Several libraries, such as nltk, uniout, xlwt, pip install if you miss any of it

## Authors

* **Erick Rocha Fonseca** - Re-implement - [his work](https://github.com/erickrf)
* **David Huang** - convert input language - [his work](https://github.com/chuangag)
* **Evelyn Hsin-Wei Yo ** - Removing conjuntion - [Hsin-Wei](https://github.com/hsinweiyo) 


## Acknowledgments

* Much more faster using GPUs
* There will be a xls file in the saved-model file which stores the hyperparameters and information of every time we saved models, it is useful to dig into the data
