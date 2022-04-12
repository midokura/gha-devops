# gha-devops: Midokura DevOps GitHub Actions

Shared Midokura DevOps GitHub Actions.

## Documentation

Each GitHub Action is definned in every folder of that repo.

Each folder contains, at least, 2 files:

- 'action.yaml' file: Implementation of the GitHub Action
- 'README.md" file: Automatically generated documentation for the GitHub Action
- Other files used in the 'action.yaml' file for the implementation

So, **if you have some doubt about one GitHub Action, please read the corresponding 'README.md' file**.

## Project tasks

Use the 'Makefile' to execute the project tasks:

```bash
$ make help
...
```

To update the documentation for a new release, you need to execute the 'gen-docs' Makefile task:

```bash
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
