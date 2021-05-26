%def_without check

%define modulename lzf
Name: python3-module-lzf
Version: 0.2.4
Release: alt2

Summary: liblzf python bindings

Url: https://github.com/matrix-org/python-canonicaljson
License: the liblzf bsd 2-clause and gpl, and own bsd 3-clause
Group: Development/Python3


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/teepark/python-lzf/archive/release-%version.tar.gz
Source: %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: liblzf-devel

%description
This package is just a straight translation of the C api of liblzf to python.
It has two functions: compress() and decompress().

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.txt
%python3_sitelibdir/*

%changelog
* Wed May 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.2.4-alt2
- Drop python2 support.

* Sat Dec 01 2018 Vitaly Lipatov <lav@altlinux.ru> 0.2.4-alt1
- initial build for ALT Sisyphus
