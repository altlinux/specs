%define _unpackaged_files_terminate_build 1
%define pypi_name cvss
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 3.2
Release: alt1

Summary: CVSS2/3/4 library with interactive calculator for Python 3
License: LGPL-3.0
Group: Development/Python3
Url: https://pypi.org/project/cvss/
Vcs: https://github.com/RedHatProductSecurity/cvss

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This Python package contains CVSS v2, v3 and v4 computation utilities and
interactive calculator.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python3 tests/test_cvss2.py
%pyproject_run -- python3 tests/test_cvss3.py
%pyproject_run -- python3 tests/test_cvss4.py

%files
%doc COPYRIGHT LICENSE README.rst
%_bindir/cvss_calculator
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 29 2024 Anton Zhukharev <ancieg@altlinux.org> 3.2-alt1
- Built for ALT Sisyphus.

