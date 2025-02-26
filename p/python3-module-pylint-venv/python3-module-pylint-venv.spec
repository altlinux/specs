%define _unpackaged_files_terminate_build 1
%define pypi_name pylint-venv
%define mod_name pylint_venv

%def_with check

Name: python3-module-%pypi_name
Version: 3.0.4
Release: alt1

Summary: Make pylint respect virtualenvs
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pylint-venv/
Vcs: https://github.com/jgosmann/pylint-venv

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
BuildRequires: python3-module-pylint
%endif

%description
Pylint does not respect the currently activated virtualenv if it
is not installed in every virtual environment individually.
This module provides a Pylint init-hook to use the same Pylint
installation with different virtual environments.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- test/test.sh

%files
%doc LICENSE.txt CHANGES.md README.rst
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Feb 26 2025 Anton Zhukharev <ancieg@altlinux.org> 3.0.4-alt1
- Updated to 3.0.4.

* Wed Nov 08 2023 Anton Zhukharev <ancieg@altlinux.org> 3.0.3-alt1
- Built for ALT Sisyphus.

