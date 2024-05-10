# WordPress-MD-Astro

WordPress-MD-Astro is a Python script for exporting WordPress blog posts to Markdown files, suitable for use in static site generators like Astro. This script retrieves posts from a WordPress database, converts them to Markdown format, and enriches them with YAML front matter for metadata.

## Features

- Fetches published blog posts directly from a WordPress database.
- Converts HTML content of posts to Markdown format.
- Adds YAML front matter to the Markdown files for better integration with static site generators.
- Automatically generates slugs for file names based on post titles.

## Prerequisites

- Python 3.6 or higher
- `markdownify` Python package
- `mysql-connector-python` package for MySQL database connection

## Setup

### Install Required Packages

Before running the script, make sure to install the required Python packages:

```bash
pip install markdownify mysql-connector-python
```

### Database Configuration

Edit the script to include your MySQL database connection settings:

```python
cnx = mysql.connector.connect(
    user='your_username',
    password='your_password',
    host='your_host',
    database='your_database'
)
```

## Usage

1. Ensure that your MySQL server is running and that you have the correct privileges to access the database.
2. Run the script from the command line:

```bash
python convert.py
```

The script will:
- Connect to your WordPress database.
- Retrieve and process posts.
- Save the Markdown files in a specified directory.

## Output

The Markdown files are saved in the `markdown_files` directory. Each file is named using a slug derived from the blog post title and includes a YAML block at the top with metadata such as the title, publication date, author, and a placeholder for an image.

## Customization

You can customize the script by modifying the SQL query to fetch different types of posts or additional data, adjusting the Markdown conversion settings, or by altering the structure of the YAML front matter.

## Contributing

Contributions to enhance WordPress-MD-Astro are welcome. Please feel free to fork the repository, make improvements, and submit pull requests.

## License

MIT