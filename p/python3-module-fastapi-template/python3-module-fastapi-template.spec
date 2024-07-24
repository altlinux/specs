%define _unpackaged_files_terminate_build 1
%define pypi_name fastapi_template
%define pypi_nname fastapi-template

%def_with check

Name: python3-module-%pypi_nname
Version: 5.1.0
Release: alt1.git8c5f2813

Summary: Flexible general-purpose template for FastAPI
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/fastapi_template/
Vcs: https://github.com/s3rius/FastAPI-template

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: instead_of_pytests.sh
Patch: fastapi-template-5.1.0-alt-fix_dependencies.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: git
BuildRequires: python3-module-poetry
%pyproject_builddeps_metadata
%endif

Requires: git
Requires: python3-module-poetry

# Manually manage extras dependencies with metadata.
AutoReq: yes, nopython3

%description
One of the coolest features is that this project is extremely configurable.
You can choose between different databases and even ORMs,
or you can even generate a project without a database!
Currently SQLAlchemy 2.0, TortoiseORM, Piccolo and Ormar are supported.

This project can run as TUI or CLI and has excellent code documentation.

Generator features:
- Pydantic V2 (Where it's possible. Some libs doesn't have support);
- You can choose between GraphQL and REST api;
- Uvicorn and gunicorn;
- Different databases support;
- Different ORMs support;
- Optional migrations for each ORM except raw drivers;
- Optional redis support;
- Optional rabbitmq support;
- different CI\CD;
- Optional Kubernetes config generation;
- Optional Demo routers and models
- (This helps you to see how project is structured);
- Pre-commit integration;
- Tests for the generator itself;
- Optional Prometheus integration;
- Optional Sentry integration;
- Optional Loguru logger;
- Optional Opentelemetry integration.
- Optional taskiq integration.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

export binfile="%buildroot%_bindir/%pypi_name"
export datadir="%buildroot%_datadir"
export PYTHONPATH=$PYTHONPATH:%buildroot%python3_sitelibdir_noarch
mkdir -p $datadir/zsh/site-functions
_FASTAPI_TEMPLATE_COMPLETE=zsh_source \
    $binfile > $datadir/zsh/site-functions/_%pypi_name
mkdir -p $datadir/bash-completion/completions
_FASTAPI_TEMPLATE_COMPLETE=bash_source \
    $binfile > $datadir/bash-completion/completions/%pypi_name
mkdir -p $datadir/fish/vendor_completions.d
_FASTAPI_TEMPLATE_COMPLETE=fish_source \
    $binfile > $datadir/fish/vendor_completions.d/%pypi_name.fish

%check
# Tests don't work without internet and docker-compose, so they are disabled.
# Instead, a bash script is used for testing.
%SOURCE2

%files
%doc README.* LICENSE
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%_datadir/zsh/site-functions/_%pypi_name
%_datadir/bash-completion/completions/%pypi_name
%_datadir/fish/vendor_completions.d/%pypi_name.fish

%changelog
* Tue Jul 23 2024 Denis Rastyogin <gerben@altlinux.org> 5.1.0-alt1.git8c5f2813
- Initial build for ALT Sisyphus.
