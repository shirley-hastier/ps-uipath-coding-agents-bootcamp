"""
MkDocs-macros module: injects the training-environment values into pages.

Why this exists
----------------
The training environment differs between authoring and release:
  - staging  -> used while authoring, so live cohorts are never disrupted
  - prod     -> the real participant environment

Pages reference the variables instead of hardcoding URLs/tenants, e.g.:

    !!! tip "Training Environment"
        Log in at **[{{ training_url }}]({{ training_url }})** using tenant **{{ training_tenant }}**.

Switch environments at build time with the BOOTCAMP_ENV variable:
    BOOTCAMP_ENV=staging mkdocs serve     # author/preview
    BOOTCAMP_ENV=prod    mkdocs build     # release (CI uses this)

Default is "prod" so a plain build is release-safe.
"""

import os

ENVIRONMENTS = {
    "staging": {
        "training_url": "https://staging.uipath.com/partnersuccess",
        "training_tenant": "Workshops",
        "env_label": "Staging (build & preview)",
    },
    "prod": {
        "training_url": "https://staging.uipath.com/uspsenablement/portal_/home",
        "training_tenant": "USTechnicalServices",
        "env_label": "USPS Enablement (staging)",
    },
}


def define_env(env):
    profile = os.getenv("BOOTCAMP_ENV", "prod").lower()
    cfg = ENVIRONMENTS.get(profile, ENVIRONMENTS["prod"])
    for key, value in cfg.items():
        env.variables[key] = value
    env.variables["bootcamp_env"] = profile
