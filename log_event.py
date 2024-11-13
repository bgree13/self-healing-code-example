import boto3
import logging
import watchtower  # for CloudWatch logging handler
import sys

# Set up AWS CloudWatch logging with watchtower
def setup_cloudwatch_logger():
    # Initialize the logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # Set to the desired logging level

    # AWS CloudWatch handler using watchtower
    cloudwatch_handler = watchtower.CloudWatchLogHandler(
        log_group="self-healing-cw-log",  # Replace with your CloudWatch Log Group
        stream_name="self-healing-log-stream",  # Replace with your CloudWatch Stream Name
        boto3_client=boto3.client("logs")  # Create a CloudWatch Logs client
    )
    
    # Set handler format and add to logger
    cloudwatch_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(cloudwatch_handler)
    
    return logger

def main():
    # Setup CloudWatch logging
    logger = setup_cloudwatch_logger()

    # Test log messages
    logger.info("This is an info log message.")
    logger.error("This is an error log message.")

    # Your application logic here
    for i in range(5):
        logger.info(f"Processing item {i}")
    
    print("Finished logging to CloudWatch.")
     
   
    try:
      run_my_stuff()
    except:
      logger.exception('Got exception on main handler')
      raise 

if __name__ == "__main__":
    main()