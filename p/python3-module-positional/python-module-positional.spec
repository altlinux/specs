%define oname positional

Name: python3-module-%oname
Version: 1.2.1
Release: alt2

Summary: Library to enforce positional or key-word arguments
License: Apache-2.0
Group: Development/Python3

Url: https://github.com/morganfainberg/positional
BuildArch: noarch

Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-wrapt

%description
`positional` provides a decorator which enforces only some args may be passed
positionally. The idea and some of the code was taken from the oauth2 client
of the google-api client.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Sat Aug 01 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt2
- Drop python2 support.

* Mon Dec 17 2018 Alexey Shabalin <shaba@altlinux.org> 1.2.1-alt1
- 1.2.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- 1.1.1
- add test packages

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- initial build
