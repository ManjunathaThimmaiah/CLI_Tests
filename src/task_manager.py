import subprocess
import pexpect
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def run_command(task, action, *args):
    logging.info(f"Executing action '{action}' on task '{task}' with arguments {args}")

    # Validate action
    if action not in ["list", "add", "delete"]:
        raise ValueError("Invalid action. Supported actions are 'list', 'add', and 'delete'.")

    # Construct command based on action
    if action == "list":
        command = f"{task} list"
    elif action == "add":
        additional_args = ' '.join(args)
        command = f"{task} add {additional_args}"
    elif action == "delete":
        additional_args = ' '.join(args)
        command = f"{task} delete {additional_args}"

    logging.info(f"Constructed command: {command}")

    # Execute command
    if action in ["list", "add"]:
        logging.info("Running command using subprocess")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        logging.info(f"Command output: {result.stdout}")
        if result.returncode != 0:
            logging.error(f"Error executing command: {command}")
            logging.error(f"Error output: {result.stderr}")
        return result
    elif action == "delete":
        logging.info("Running command using pexpect")
        child = pexpect.spawn(command)

        while True:
            try:
                index = child.expect([r'.*yes/no.*', pexpect.EOF, pexpect.TIMEOUT], timeout=10)
                if index == 0:
                    prompt = child.before.decode() + child.after.decode()
                    logging.info(f"Received prompt: '{prompt.strip()}'")
                    child.sendline("yes")
                    logging.info("Sent response: 'yes'")
                elif index == 1:
                    logging.info("End of output reached")
                    break
                elif index == 2:
                    logging.info("Timeout reached")
                    break
            except pexpect.exceptions.EOF:
                logging.info("EOF encountered")
                break
            except pexpect.exceptions.TIMEOUT:
                logging.info("Timeout encountered")
                break

        logging.info(f"Command output: {child.before.decode()}")
        exitstatus = child.wait()
        return exitstatus
