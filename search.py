import sys
import os

default_rate = 1e-6

if __name__ == '__main__':
    init_rate = [default_rate * (10 ** k) for k in range(4)]
    param_list = [(rate, batch_size, num_unit) for rate in init_rate for batch_size in [4, 16, 32] for num_unit in [100, 200]]
    path = 'src/train.py'
    embeddings = 'ckip-word-embedding/Glove_CNA_ASBC_300d.txt'
    train = 'SSQA_concated_data/SSQA_train.txt'
    validation = 'SSQA_concated_data/SSQA_dev.txt'
    save_folder = 'save_'
    model = 'lstm'

    for index, (rate, batch, units) in enumerate(param_list):
        print (index, rate, batch, units)
        print ('python %s %s %s %s %s%d -r %s -b %s -u %s -d 0.9 -e 20 --use-intra' % (path, embeddings, train, validation, save_folder, index, rate, batch, units))
        os.system('mkdir %s%d' % (save_folder, index))
        os.system('python %s %s %s %s %s%d %s -r %s -b %s -u %s -d 0.9 -e 20 --use-intra' % (path, embeddings, train, validation, save_folder, index, model, rate, batch, units))
