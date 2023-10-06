import torch
import config
from nets.nets import DQNet, DQNAgent
from gameAPI.game import GamePacmanAgent


'''测试运行'''
def runDemo():
	game_pacman_agent = GamePacmanAgent(config)
	dqn_net = DQNet(config)
	dqn_net.load_state_dict(torch.load(config.weightspath))
	dqn_agent = DQNAgent(game_pacman_agent, dqn_net, config)
	dqn_agent.test()


'''运行'''
if __name__ == '__main__':
	runDemo()