# Bank Branch API

A RESTful API service for accessing Indian bank and branch information, built with FastAPI and SQLAlchemy.

## Features

- Get bank details by ID
- Search branches by IFSC code, bank ID, branch name, city, or state
- Paginated results for all endpoints
- Efficient handling of large datasets (150,000+ branches)
- Deployable to Heroku or other cloud platforms


## Solution Architecture

### Technical Stack
- **Framework**: FastAPI (Python 3.8+)
- **Database**: PostgreSQL (Production), SQLite (Development)
- **ORM**: SQLAlchemy 1.4
- **Data Handling**: Bulk loading with batch processing
- **Deployment**: Heroku with Heroku Postgres

## Problem-Solving Approach

### 1. Large Dataset Handling
**Challenge**: Efficiently process 150,000+ branch records  
**Solution**:
```python
# Batch processing implementation
def load_large_dataset(file_path, batch_size=10000):
    with open(file_path) as f:
        reader = csv.DictReader(f)
        batch = []
        for i, row in enumerate(reader):
            batch.append(process_row(row))
            if i % batch_size == 0:
                db.bulk_save_objects(batch)
                batch = []
