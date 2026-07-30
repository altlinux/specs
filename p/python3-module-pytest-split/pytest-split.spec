%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-split
%define mod_name pytest_split

%def_with check

Name: python3-module-%pypi_name
Version: 0.11.0
Release: alt1

Summary: Pytest plugin which splits the test suite to equally sized sub suites based on test execution time
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/pytest-split
VCS: https://github.com/jerry-git/pytest-split

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=''

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%_bindir/slowest-tests

%changelog
* Wed Mar 04 2026 Aleksandr A. Voyt <sobue@altlinux.org> 0.11.0-alt1
- Initial build.
