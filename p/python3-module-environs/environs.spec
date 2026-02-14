%define _unpackaged_files_terminate_build 1
%define pypi_name environs
%def_with check

Name: python3-module-%pypi_name
Version: 14.5.0
Release: alt1

Summary: Simplified environment variable parsing
License: MIT
Group: Development/Python3
Url: https://github.com/sloria/environs
Vcs: https://github.com/sloria/environs.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: %name-%version-predownloaded.tar

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: pip
BuildRequires: python3-module-pytest
BuildRequires: /proc
%endif

%description
Environs is a Python library for parsing environment variables.
It provides type casting, default values, and validation.

%prep
%setup -a2
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
pip install --no-index -f packages packages/dj_database_url-3.1.0-py3-none-any.whl
pip install --no-index -f packages packages/dj_email_url-1.0.6-py2.py3-none-any.whl
pip install --no-index -f packages packages/django_cache_url-3.4.6-py2.py3-none-any.whl
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jan 16 2026 Grant Makyan <karonus@altlinux.org> 14.5.0-alt1
- First build for ALT.
