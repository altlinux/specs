%def_without check

%define modulename pyperf
Name: python3-module-pyperf
Version: 1.7.0
Release: alt2

Summary: Python module to run and analyze benchmarks

Url: https://github.com/vstinner/pyperf
License: the libpyperf bsd 2-clause and gpl, and own bsd 3-clause
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/vstinner/pyperf/archive/%version.tar.gz
Source: %modulename-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
The Python pyperf module is a toolkit to write, run and analyze benchmarks.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install
rm -rfv %buildroot%python3_sitelibdir/pyperf/tests/

%files
%_bindir/pyperf
%doc README.rst
%python3_sitelibdir/*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt2
- Drop python2 support.

* Mon Jan 27 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- initial build for ALT Sisyphus
