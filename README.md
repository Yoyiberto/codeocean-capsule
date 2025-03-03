# Code Ocean Capsule Example

This repository contains a simple Python script designed to be run in a Code Ocean capsule.

## Structure

- `code/`: Contains the Python script
  - `main.py`: Main Python script that processes data
- `data/`: Contains input data
  - `sample.json`: Sample data file
- `results/`: Directory where results will be saved
- `Dockerfile`: Defines the Docker environment
- `requirements.txt`: Lists Python dependencies
- `run`: Bash script that runs the code

## How to Use

### On Code Ocean

1. Create a new capsule from this GitHub repository
2. Click "Reproducible Run" to execute the code
3. Results will be saved in the `/results` directory

### Locally

To run this code locally with Docker:

```bash
# Build the Docker image
docker build -t codeocean-example .

# Run the container
docker run -v $(pwd)/data:/data -v $(pwd)/results:/results codeocean-example /code/run
```

## Dependencies

- Python 3.9
- NumPy
- Pandas
- Matplotlib
- tqdm
- PyYAML

## Output

The script will generate a JSON file in the `/results` directory containing:
- Timestamp of execution
- Number of input files found
- List of input files
- A sample message

## License

MIT 