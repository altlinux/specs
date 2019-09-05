%define modulename authres
Name: python3-module-%modulename
Version: 1.2.0
Release: alt1
Summary: RFC 7601 Authentication Results Header manipulation for Python3
License: ASL 2.0
Url: https://launchpad.net/authentication-results-python
BuildArch: noarch
Group: Development/Python
Source0: %name-%version.tar
BuildRequires: python3-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
Python3 module to create and parse RFC 7601 Authentication Results headers.

The module provides a class for creating and parsing RFC compliant headers for
use in Python3 applications. It supports all currently registered extensions in
addition to the core RFC 7601 types.

http://tools.ietf.org/rfc/rfc7601.txt

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc CHANGES README COPYING
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-*.egg-info

%changelog
* Thu Sep 05 2019 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- first build for ALT

