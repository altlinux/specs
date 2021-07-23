%def_without check

%define modulename unpaddedbase64
Name: python3-module-unpaddedbase64
Version: 1.1.0
Release: alt2

Summary: Encode and decode Base64 without "=" padding

Url: https://github.com/matrix-org/python-unpaddedbase64
License: Apache-2.0
Group: Development/Python3


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/matrix-org/python-unpaddedbase64/archive/v%version.tar.gz
Source: %modulename-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
RFC 4648 specifies that Base64 should be padded to a multiple of 4 bytes
using "=" characters. However this conveys no benefit so many protocols
choose to use Base64 without the "=" padding.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt2
- Drop python2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1.qa1
- NMU: applied repocop patch

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Sisyphus

