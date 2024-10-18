# gha-devops: Midokura DevOps GitHub Actions

Shared Midokura DevOps GitHub Actions.

## Documentation

You have an **GitHub Actions Index file with all the implemented GitHub Actions in [gha.md](./gha.md)**.

Each GitHub Action is definned in every folder of that repo.

Each folder contains, at least, 2 files:

- 'action.yaml' file: Implementation of the GitHub Action
- 'README.md" file: Automatically generated documentation for the GitHub Action
- Other files used in the 'action.yaml' file for the implementation

So, **if you have some doubt about one GitHub Action, please go to the [GitHub Actions Index file](./gha.md) and read the corresponding 'README.md' file**.


## Reusable Workflows

You can find the documentation for the reusable workflows in the [GitHub Workflows file](./reusable-workflows.md).

### Develop new GitHub Action

To develop a new GitHub Action and have propper documentation, please, don't forget to add a new README.md file in the new action folder, with the contents of the next template:

```md
# GitHub Actions: midokura/gha-devops/<FOLDER_OF_NEW_GITHUBACTION>

[Index](../gha.md)

<!-- action-docs-description -->

<!-- action-docs-inputs -->

<!-- action-docs-outputs -->

<!-- action-docs-runs -->
```

## Project tasks

Use the 'Makefile' to execute the project tasks:

```bash
$ make help
...
```

To update the documentation for a new release, you need to execute the 'gen-docs' Makefile task, and you need to have the 'yq' command installed:

```bash
$ sudo snap install yq
...
$ make gen-docs
...
> Generating docs:

- GitHub Action: add-k8singser-host
- GitHub Action: add-k8sns-dockerregistry-creds
- GitHub Action: setup-kind
- GitHub Action: test
- GitHub Action: test-nested
...
```
