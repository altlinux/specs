Name: conan
Summary: A distributed, open source, package manager
Version: 0.29.1
Release: alt0.1

Group: System/Libraries
License: MIT
Url: https://github.com/conan-io/conan

# Source-url: https://github.com/conan-io/conan/archive/%version.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-alt.patch


Packager: Pavel Vainerman <pv@altlinux.org>

BuildArch: noarch

# python3-dev
BuildRequires: python-module-setuptools python-module-yaml python-module-phatch 

%py_requires yaml

# Skip findreq on all modules:
%add_findreq_skiplist %python_sitelibdir/%name/conans/test/*
%add_findreq_skiplist %python_sitelibdir/%name/conans/test_integration/*

%description
A distributed, open source, package manager.

%prep
%setup
%patch0 -p0

%build
%python_build

%install
%python_install

%files
%_bindir/%{name}*
%python_sitelibdir/%{name}*
%doc README.rst LICENSE.md
%exclude %python_sitelibdir/conans/test/*
%exclude %python_sitelibdir/conans/test_integration/*

%changelog
* Fri Dec 01 2017 Pavel Vainerman <pv@altlinux.ru> 0.29.1-alt0.1
- initial build version (0.29.1) with rpmgs script

