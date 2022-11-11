%def_disable snapshot
%define _unpackaged_files_terminate_build 1
%define pypi_name crashtest

%def_enable check

Name: python3-module-%pypi_name
Version: 0.4.1
Release: alt1

Summary: Crashtest is a Python library that makes exceptions handling and inspection easier.
License: MIT
Group: Development/Python3
Url: https://github.com/sdispater/crashtest

%if_disabled snapshot
Source: https://github.com/sdispater/crashtest/archive/%version/%pypi_name-%version.tar.gz
%else
Vcs: https://github.com/sdispater/crashtest.git
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(poetry-core)

%{?_enable_check:BuildRequires: python3(pytest)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)}

%description
Crashtest is a Python library that makes exceptions handling and inspection easier.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%doc README.md

%changelog
* Sat Nov 12 2022 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Mon Sep 12 2022 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- first build for Sisyphus



