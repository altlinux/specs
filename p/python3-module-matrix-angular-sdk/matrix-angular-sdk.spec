%def_without check

%define modulename matrix-angular-sdk
Name: python3-module-matrix-angular-sdk
Version: 0.6.8
Release: alt2

Summary: Matrix Angular Sdk

Url: https://pypi.python.org/pypi/matrix-angular-sdk
License: Apache-2.0
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/m/%modulename/%modulename-%version.tar.gz
Source: %modulename-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
This project provides AngularJS services for implementing the Client-Server API on Matrix:
an open standard for interoperable Instant Messaging and VoIP.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 0.6.8-alt2
- Drop python2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.8-alt1.qa1
- NMU: applied repocop patch

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.8-alt1
- initial build for ALT Sisyphus

