# GitHub Actions: midokura/gha-devops/selfsigned-new-cert

[Index](../gha.md)

<!-- action-docs-description -->
## Description

Action for creating a new certificate signed by a previously created CA

Example:
```
- name: Self signed CA init
  uses: midokura/gha-devops/selfsigned-ca-init@main
    with:
      namespace: 'my-namespace'
- name: Self signed new cert
  uses: midokura/gha-devops/selfsigned-new-cert@main
    with:
      namespace: 'my-namespace'
      cert_name: 'my-cert'

```
<!-- action-docs-description -->

<!-- action-docs-inputs -->
## Inputs

| parameter | description | required | default |
| --- | --- | --- | --- |
| cert_name | Common name for the new certificate | `true` |  |
| cert_dir | Directory to export recently created certificate | `true` |  |
| namespace | Namespace where certificates will be created | `true` |  |
| dns_name | DNS name to be added to the certificate | `false` | my-cert.example.com |
<!-- action-docs-inputs -->

<!-- action-docs-outputs -->

<!-- action-docs-outputs -->

<!-- action-docs-runs -->
## Runs

This action is a `composite` action.
<!-- action-docs-runs -->
