from environs import Env


env = Env()
env.read_env()
SECRET_KEY = env('SECRET_KEY')