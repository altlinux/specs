%define oname daiquiri

Summary: Library to configure Python logging easily
Name: python3-module-%oname
Version: 0.1.0
Release: alt2
Url: https://github.com/jd/daiquiri
Source: %oname-%version.tar.gz
License: Apache
Group: Development/Python3

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr
BuildRequires: python3-module-six

%description
The daiquiri library provides an easy way to configure logging.
It also provides some custom formatters and handlers.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

%build
export LANG=en_US.UTF-8
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
* Wed Jun 09 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.0-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- initial build
