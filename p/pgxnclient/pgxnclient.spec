Name: pgxnclient
Version: 1.3.2
Release: alt2

Summary: A command line tool to interact with the PostgreSQL Extension Network

Url: https://pgxn.github.io/pgxnclient/
License: BSD-3-Clause
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/pgxn/pgxnclient/archive/refs/tags/v1.3.2.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-module-wheel


AutoProv: no

%description
The PGXN Client is a command line tool designed to
interact with the PostgreSQL Extension Network allowing searching,
compiling, installing, and removing extensions in PostgreSQL databases.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%_bindir/pgxn
%_bindir/%name
%python3_sitelibdir/*

%changelog
* Wed Feb 15 2023 Anton Vyatkin <toni@altlinux.org> 1.3.2-alt2
- NMU: Fix buildrequires.

* Thu Feb 02 2023 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt1
- initial build for ALT Sisyphus

