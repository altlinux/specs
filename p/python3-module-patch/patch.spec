%def_without check

%define modulename patch
Name: python3-module-patch
Version: 1.16
Release: alt3

Summary: Library to parse and apply unified diffs

Url: https://pypi.python.org/pypi/patch/
License: Python Software Foundation License
Group: Development/Python3


Packager: Vitaly Lipatov <lav@altlinux.ru>

# NOSource-url: https://pypi.io/packages/source/p/%modulename/%modulename-%version.tar.gz
# Source-url: https://github.com/techtonik/python-patch/archive/%version.tar.gz
Source: %modulename-%version.tar

BuildRequires(pre): rpm-build-python3

%description
Library to parse and apply unified diffs.

%prep
%setup -n %modulename-%version

%build

%install
install -D -m755 patch.py %buildroot%python3_sitelibdir/patch.py
sed -i "s|^#!/usr/bin/env python$|#!/usr/bin/python3|g" %buildroot%python3_sitelibdir/patch.py

%files
%doc README.md doc/
%python3_sitelibdir/*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.16-alt3
- Drop python2 support.

* Sun Feb 09 2020 Vitaly Lipatov <lav@altlinux.ru> 1.16-alt2
- use python2 in the script

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1.qa1
- NMU: applied repocop patch

* Fri Dec 01 2017 Vitaly Lipatov <lav@altlinux.ru> 1.16-alt1
- initial build for ALT Sisyphus

