import os
import torch

'''训练'''
batch_size = 32 # 批次大小
max_explore_iterations = 5000 # 最大迭代大小
max_memory_size = 100000 # 最大内存大小
max_train_iterations = 100000 # 最大训练次数
save_interval = 10000 # 训练pkl保存间隔
save_dir = 'model_saved' # 训练pkl保存路径
frame_size = None # 框架尺寸根据布局自动计算
num_continuous_frames = 1 # 连续帧
logfile = 'train.log' # 日志文件保存位置
use_cuda = torch.cuda.is_available() # 使用cuda检测存在性
eps_start = 1.0 # 开始探索点
eps_end = 0.1 # 结束探索点
eps_num_steps = 10000 # 探索步数

'''测试'''
weightspath = os.path.join(save_dir, str(max_train_iterations)+'.pkl') # 调用训练集

'''游戏'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
SKYBLUE = (0, 191, 255)
layout_filepath = 'layouts/mediumClassic.lay' # 地图
num_element_types = 6
ghost_image_paths = [(each.split('.')[0], os.path.join(os.getcwd(), each)) for each in ['gameAPI/images/Blinky.png', 'gameAPI/images/Inky.png', 'gameAPI/images/Pinky.png', 'gameAPI/images/Clyde.png']]
scaredghost_image_path = os.path.join(os.getcwd(), 'gameAPI/images/scared.png')
pacman_image_path = ('pacman', os.path.join(os.getcwd(), 'gameAPI/images/pacman.png'))
font_path = os.path.join(os.getcwd(), 'gameAPI/font/ALGER.TTF')
grid_size = 32
ghost_action_method = 'random'