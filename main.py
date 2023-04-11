import os

import pyperclip
import yaml
from pick import pick


# ─── Algorithm ────────────────────────────────────────────────────────────────


def main():
    # Language Selection
    os.system('cls' if os.name == 'nt' else 'clear')
    title = 'Select your commit language'
    options = [template[:-5] for template in os.listdir('templates')]
    option, _ = pick(options, title, indicator='>> ')

    # Commit Type
    with open(f'templates/{option}.yaml', 'r', encoding='utf-8') as f:
        templates = yaml.safe_load(f)
    title = 'Select a commit type'
    options = list(templates.keys())
    option, _ = pick(options, title, indicator='>> ')

    # Description
    os.system('cls' if os.name == 'nt' else 'clear')
    description = input(
        f'Enter a short description (if needed) of your {templates[option]["id"]} commit.\n[Description]: '
    )
    commit_title = f'{templates[option]["title"]}: {description}' if description != '' else templates[
        option]["title"]
    pyperclip.copy(commit_title)
    print('\n Commit title copied to clipboard.')


if __name__ == '__main__':
    main()