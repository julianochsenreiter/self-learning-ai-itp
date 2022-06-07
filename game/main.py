from stable_baselines3 import A2C, DQN, PPO
from AIManager import GatherData

def main():
  GatherData(A2C)
  GatherData(DQN)
  GatherData(PPO)

if __name__ == "__main__":
  main()