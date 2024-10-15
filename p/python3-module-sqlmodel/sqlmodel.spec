%define _unpackaged_files_terminate_build 1
%define pypi_name sqlmodel
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.22
Release: alt1

Summary: SQL databases in Python, designed for simplicity, compatibility, and robustness
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/sqlmodel/
Vcs: https://github.com/fastapi/sqlmodel

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-module-black
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
SQLModel is a library for interacting with SQL databases from Python code,
with Python objects. It is designed to be intuitive, easy to use, highly
compatible, and robust.

SQLModel is based on Python type annotations, and powered by Pydantic and
SQLAlchemy.

The key features are:

* Intuitive to write: Great editor support. Completion everywhere. Less time
  debugging. Designed to be easy to use and learn. Less time reading docs.
* Easy to use: It has sensible defaults and does a lot of work underneath to
  simplify the code you write.
* Compatible: It is designed to be compatible with FastAPI, Pydantic, and
  SQLAlchemy.
* Extensible: You have all the power of SQLAlchemy and Pydantic underneath.
* Short: Minimize code duplication. A single type annotation does a lot of
  work. No need to duplicate models in SQLAlchemy and Pydantic.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-tests.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH="$PYTHONPATH:$(realpath ./)"
%pyproject_run_pytest -q -Wignore tests

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Oct 15 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.22-alt1
- Initial build for ALT Sisyphus.

