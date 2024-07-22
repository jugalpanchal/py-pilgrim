from unittest.mock import MagicMock

# Create a mock logger
logger = MagicMock()

# Replace the 'info' method of the logger with a print statement
logger.info = print

# Now, when you call logger.info, it will actually print the message
env = 'local'
logger.info('running on {env}')
