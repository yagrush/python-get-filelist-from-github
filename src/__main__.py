import requests
import yaml
from github import Github
import os

CONFIG_PATH = "config.yaml"


def download_content_from_github_and_save(
    github_content_download_url: str, save_path: str, github_token: str
) -> bool:
    try:
        headers = {"Authorization": f"token {github_token}"}
        response = requests.get(
            github_content_download_url, headers=headers, timeout=30
        )
        response.raise_for_status()
        with open(save_path, "wb") as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"Error downloading file: {e}")
        return False


with open(CONFIG_PATH, "r", encoding="UTF-8") as yml:
    config = yaml.safe_load(yml)

    github_token = config["github_token"]
    g = Github(github_token)

    config_repo = config["target_github_repository"]
    repo_name = f'{config_repo["author"]}/{config_repo["name"]}'
    repo = g.get_repo(repo_name)

    directory_path = config_repo["target_dir_path"]

    save_dir_path = f"./{directory_path}"
    os.makedirs(save_dir_path, exist_ok=True)

    contents = repo.get_contents(directory_path)

    for content_file in contents:
        if content_file.type == "file":
            download_content_from_github_and_save(
                github_content_download_url=content_file.download_url,
                save_path=f"./{content_file.path}",
                github_token=github_token,
            )
