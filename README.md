# Bank Branch API

A RESTful API service for accessing Indian bank and branch information, built with FastAPI and SQLAlchemy.

## Features

- Get bank details by ID
- Search branches by IFSC code, bank ID, branch name, city, or state
- Paginated results for all endpoints
- Efficient handling of large datasets (150,000+ branches)
- Deployable to Heroku or other cloud platforms

## Data Source

Bank branch data sourced from [Indian Banks GitHub repository](https://github.com/Amanskywalker/indian_banks) containing:

- 150,000+ bank branches
- Complete IFSC code information
- Bank names and branch details

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL (for production) or SQLite (for development)
- pip

