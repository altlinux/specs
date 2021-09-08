Name: python3-module-z3c
Summary: Pure namespace package 'z3c' for Python 2
Version: 3.0.0
Release: alt4
License: ZPL
Group: Development/Python3

Source: __init__.py
BuildRequires(pre): rpm-build-python3

%description
%summary

%install
install -Dm644 %SOURCE0 %buildroot%python3_sitelibdir/z3c/__init__.py

%files
%python3_sitelibdir/z3c

%changelog
* Wed Sep 08 2021 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt4
- Drop python2 support.

* Sat Feb 02 2019 Ivan A. Melnikov <iv@altlinux.org> 3.0.0-alt3
- Build as a separate package
