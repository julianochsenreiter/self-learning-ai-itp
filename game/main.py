import gym_spaceship
import gym

def main():
    env = gym.make("gym_spaceship/Spaceship-v0")
    env.action_space.seed(1337)

    observation, info = env.reset(return_info=True)

    while True:
        observation, reward, done, info = env.step(env.action_space.sample())
        env.render()
        # print(f"{reward>0=}")

        if done:
            observation, info = env.reset(return_info=True)

    env.close()

if __name__ == "__main__":
    main()