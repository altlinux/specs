
%define oname weakrefmethod

Name: python3-module-%oname
Version: 1.0.3
Release: alt2
Summary: WeakMethod class for storing bound methods using weak references.
Group: Development/Python3
License: PSF
Url: http://github.com/twang817/weakrefmethod
Source: %oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
This project is a backport of the WeakMethod class, and tests, for Python 2.6.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.3-alt2
- Transfer on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 06 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- Initial package.
