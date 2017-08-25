# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import argparse
from itertools import izip
import tensorflow as tf
import sys

import utils
import ioutils
import uniout
"""
Evaluate the performance of an NLI model on a dataset
"""
def print_errors(labels, sents1, sents2,  answers, label_dict):
    """
    Print the pairs for which the model gave a wrong answer,
    their gold label and the system one.
    """
    text = open('Error_bc.txt', 'w')

    for label, sent1, sent2, answer in izip(labels, sents1, sents2, answers):
        label_str = str(label)
        label_str.encode('ascii')
        #text.write('\nSystem label: {}, gold label: {}\n'.format(answer, label_str))
        #text.write(sent1.encode('utf-8') + sent2.encode('utf-8'))
        if label_str == "Y\n":
            label_number = 0
        elif label_str == "N\n":
            label_number = 1   
        else:
            label_number = -1
        
        if answer != label_number:
            text.write('\nSystem label: {}, gold label: {}\n'.format(answer, label_number))
            text.write(sent1.encode('utf-8') + sent2.encode('utf-8'))

            #print('Sent 1: {}\n Sent 2: {}'.format(sent1.encode('utf-8'), sent2.encode('utf-8')))
            print(sent1.encode('utf-8') + sent2.encode('utf-8'))
            print('System label: {}, gold label: {}'.format(answer, label_number))
            #print('Answer Index: %d\n' % answers.index(answer))
       
      
       
    text.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('model', help='Directory with saved model')
    parser.add_argument('dataset',
                        help='JSONL or TSV file with data to evaluate on')
    parser.add_argument('embeddings', help='Numpy embeddings file')
    parser.add_argument('--vocabulary',
                        help='Text file with embeddings vocabulary')
    parser.add_argument('-v',
                        help='Verbose', action='store_true', dest='verbose')
    parser.add_argument('-e',
                        help='Print pairs and labels that got a wrong answer',
                        action='store_true', dest='errors')
    args = parser.parse_args()

    utils.config_logger(verbose=args.verbose)
    params = ioutils.load_params(args.model)
    sess = tf.InteractiveSession()

    model_class = utils.get_model_class(params)
    model = model_class.load(args.model, sess)
    word_dict, embeddings = ioutils.load_embeddings(args.embeddings,
                                                    args.vocabulary,
                                                    generate=False,
                                                    load_extra_from=args.model,
                                                    normalize=True)
    model.initialize_embeddings(sess, embeddings)
    label_dict = ioutils.load_label_dict(args.model)
    print('Label dict[Y] : ',label_dict['Y'])
#    pairs = ioutils.read_corpus(args.dataset, params['lowercase'],
                     #           params['language'])
    #dataset = utils.create_dataset(pairs, word_dict, label_dict)
    dataset, labels, sents1, sents2 = utils.create_dataset_SSQA(args.dataset, word_dict, label_dict)
    #for pair in pairs:
        #print(pair[0].encode('utf-8'))
        #print(pair[1].encode('utf-8'))
        #print(pair[2].encode('utf-8'))
    loss, acc, answers = model.evaluate(sess, dataset, True)
    print('Loss: %f' % loss)
    print('Accuracy: %f' % acc)
    print('answer from evaluate.py')
    print(answers)
    if args.errors:
        print_errors(labels, sents1, sents2, answers, label_dict)
