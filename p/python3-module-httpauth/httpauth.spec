%define _unpackaged_files_terminate_build 1
%define pypi_name httpauth

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.1
Release: alt1

Summary: WSGI middleware securing routes using HTTP Digest Authentication
License: ISC
Group: Development/Python3
Url: https://pypi.org/project/httpauth/
Vcs: https://github.com/jonashaag/httpauth

BuildArch: noarch
 
Source: %name-%version.tar

BuildRequires: python3-module-setuptools

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
%doc README.* LICENSE
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/__pycache__/*

%changelog
* Wed Sep 17 2025 Denis Rastyogin <gerben@altlinux.org> 0.4.1-alt1
- Initial build for ALT Sisyphus.
