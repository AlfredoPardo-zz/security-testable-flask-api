import yaml

def get_config():

    with open("config.yaml") as f:
    
        config = yaml.load(f, Loader=yaml.FullLoader)
    
    if config:
        
        return config

    else:

        return None