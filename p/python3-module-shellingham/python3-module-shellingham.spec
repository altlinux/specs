%def_disable snapshot
%define _unpackaged_files_terminate_build 1
%define pypi_name shellingham

%def_enable check

Name: python3-module-%pypi_name
Version: 1.5.1
Release: alt1

Summary: Shellingham detects what shell the current Python executable is running in
License: ISC
Group: Development/Python3
Url: https://github.com/sarugaku/shellingham

%if_disabled snapshot
Source: https://github.com/sarugaku/shellingham/archive/%version/%pypi_name-%version.tar.gz
%else
Vcs: https://github.com/sarugaku/shellingham.git
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)

%{?_enable_check:BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)}
#BuildRequires: /usr/bin/pipenv

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3
#%%tox_check

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%doc README* CHANGELOG*

%changelog
* Tue Feb 28 2023 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Mon Sep 12 2022 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- first build for Sisyphus



