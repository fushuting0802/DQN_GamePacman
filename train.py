import config
from nets.nets import DQNet, DQNAgent
from gameAPI.game import GamePacmanAgent


'''训练模型'''
def train():
	game_pacman_agent = GamePacmanAgent(config)
	dqn_net = DQNet(config)
	dqn_agent = DQNAgent(game_pacman_agent, dqn_net, config)
	dqn_agent.train()

	
'''运行'''
if __name__ == '__main__':
	train()