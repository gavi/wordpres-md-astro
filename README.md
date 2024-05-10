# WordPress-MD-Astro

WordPress-MD-Astro is a Python project designed to export WordPress blog posts to Markdown files, suitable for use in static site generators like Astro. This project includes scripts to retrieve posts from a WordPress database, convert them to Markdown format, enrich them with YAML front matter for metadata, and ensure hero images are updated correctly.

## Features

- Fetches published blog posts directly from a WordPress database.
- Converts HTML content of posts to Markdown format.
- Adds YAML front matter to the Markdown files for better integration with static site generators.
- Automatically generates slugs for file names based on post titles.
- Updates the `heroImage` in the YAML front matter with the first image found in the post.

## Prerequisites

- Python 3.6 or higher
- `markdownify` and `requests` Python packages
- `mysql-connector-python` package for MySQL database connection

## Setup

### Install Required Packages

Before running the scripts, make sure to install the required Python packages:

```bash
pip install markdownify mysql-connector-python requests
```

### Database Configuration

Edit the scripts to include your MySQL database connection settings:

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
2. Run the main script from the command line to convert WordPress posts to Markdown:

```bash
python convert.py
```

3. After generating the Markdown files, run the `clean.py` script to update the hero images:

```bash
python clean.py
```

The scripts will:
- Connect to your WordPress database and retrieve posts.
- Save the converted Markdown files in a specified directory.
- Update the `heroImage` in the Markdown files using the first image URL found in the content.

## Output

The Markdown files are saved in the `markdown_files` directory. Each file is named using a slug derived from the blog post title and includes a YAML block at the top with metadata such as the title, publication date, author, and an updated hero image URL.

## Customization

You can customize the scripts by modifying the SQL query to fetch different types of posts or additional data, adjusting the Markdown conversion settings, or by altering the structure of the YAML front matter and image update logic.

## Contributing

Contributions to enhance WordPress-MD-Astro are welcome. Please feel free to fork the repository, make improvements, and submit pull requests.

## License

MIT