from configparser import ConfigParser

config = ConfigParser()


#config.read('project_config.ini')


# user = config['database']['user']
# password = config['database']['password']
# host = config['database']['host']
# port = config['database']['port']
# db = config['database']['db']
DATABASE_URI = 'sqlite:///user.sqlite3'  # "mysql://" + user + ":" + password + "@" + host + ":" + port + "/" + db

# ERROR_LOG_PATH = config['log']['path']

# MASTER_QUERY = config['mysql']['master_query']
