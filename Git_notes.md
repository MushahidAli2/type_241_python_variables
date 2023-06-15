# Git Introduction

## What is Git?

Git is a distributed version control system (VCS) widely used in software development. It allows multiple people to collaborate on a project simultaneously, keeping track of changes, and managing different versions of files efficiently.

## Version Control Systems (VCS)

Before Git, traditional version control systems relied on centralized models. Developers would check out files from a central repository, make changes locally, and then check them back in. This approach had limitations, such as single points of failure and difficulties collaborating on multiple branches simultaneously.
![Alt Text](https://archaeogeek.github.io/foss4gukdontbeafraid/images/newschool_vcs.png)
## How Git revolutionized version control

Git introduced a distributed approach to version control, addressing the limitations of centralized systems. With Git, each developer has their own complete copy of the project's entire history, including all files and branches. This allows for seamless branching, merging, and easy collaboration with others.
![Alt Text](https://archaeogeek.github.io/foss4gukdontbeafraid/images/oldschool_vcs.png)
## Git Commands

### `git init`

The `git init` command initializes a new Git repository in the current directory. It creates a hidden `.git` folder to store all the necessary metadata and configuration files for version control.

### `git status`

The `git status` command shows the current state of the repository. It displays information about any modified, staged, or untracked files, as well as the current branch.

### `git add .`

The `git add .` command stages all modified and untracked files in the current directory and its subdirectories. Staging prepares the changes to be included in the next commit.

### `git commit -m "<commit message>"`

The `git commit` command saves the staged changes as a new commit in the repository's history. The `-m` flag allows you to provide a commit message describing the changes made. A good commit message is concise and descriptive, summarizing the purpose or intent of the commit.

## Conclusion

Git has revolutionized version control by providing a distributed and powerful system for managing changes in software development projects. Understanding Git basics and using commands like `git init`, `git status`, `git add .`, and `git commit -m ""` are essential for effective collaboration and version control.

By leveraging Git, developers can work together seamlessly, track changes, easily switch between branches, and maintain a complete and reliable history of their projects.

Remember to consult the Git documentation and explore more advanced commands and concepts as you continue your journey with Git.

