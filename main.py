import os
import markdown
import frontmatter
from slugify import slugify
from jinja2 import Template

home = [f for f in os.listdir("data/home") if os.path.isfile(os.path.join("data/home", f))]
about = [f for f in os.listdir("data/about") if os.path.isfile(os.path.join("data/about", f))]
articles = [f for f in os.listdir("data/articles") if os.path.isfile(os.path.join("data/articles", f))]
videos = [f for f in os.listdir("data/videos") if os.path.isfile(os.path.join("data/videos", f))]
error = [f for f in os.listdir("data/videos") if os.path.isfile(os.path.join("data/videos", f))]

article_data = []
for article in articles:
    with open(f"data/articles/{article}", "r") as f:
        file_data = frontmatter.load(f)
        metadata = file_data.metadata
        metadata["slug"] = slugify(metadata["title"])
        metadata["type"] = "article"
        content = markdown.markdown(file_data.content)
        article_data.append({"metadata": metadata, "content": content})
print(article_data)

video_data = []
for video in videos:
    with open(f"data/videos/{video}", "r") as f:
        file_data = frontmatter.load(f)
        metadata = file_data.metadata
        metadata["slug"] = slugify(metadata["title"])
        metadata["type"] = "article"
        content = markdown.markdown(file_data.content)
        article_data.append({"metadata": metadata, "content": content})
print(article_data)
