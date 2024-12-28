%define _unpackaged_files_terminate_build 1
%define pypi_name pymacaroons
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.13.0
Release: alt1
Summary: Macaroon library for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pymacaroons
Vcs: https://github.com/ecordell/pymacaroons
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter bumpversion
%add_pyproject_deps_check_filter yanc
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
PyMacaroons is a Python implementation of Macaroons. They're better than
cookies!

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# No module named 'hypothesis.specifiers'
%pyproject_run_pytest -ra --ignore=tests/property_tests/macaroon_property_tests.py

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jun 04 2024 Stanislav Levin <slev@altlinux.org> 0.13.0-alt1
- Initial build for Sisyphus.
