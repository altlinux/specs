%define _unpackaged_files_terminate_build 1
%define pypi_name sansldap

%def_with check
## TODO: fix docs
%def_without docs

Name:    python3-module-%pypi_name
Version: 0.1.0
Release: alt1

Summary: Python Sans I/O LDAP Library
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/sansldap/
VCS:     https://github.com/jborean93/sansldap

BuildArch: noarch

Source: %pypi_name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra testing
%pyproject_builddeps_metadata_extra linkify

BuildRequires: python3(pytest-cov)
%endif

%if_with docs
BuildRequires: python3(sphinx)
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3(sphinx_autodoc_typehints)
BuildRequires: python3-module-sphinxcontrib-apidoc
BuildRequires: python3(myst_parser)
BuildRequires: python3(sphinx_rtd_theme)
%endif

%description
Library for LDAP in Python. It does not provide any IO or concurrency logic
as it's designed to be a pure Python implementation that is then used by
other libraries. This follows the sans-IO paradigm to promote re-usability
and have it focus purely on the protocol logic.

%prep
%setup -n %pypi_name-%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build
%if_with docs
pushd docs
make html-strict
ls -la 
tree ./
popd
%endif

%install
%pyproject_install

%check
%tox_check_pyproject
%pyproject_run_pytest -ra tests

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Jul 08 2023 Andrey Limachko <liannnix@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
