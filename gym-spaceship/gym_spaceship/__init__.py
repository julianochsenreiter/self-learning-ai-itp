from gym.envs.registration import register

register(
    id="Spaceship-v0",
    entry_point="gym_spaceship.envs:SpaceshipEnv"
)