%def_with check

%define modulename unpaddedbase64

Name: python3-module-%modulename
Version: 2.1.0
Release: alt1

Summary: Encode and decode Base64 without "=" padding

Url: https://github.com/matrix-org/python-unpaddedbase64
License: Apache-2.0
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
RFC 4648 specifies that Base64 should be padded to a multiple of 4 bytes
using "=" characters. However this conveys no benefit so many protocols
choose to use Base64 without the "=" padding.

%prep
%setup
# https://bugzilla.altlinux.org/show_bug.cgi?id=39907
[ -e setup.py ] && rm -f ./setup.py
echo 'import setuptools; setuptools.setup()' > setup.py

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -m pytest

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Tue May 31 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1
- Build new version.
- Build with check.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt2
- Drop python2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1.qa1
- NMU: applied repocop patch

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Sisyphus

