# Home

<!-- ci/cd -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-runtime-overrides/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-runtime-overrides/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-runtime-overrides/deploy.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-runtime-overrides/actions/workflows/deploy.yml)
<!-- testing -->
[![CoverageTester](https://codecov.io/gh/Winipedia/pyrig-runtime-overrides/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-runtime-overrides)
[![ProjectTester](https://img.shields.io/badge/tested%20with-pytest-46a2f1.svg?logo=pytest)](https://pytest.org)
<!-- code-quality -->
[![DependencyAuditor](https://img.shields.io/badge/security-pip--audit-blue?logo=python)](https://github.com/pypa/pip-audit)
[![DependencyChecker](https://img.shields.io/badge/dependencies-deptry-blue)](https://github.com/osprey-oss/deptry)
[![MarkdownLinter](https://img.shields.io/badge/markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![SpellChecker](https://img.shields.io/badge/spell--check-typos-blue)](https://github.com/crate-ci/typos)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![VersionControlHookManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
<!-- tooling -->
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Pyrigger](https://img.shields.io/badge/built%20with-pyrig-3776AB?logo=buildkite&logoColor=black)](https://github.com/Winipedia/pyrig)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/pyrig-runtime-overrides?style=social)](https://github.com/Winipedia/pyrig-runtime-overrides)
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
<!-- project-info -->
[![DocsBuilder](https://img.shields.io/badge/MkDocs-Documentation-326CE5?logo=mkdocs&logoColor=white)](https://Winipedia.github.io/pyrig-runtime-overrides)
[![PackageIndex](https://img.shields.io/pypi/v/pyrig-runtime-overrides?logo=pypi&logoColor=white)](https://pypi.org/project/pyrig-runtime-overrides)
[![ProgrammingLanguage](https://img.shields.io/pypi/pyversions/pyrig-runtime-overrides)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-runtime-overrides)](https://github.com/Winipedia/pyrig-runtime-overrides/blob/main/LICENSE)

---

> A simple package that contains overrides for pyrig-runtime.

---

## Overview

pyrig-runtime-overrides carries the project overrides applied to
[pyrig-runtime](https://github.com/Winipedia/pyrig-runtime)'s own repository. It
is a maintenance package for pyrig-runtime itself — not a general-purpose
plugin — added as a development dependency to the pyrig-runtime project.

## Installation

```bash
uv add pyrig-runtime-overrides --dev
uv run pyrig sync
```

## How it works

The package overrides one pyrig class:

- **Dependencies** — removes `pyrig-runtime` from the dependencies the base
  configuration would otherwise add to `pyproject.toml`, avoiding a circular
  dependency, since pyrig-runtime cannot depend on itself.

## API Reference

For class- and method-level details, see the [API Reference](api.md), generated
automatically from the source.
