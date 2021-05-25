%def_without check

%define modulename pymacaroons-pynacl
Name: python3-module-pymacaroons-pynacl
Version: 0.13.0
Release: alt2

Summary: Library providing non-opaque cookies for authorization

Url: https://github.com/ecordell/pymacaroons
License: MIT
Group: Development/Python3
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/ecordell/pymacaroons/archive/v%version.tar.gz
Source: %modulename-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
This is a Python re-implementation of the libmacaroons C library.
Macaroons, like cookies, are a form of bearer credential. Unlike
opaque tokens, macaroons embed caveats that define specific authorization
requirements for the target service, the service that issued the root macaroon
and which is capable of verifying the integrity of macaroons it receives.

Macaroons allow for delegation and attenuation of authorization. They are
simple and fast to verify, and decouple authorization policy from the
enforcement of that policy.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 0.13.0-alt2
- Drop python2 support.

* Wed Feb 06 2019 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1.qa1
- NMU: applied repocop patch

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- initial build for ALT Sisyphus

