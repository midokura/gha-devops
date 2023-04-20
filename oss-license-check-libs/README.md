# GitHub Actions: midokura/gha-devops/oss-license-check-libs

[Index](../gha.md)

<!-- action-docs-description -->
## Description

Action to check the OSS License for the source code and libs
Example:
```
- name: OSS License Check | Libs
  uses: midokura/gha-devops/oss-license-check-libs@main
  with:
    githubToken: <secrets.TOKEN_PACKAGES>
    repository: midokura/evp-device-agent
    branch: main
    fossologyEndpoint: https://fossology.bcn-penguin.midocloud.net/repo
    fossologyToken: <secrets.FOSSOLOGY_TOKEN>
    fossologyFolderId: "4"
```
<!-- action-docs-description -->

<!-- action-docs-inputs -->
## Inputs

| parameter | description | required | default |
| --- | --- | --- | --- |
| githubToken | GitHub repo access token | `true` |  |
| repository | GitHub repository in ORG/NAME format (midokura/...) | `true` |  |
| branch | Branch name (default if not provided) | `false` |  |
| fossologyEndpoint | Fossology endpoint | `true` |  |
| fossologyToken | Fossology access token | `true` |  |
| fossologyFolderId | Fossology folder ID | `true` |  |
<!-- action-docs-inputs -->

<!-- action-docs-outputs -->

<!-- action-docs-outputs -->

<!-- action-docs-runs -->
## Runs

This action is a `composite` action.
<!-- action-docs-runs -->
