# GitHub Actions: midokura/gha-devops/selfsigned-ca-init

[Index](../gha.md)

<!-- action-docs-description -->
## Description

Action for setting up a self signed CA authority. Requires Kubernetes running

Example:
```
- name: Self signed CA init
  uses: midokura/gha-devops/selfsigned-ca-init@main
    with:
      namespace: 'my-namespace'

```
<!-- action-docs-description -->

<!-- action-docs-inputs -->
## Inputs

| parameter | description | required | default |
| --- | --- | --- | --- |
| cert_dir | DockerHub registry username | `false` |  |
| namespace | Namespace where certificates will be created | `true` |  |
<!-- action-docs-inputs -->

<!-- action-docs-outputs -->

<!-- action-docs-outputs -->

<!-- action-docs-runs -->
## Runs

This action is a `composite` action.
<!-- action-docs-runs -->
