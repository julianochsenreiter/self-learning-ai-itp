import gym_spaceship
import gym

def main():
    env = gym.make("gym_spaceship/Spaceship-v0")
    env.action_space.seed(42)

    observation, info = env.reset(seed=42, return_info=True)

    for _ in range(1000):
        observation, reward, done, info = env.step(env.action_space.sample())
        env.render()

        if done:
            observation, info = env.reset(return_info=True)

    env.close()

if __name__ == "__main__":
    main()