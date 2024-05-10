import numpy as np
import os
import tqdm
from scipy.io import wavfile

def split_wav(input_path, output_dir, chunk_seconds=5):
    filename = os.path.basename(input_path)
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 读取 WAV 文件的头部信息

    sample_rate, data = wavfile.read(input_path)

    print(f"The sample rate is: {sample_rate}")
    
    # 确保数据是浮点数，如果不是，需要转换
    if data.dtype.kind not in 'f':

        data = data.astype('float32')
    
    # 计算每个块的样本数
    num_samples = len(data)
    chunk_size = int(sample_rate * chunk_seconds)
    
    # 计算可以切分的完整块的数量
    num_full_chunks = num_samples // chunk_size
    
    # 存储所有音频块的列表
    chunks = []

    
    # 循环切分完整块

    for i in range(num_full_chunks):
        start = i * chunk_size
        end = start + chunk_size
        audio_chunk = data[start:end]
        chunks.append(audio_chunk)
    
    # 处理最后一个不完整的块
    remaining_samples = num_samples % chunk_size
    if remaining_samples > 0:
        start = num_full_chunks * chunk_size
        last_chunk = data[start:start + remaining_samples]

        chunks.append(last_chunk)
    
    # 写入所有音频块到 WAV 文件
    for i, audio_chunk in enumerate(chunks):
        # 创建输出文件的路径
        chunk_path = os.path.join(output_dir, f"{filename}_chunk_{i+1}.wav")
        
        # 写入切分后的音频块到新的 WAV 文件
        wavfile.write(chunk_path, sample_rate, audio_chunk)


feature_list = open("dataset/train_list.txt", 'r', encoding='utf-8')
for line in tqdm.tqdm(feature_list.readlines()):
    path, spk_id = line.replace('\n', '').split('\t')
    output_path = os.path.dirname(path).replace('data', 'test')
    split_wav(path, output_path)
