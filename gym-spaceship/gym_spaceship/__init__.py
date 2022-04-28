from gym.envs.registration import register

register(
    id="gym_spaceship/Spaceship-v0",
    entry_point="gym_spaceship.envs:SpaceshipEnv"
)