%def_without check

%define modulename daemonize
Name: python3-module-daemonize
Version: 2.5.0
Release: alt2

Summary: Library for writing system daemons in Python

Url: https://github.com/thesharp/daemonize
License: MIT
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/thesharp/daemonize/archive/v%version.tar.gz
Source: %modulename-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
daemonize is a library for writing system daemons in Python.

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
* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt2
- Drop python2 support.

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- new version 2.5.0 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.4.7-alt1.qa1
- NMU: applied repocop patch

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.4.7-alt1
- initial build for ALT Sisyphus

