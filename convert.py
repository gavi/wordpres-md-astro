import mysql.connector
import markdownify
import os
import re


def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    value = re.sub(r'[\s_-]+', '-', value)
    if value[0].isdigit():
        value = f'post-{value}'
    return value


# Connect to your WordPress database
cnx = mysql.connector.connect(
    user='your_username',
    password='your_password',
    host='your_host',
    database='your_database'
)

# Create a cursor to execute queries
cursor = cnx.cursor()

# Updated query to retrieve blog entries with author names
query = """
SELECT p.post_title, p.post_content, p.post_name, p.post_date, u.display_name 
FROM wp_posts p 
JOIN wp_users u ON p.post_author = u.ID
WHERE p.post_type = 'post' AND p.post_status = 'publish'
"""

# Execute the query
cursor.execute(query)

# Fetch all the rows
rows = cursor.fetchall()

# Close the cursor and connection
cursor.close()
cnx.close()

# Create a directory to store the Markdown files
markdown_dir = 'markdown_files'
if not os.path.exists(markdown_dir):
    os.makedirs(markdown_dir)

# Loop through each blog entry
for title, content, slug, date, author in rows:
    # Convert HTML content to Markdown using markdownify
    md_content = markdownify.markdownify(content, heading_style='ATX')

    # Create a YAML front matter block with dynamic values
    yaml_block = f'''---
title: '{title}'
description: '{title}'
pubDate: '{date.strftime('%b %d %Y')}'
heroImage: '/img/blog/og_logo.png'
author: '{author}'
---
'''

    # Write the Markdown content to a file
    # Generate a slug from the title for the filename
    file_slug = slugify(title)
    with open(f'{markdown_dir}/{file_slug}.md', 'w') as f:
        # Title right after YAML block
        f.write(yaml_block + f'\n\n# {title}\n\n' + md_content)
