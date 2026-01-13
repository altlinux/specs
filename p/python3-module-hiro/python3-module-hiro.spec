%define _unpackaged_files_terminate_build 1
%define pypi_name hiro
%define mod_name hiro

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.1
Release: alt1
Summary: Hiro - time manipulation utilities for testing in python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hiro/
Vcs: https://github.com/alisaifee/hiro
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest-cov
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst LICENSE doc/
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jan 13 2026 Alexey Rodygin <alehandro@altlinux.org> 1.1.1-alt1
- Initial build for ALT Linux
