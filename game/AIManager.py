import os
from typing import Tuple

import gym
import numpy as np
import matplotlib.pyplot as plt

import gym_spaceship
import stable_baselines3

from stable_baselines3 import DQN
from stable_baselines3.common import results_plotter
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.results_plotter import load_results, ts2xy, plot_results
from stable_baselines3.common.noise import NormalActionNoise
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.off_policy_algorithm import BaseAlgorithm

class SaveOnTimestampRewardCallback(BaseCallback):
  """
  Callback for saving a model (the check is done every ``check_freq`` steps)
  based on the training reward (in practice, we recommend using ``EvalCallback``).

  :param check_freq:
  :param log_dir: Path to the folder where the model will be saved.
    It must contains the file created by the ``Monitor`` wrapper.
  :param verbose: Verbosity level.
  """
  def __init__(self, check_timestamps: Tuple[int], update_best_frequency: int, log_dir: str, verbose: int = 1):
    super(SaveOnTimestampRewardCallback, self).__init__(verbose)
    self.check_timestamps = check_timestamps
    self.check_freq = update_best_frequency
    self.save_path = log_dir
    self.data_path = os.path.join(log_dir, "data.csv")
    self.best_mean_reward = -np.inf
    
    self.createDataFile()

  def _init_callback(self) -> None:
    # Create folder if needed
    if self.save_path is not None:
        os.makedirs(self.save_path, exist_ok=True)
  
  def createDataFile(self):
    with open(self.data_path, "w+") as f:
      f.write("timestamp,reward\n")
      print(f"File {self.data_path} Created")

  def _on_step(self) -> bool:
    if self.num_timesteps in self.check_timestamps:
      # Example for saving best model
      if self.verbose > 0:
        print(f"Saving best model at {self.num_timesteps} to {self.save_path}")
      self.model.save(os.path.join(self.save_path, f'best_model_{self.num_timesteps}'))
    
    if self.n_calls % self.check_freq == 0:
      # Retrieve training reward
      x, y = ts2xy(load_results(self.save_path), 'timesteps')
      if len(x) > 0:
          # Mean training reward over the last 100 episodes
          mean_reward = np.mean(y[-self.check_freq:])
          if self.verbose > 0:
            print(f"Num timesteps: {self.num_timesteps}")
            print(f"Best mean reward: {self.best_mean_reward:.2f} - Last mean reward per episode: {mean_reward:.2f}")

          # New best model, you could save the agent here
          if mean_reward > self.best_mean_reward:
              self.best_mean_reward = mean_reward
          
          with open(self.data_path, "a") as file:
            file.write(f"{self.num_timesteps},{mean_reward}\n")

    return True

def GatherData(cls: type[BaseAlgorithm]):
  # log dir
  log_dir = f"data/{cls.__name__}"
  os.makedirs(log_dir, exist_ok=True)

  env = gym.make('gym_spaceship/Spaceship-v0')
  env = Monitor(env, log_dir)
  
  # MultiInputPolicy weil Dictionary
  model = cls('MultiInputPolicy', env)
  
  timestamps = [100000, 330000, 660000, 1000000, 2000000, 3000000]

  callback = SaveOnTimestampRewardCallback(check_timestamps=timestamps,update_best_frequency=10000, log_dir=log_dir)
  
  timesteps = max(timestamps)
  model.learn(total_timesteps=int(timesteps), callback=callback)

  plot_results([log_dir], timesteps, results_plotter.X_TIMESTEPS, "Spaceship")
  plt.show()

def Load(path: str, alg: type[BaseAlgorithm]):
  env = gym.make('gym_spaceship/Spaceship-v0')

  model = alg.load(path, env)
  # print(model)

  # Enjoy trained agent
  obs = env.reset()
  for i in range(10000):
      # print(f"run {i}")
      action, _states = model.predict(obs, deterministic=True)
      obs, rewards, done, info = env.step(action)
      if done:
        env.reset()
      env.render()