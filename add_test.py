import random
import os

# 提取特征保存文件
def add_test_features(save_dir='dataset/'):
    all_data_list = os.path.join(save_dir, 'all_list_features.txt').replace('\\', '/')
    train_data_list = all_data_list.replace("all", "train")
    test_data_list = all_data_list.replace("all", "test")
    enroll_data_list = all_data_list.replace("all", "enroll")

    feature_list = open("dataset/all_list_features.txt", 'r', encoding='utf-8')
    train_list = open(train_data_list, 'w', encoding='utf-8')
    test_list = open(test_data_list, 'w', encoding='utf-8')
    enroll_list = open(enroll_data_list, 'w', encoding='utf-8')
    id = 0
    for line in feature_list.readlines():
        _, spk_id = line.replace('\n', '').split('\t')
        if spk_id != id:
            id = spk_id
            enroll_list.write(line)
            train_list.write(line)
        else:
            if random.random() < 0.1:
                test_list.write(line)
            else:
                train_list.write(line)

def create_cn_instrument(data_path='dataset/'):
    f_train = open("dataset/all_list_features.txt", 'w', encoding='utf-8')
    data_dir = os.path.join(data_path, 'features_MelSpec/')
    dirs = sorted(os.listdir(data_dir))
    for _, d in enumerate(dirs):
        for file in os.listdir(os.path.join(data_dir, d)):
            sound_path = os.path.join(data_dir, d, file).replace('\\', '/')
            f_train.write(f'{sound_path}\t{d}\n')
    f_train.close()

if __name__ == '__main__':
    create_cn_instrument()
    add_test_features()
