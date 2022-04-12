# GitHub Actions: midokura/gha/add-k8sns-dockerregistry-creds

<!-- action-docs-description -->
## Description

Action to add to a k8s Namespace docker registry creds as a secret

Example:
```
- name: Add docker registry creds to kind namespace
  uses: midokura/gha-devops/add-k8sns-dockerregistry-creds@main
  with:
    k8sNS: tb
    secretName: dockerregistry-creds    
```



<!-- action-docs-description -->

<!-- action-docs-inputs -->
## Inputs

| parameter | description | required | default |
| - | - | - | - |
| k8sNS | Kubernetes Namespace | `true` |  |
| secretName | Name for the new secret | `true` |  |



<!-- action-docs-inputs -->

<!-- action-docs-outputs -->

<!-- action-docs-outputs -->

<!-- action-docs-runs -->
## Runs

This action is an `composite` action.


<!-- action-docs-runs -->