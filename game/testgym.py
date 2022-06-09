import gym_spaceship
import gym
from gym.utils.env_checker import check_env

env = gym.make("gym_spaceship/Spaceship-v0")
check_env(env)