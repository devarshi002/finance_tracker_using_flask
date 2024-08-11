# Finance Tracker Using Flask

## Overview

The **Finance Tracker Using Flask** is a web application that helps users track their financial transactions. Built with Flask for the backend, HTML, CSS, and JavaScript for the frontend, this application allows users to add new transactions, view transaction history, and analyze their financial data through plots.

## Features

- **Add New Transactions**: Users can add details for new transactions including date, amount, category (Income or Expense), and an optional description.
- **View Transactions**: Users can view all transactions with a summary of their total income, expenses, and net savings. Users can also filter transactions by date range and view a plot of their financial data.
- **Responsive Design**: The application is designed to be fully responsive and works well on various devices.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: (Specify if using any database or if using file-based storage)
- **Plotting**: Matplotlib (for generating plots)

## Getting Started

To get started with this project, follow these steps:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/devarshi002/finance_tracker_using_flask.git
    cd finance_tracker_using_flask
    ```

2. **Create a Virtual Environment**:

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Application**:

    ```bash
    python app.py
    ```

    The application will start running on `http://127.0.0.1:5000/`.

## Project Structure

- `app.py`: Main Flask application file.
- `templates/`: Contains HTML files for the web pages.
  - `index.html`: Home page.
  - `add.html`: Page for adding new transactions.
  - `view.html`: Page for viewing transactions and plots.
- `static/`: Contains static files like CSS and JavaScript.
  - `styles.css`: Main stylesheet.
  - `styles2.css`: Additional stylesheet for specific pages.
- `requirements.txt`: List of Python dependencies.
- `README.md`: This file.

## CSS Styling

- `styles.css`: General styling for the application including table styles, button styles, and responsive design.
- `styles2.css`: Specific styling for the "Add New Transaction" page.

## Known Issues

- Ensure all form inputs are correctly formatted to avoid errors.
- Matplotlib plots may require additional configuration for display.

## Future Enhancements

- Implement user authentication.
- Add more detailed financial reports and analytics.
- Integrate with an external database for persistent storage.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or bug fixes. Please ensure that you follow the project's coding guidelines and write appropriate tests for any new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Screenshots
![plot](https://github.com/user-attachments/assets/eb0d974d-b7ce-4212-a703-35b7eea0ba1a)
![exp-home](https://github.com/user-attachments/assets/8a0b9ce1-65d5-41db-a844-d8dafd79ce60)
![exp-add](https://github.com/user-attachments/assets/25f48b9b-de46-417e-a221-26413187a4a3)
![exp-view](https://github.com/user-attachments/assets/175a3507-9908-442f-b553-6659921bd326)
![exp-transaction](https://github.com/user-attachments/assets/e6736d2a-4f8d-4ca9-a8e7-468c26972eca)

