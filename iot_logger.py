import logging
import os
import sys
import subprocess

def fix_permissions(path):
    """
    Runs Windows icacls to ensure the current user and SYSTEM 
    have full access to the log folder/file.
    """
    if os.name == 'nt':  # Only run on Windows
        try:
            # Grant Full access to the current logged-in user
            username = os.environ.get('USERNAME')
            subprocess.run(['icacls', path, '/grant', f'{username}:F', '/T'], 
                           capture_output=True, check=True)
            
            # Grant Full access to SYSTEM (for the Mosquitto Service)
            subprocess.run(['icacls', path, '/grant', 'SYSTEM:F', '/T'], 
                           capture_output=True, check=True)
        except Exception as e:
            print(f"Warning: Could not set permissions: {e}")

def get_mqtt_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        project_root = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(project_root, "logs")
        
        # 1. Create directory if missing
        os.makedirs(log_dir, exist_ok=True)
        
        # 2. Fix Permissions on the directory immediately
        fix_permissions(log_dir)

        log_path = os.path.join(log_dir, "mqtt_system.log")
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # File Handler
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)

        # Console Handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.DEBUG)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger