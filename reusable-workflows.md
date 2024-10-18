# Reusable Workflows

## Force renovate to inspect and upgrade relevant dependencies

### Usage

```yaml
jobs:
  renovate-reuse:
    uses: midokura/gha-devops/.github/workflows/update-helmchart-dependencies.yaml@main
    with:
      registry: "cratrrlsprdartifactsgl.azurecr.io"
      include-paths: "aitrios-core/values.yaml,values.yaml"
    secrets:
      registry-user: ${{ secrets.GDO_GAR_SCS_USERNAME }}
      registry-password: ${{ secrets.GDO_GAR_SCS_PASSWORD }}
      renovate-bot-pat: ${{ secrets.DEMO_RENOVATE_BOT_PAT }}
```

### Description

This workflow will trigger a renovatebot iteration that will automatically update the
images and chart versions of the paths in `include-paths`.

To follow a common convention to automate only the tags that are not in development,
it will only update tags that follow this regex: `^\d+\.\d+\.\d-main-\d+-[a-f0-9]{7,40}$`.
For example, `1.8.2-main-637-a7de93b1`, where the values are: `{aitrios_version}-main-{commit_number}-{sha}`.

#### Inputs

|Input|Description|Required|Secret|
|---|---|---|---|
|`registry`|Registry where the chart images and dependencies are stored. In the version, only one registry is supported|yes|no|   |
|`include-paths`|Comma-separated list of paths of the files it should try to update. The files shoud be either `values.yaml`s or `Chart.yaml`s.|yes|no|
|`registry-user`|Username to login into the `registry`|yes|yes|
|`registry-password`|Password to login into the `registry`|yes|yes|
|`renovate-bot-pat`|GitHub PAT renove bot will use to create the Pull Requests|yes|yes|
