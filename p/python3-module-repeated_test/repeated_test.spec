%define oname repeated_test

Name: python3-module-%oname
Version: 1.0.1
Release: alt2

Summary: A quick unittest-compatible framework for repeating a test function over many fixtures

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/repeated_test/

# Source-url: https://pypi.io/packages/source/r/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

%py3_provides %oname

BuildRequires(pre): rpm-build-python3 rpm-build-intro

%description
A quick unittest-compatible framework for repeating a test function over many fixtures.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%python3_check

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt2
- Drop python2 support.

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Sisyphus

