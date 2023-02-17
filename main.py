import os
import markdown
import frontmatter
from slugify import slugify
from jinja2 import Environment, FileSystemLoader, select_autoescape
from jinja2.loaders import FileSystemLoader


home = [f for f in os.listdir("data/home") if os.path.isfile(os.path.join("data/home", f))]
about = [f for f in os.listdir("data/about") if os.path.isfile(os.path.join("data/about", f))]
articles = [f for f in os.listdir("data/articles") if os.path.isfile(os.path.join("data/articles", f))]
videos = [f for f in os.listdir("data/videos") if os.path.isfile(os.path.join("data/videos", f))]
error = [f for f in os.listdir("data/error") if os.path.isfile(os.path.join("data/videos", f))]


home_data = []
for homepage in home:
    with open(f"data/home/{homepage}", "r") as f:
        file_data = frontmatter.load(f)
        metadata = file_data.metadata
        metadata["slug"] = slugify(metadata["title"])
        metadata["type"] = "homepage"
        content = markdown.markdown(file_data.content)
        home_data.append({"metadata": metadata, "content": content})
print(home_data)

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
        metadata["type"] = "video"
        content = markdown.markdown(file_data.content)
        video_data.append({"metadata": metadata, "content": content})
print(video_data)


about_data = []
for aboutme in about:
    with open(f"data/about/{aboutme}", "r") as f:
        file_data = frontmatter.load(f)
        metadata = file_data.metadata
        metadata["slug"] = slugify(metadata["title"])
        metadata["type"] = "aboutme"
        content = markdown.markdown(file_data.content)
        about_data.append({"metadata": metadata, "content": content})
print(about_data)


error_data = []
for erro in error:
    with open(f"data/error/{erro}", "r") as f:
        file_data = frontmatter.load(f)
        metadata = file_data.metadata
        metadata["slug"] = slugify(metadata["title"])
        metadata["type"] = "erro"
        content = markdown.markdown(file_data.content)
        error_data.append({"metadata": metadata, "content": content})

env = Environment(loader=FileSystemLoader("./templates"))
template = env.get_template("home.html")

rendered_template = template.render()
os.makedirs("dist", exist_ok=True)
with open("dist/index.html", "w") as f:
    f.write(rendered_template)
