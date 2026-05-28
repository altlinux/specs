%define modname ldap_filter

%def_with check

Name: python3-module-%modname
Version: 1.0.1
Release: alt1

Summary: A Python 3 utility library for working with LDAP
License: MIT
Group:   Development/Python3
URL: https://github.com/SteveEwell/python-ldap-filter.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
A Python 3 utility library for working with Lightweight Directory
Access Protocol (LDAP) filters.
This project is a Python port of the node-ldap-filters project. 
The filters produced by the library are based on RFC 4515.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/%modname/
%python3_sitelibdir/%{pyproject_distinfo %modname}

%changelog
* Wed May 06 2026 Nikita Panov <nexxy@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.


