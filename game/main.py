import gym_spaceship
import gym

def main():
    env = gym.make("gym_spaceship/Spaceship-v0")
    seed = 42042
    env.action_space.seed(seed)
    highscore = 0

    observation, info = env.reset(return_info=True)
    gen = 1
    try:
        while True:
            observation, reward, done, info = env.step(env.action_space.sample())
            # env.render()

            if done:
                observation, info = env.reset(seed=seed,return_info=True)
                score = info["score"]
                if score > highscore:
                    highscore = score
                    print(f"gen {gen} new highscore ({highscore})")
                print(f"gen {gen} {score=}/{highscore}")
                gen += 1
    finally:
        env.close()

if __name__ == "__main__":
    main()