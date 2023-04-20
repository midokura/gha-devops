# SPDX-License-Identifier: Apache-2.0
# Copyright 2023, David Giron <@duhow>, Midokura
# Usage: Given syft SPDX-json output, add LICENSES missing

import requests
import urllib.parse
import json
import sys

SBOM_FILE = "sbom.json"
if len(sys.argv) > 1:
    SBOM_FILE = sys.argv[1]

with open(SBOM_FILE) as file:
    sbom_doc = json.load(file)

def get_maven(pkg_url: str): 
    pkg_url = pkg_url.replace("pkg:maven/", "")
    # required by deps.dev for pkg/func
    pkg_url = pkg_url.replace("/", ":")

    if not "@" in pkg_url:
        # not implemented
        return False

    PACKAGE_VERSION = pkg_url.split("@")[1] or "latest"
    pkg_url = pkg_url.split("@")[0]

    PACKAGE_TYPE = "maven"
    PACKAGE_NAME = urllib.parse.quote(pkg_url)

    url = f"https://api.deps.dev/v3alpha/systems/{PACKAGE_TYPE}/packages/{PACKAGE_NAME}/versions/{PACKAGE_VERSION}"
    req = requests.get(url)

    #print(url)
    #print(req.status_code)

    if req.status_code == 200:
        print(req.json())
        return req.json()
    return False

for package in sbom_doc["packages"]:
    if package["licenseDeclared"] != "NONE":
        continue
    for ref in package.get("externalRefs"):
        if ref["referenceCategory"] != "PACKAGE-MANAGER":
            continue
        url = ref["referenceLocator"]
        package_data = None
        if url.startswith("pkg:maven/"):
            package_data = get_maven(url)
        if package_data:
            package["licenseDeclared"] = package_data["licenses"]
            package["licenseConcluded"] = package_data["licenses"]

with open(SBOM_FILE, "w") as file:
    file.write(json.dumps(sbom_doc, indent=2))
