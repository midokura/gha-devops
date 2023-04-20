# GitHub Actions: midokura/gha-devops/oss-license-check-docker

[Index](../gha.md)

<!-- action-docs-description -->
## Description

Action to check the OSS License for all the docker layers

Example:
```
- name: OSS License Check | Docker
  uses: midokura/gha-devops/oss-license-check-docker@main
  with:
    dockerImage: "ghcr.io/midokura/evp-api:0.14.1-91d240c"
    runScancodeToolkit: true
```
<!-- action-docs-description -->

<!-- action-docs-inputs -->
## Inputs

| parameter | description | required | default |
| --- | --- | --- | --- |
| dockerImage | Docker image to scan | `true` |  |
| runScancodeToolkit | Run scancode-toolkit | `false` | false |
<!-- action-docs-inputs -->

<!-- action-docs-outputs -->

<!-- action-docs-outputs -->

<!-- action-docs-runs -->
## Runs

This action is a `composite` action.
<!-- action-docs-runs -->
