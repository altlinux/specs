%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-dependency
%define mod_name pytest_dependency

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.1
Release: alt1

Summary: Manage dependencies of tests
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/pytest-dependency/
Vcs: https://github.com/RKrahl/pytest-dependency

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: 0001-Adapt-matching-of-expected-output-in-the-tests-to-ad.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3-module-setuptools-scm

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This pytest plugin manages dependencies of tests. It allows to mark
some tests as dependent from other tests. These tests will then be
skipped if any of the dependencies did fail or has been skipped.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.rst
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 13 2023 Anton Zhukharev <ancieg@altlinux.org> 0.5.1-alt1
- Built for ALT Sisyphus.

