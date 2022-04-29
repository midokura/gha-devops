# GitHub Actions: midokura/gha-devops/setup-kind

[Index](../gha.md)

<!-- action-docs-description -->
## Description

Action for setting up a kind k8s cluster

Example:
```
- name: Setup kind
  uses: midokura/gha-devops/setup-kind@main
  with:
    dockerHubUsername: <SECRET_DOCKERHUB_USERNAME>
    dockerHubPassword: <SECRET_DOCKERHUB_PASSWORD>
    dockerLocalImages: "test/docker-image:local bitnami/postgresql:latest"
```



<!-- action-docs-description -->

<!-- action-docs-inputs -->
## Inputs

| parameter | description | required | default |
| - | - | - | - |
| dockerHubUsername | DockerHub registry username | `true` |  |
| dockerHubPassword | DockerHub registry password | `true` |  |
| dockerLocalImages | Docker local images to push in kind | `false` |  |



<!-- action-docs-inputs -->

<!-- action-docs-outputs -->

<!-- action-docs-outputs -->

<!-- action-docs-runs -->
## Runs

This action is an `composite` action.


<!-- action-docs-runs -->