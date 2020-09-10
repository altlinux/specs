%define modulename dkim
Name: python3-module-dkimpy
Version: 1.0.5
Release: alt1
Summary: Python 3 module for DKIM and ARC signing and verification
License: BSD-2-Clause
Url: https://code.launchpad.net/dkimpy
BuildArch: noarch
Group: Development/Python
Source0: %name-%version.tar
BuildRequires: python3-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-authres

%description
Python 3 module that implements DKIM (DomainKeys Identified Mail) email signing
and verification as well as ARC (Authenticated Received Chain) signing and
verification. Supports both RSA and Ed25519 signing and verification.
It also provides helper scripts for key generation and command line signing and
verification.


%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc ChangeLog README.md LICENSE
%_bindir/*
%_man1dir/*.1*
%python3_sitelibdir/%modulename
%python3_sitelibdir/dkimpy-*.egg-info

%changelog
* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Fri Jul 24 2020 Anton Farygin <rider@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Fri Feb 21 2020 Anton Farygin <rider@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Sep 05 2019 Anton Farygin <rider@altlinux.ru> 0.9.3-alt1
- first build for ALT

