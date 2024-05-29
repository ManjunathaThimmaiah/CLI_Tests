### README.md

```markdown
# My Project

This project is a Python-based task management system that uses Taskwarrior and includes automated tests using the `unittest` framework. The project is set up to use GitHub Actions for continuous integration.

### Features

- Task Management: Interact with Taskwarrior to manage tasks.
- Automated Testing: Uses `unittest` framework for testing.
- Continuous Integration: GitHub Actions configured to run tests on every push and pull request.

## Installation

### Prerequisites

- Python 3.9
- Taskwarrior

```

### Setting Up the Environment

1. Clone the repository:

   ```sh
   git clone git@github.com:ManjunathaThimmaiah/CLI_Tests.git
   cd CLI_Tests
   ```

2. Create a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   .\venv\Scripts\activate   # On Windows
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Install Taskwarrior:

   On Ubuntu:

   ```sh
   sudo apt-get update
   sudo apt-get install -y taskwarrior
   ```

## Running the Tests

To run all tests, use the following command:

```sh
python run_tests.py
```

## Continuous Integration

This project uses GitHub Actions for continuous integration. The configuration file is located at `.github/workflows/actions.yml`.

### GitHub Actions Workflow

The workflow is triggered on every push and pull request to the `main` branch. It performs the following steps:

1. Checks out the repository.
2. Installs Taskwarrior.
3. Sets up Python 3.9.
4. Installs the dependencies.
5. Runs the tests.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.



### Scenario 1: Add cart, update the cart, Delete the cart

`tests/test_integration.py`

1. **List Tasks (Initial State)**
   - Action: Retrieve the list of existing tasks.
   - Expected Result: The response status code is 200 OK, and the list of tasks is retrieved successfully. Note the initial number of tasks.

2. **Add a New Task**
   - Action: Create a new task with specific details such as title, description, and due date.
   - Expected Result: The response status code is 201 Created, and the task data returned matches the input payload. Note the ID of the newly created task.
  
3. **List Tasks (Confirm the New Task is Added)**
   - Action: Retrieve the list of tasks again.
   - Expected Result: The response status code is 200 OK, and the list now includes the newly added task. Verify that the number of tasks has increased by one compared to the initial state.
     
4. **Delete the Added Task**
   - Action: Delete the newly added task using its ID.
   - Expected Result: The response status code is 200 OK, confirming the task was deleted successfully.           

5. **List Tasks (Confirm the Task is Deleted)**
   - Action: Retrieve the list of tasks once more.
   - Expected Result: The response status code is 200 OK, and the list no longer includes the deleted task. Verify that the number of tasks has returned to the initial count.  

