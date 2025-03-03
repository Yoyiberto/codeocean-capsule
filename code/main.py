#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple Python script for Code Ocean capsule demonstration
"""

import os
import sys
import logging
import datetime
import json

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def process_data(input_dir, output_dir):
    """
    Process data from input directory and save results to output directory
    
    Args:
        input_dir (str): Path to input data directory
        output_dir (str): Path to output results directory
    """
    logger.info("Starting data processing")
    
    # Debug log for directories
    logger.debug(f"Input directory: {input_dir}")
    logger.debug(f"Output directory: {output_dir}")
    
    try:
        # Check if input directory exists and has files
        if not os.path.exists(input_dir):
            logger.warning(f"Input directory {input_dir} does not exist")
            return
        
        # List files in input directory
        input_files = os.listdir(input_dir)
        logger.info(f"Found {len(input_files)} files in input directory")
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Sample data processing (just a demonstration)
        results = {
            "timestamp": datetime.datetime.now().isoformat(),
            "num_input_files": len(input_files),
            "input_files": input_files,
            "message": "Hello from Code Ocean!"
        }
        
        # Save results to output file
        output_file = os.path.join(output_dir, "results.json")
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        logger.info(f"Results saved to {output_file}")
        
    except Exception as e:
        logger.error(f"Error processing data: {str(e)}")
        raise

def main():
    """Main function to run the script"""
    logger.info("Script started")
    
    # Get input and output directories from environment or use defaults
    # Code Ocean mounts /data and /results automatically
    input_dir = os.environ.get("INPUT_DIR", "/data")
    output_dir = os.environ.get("OUTPUT_DIR", "/results")
    
    # Process the data
    process_data(input_dir, output_dir)
    
    logger.info("Script completed successfully")

if __name__ == "__main__":
    main() 