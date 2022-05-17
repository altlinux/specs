%def_without check

%define modulename pynacl
Name: python3-module-pynacl
Version: 1.5.0
Release: alt1

Summary: Python binding to the Networking and Cryptography (NaCl) library

Url: https://github.com/pyca/pynacl
License: Apache-2.0
Group: Development/Python3

# Source-url: https://github.com/pyca/pynacl/archive/%version.tar.gz
Source: %modulename-%version.tar

BuildRequires:  libsodium-devel >= 1.0.16

BuildRequires(pre): rpm-build-python3 python3-module-wheel
BuildRequires: python3-module-cffi

%description
PyNaCl is a Python binding to the Networking and Cryptography library,
a crypto library with the stated goal of improving usability, security
and speed.

%prep
%setup -n %modulename-%version
# Remove bundled libsodium, to be sure
rm -vrf src/libsodium/

%build
export SODIUM_INSTALL=system
%python3_build

%install
%python3_install
# FIXME
mv %buildroot/%python3_sitelibdir/nacl/_sodium.abi3.so %buildroot/%python3_sitelibdir/nacl/_sodium.so

%files
%doc README.rst
%doc README.rst
%python3_sitelibdir/*

%changelog
* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt1
- 1.5.0 released

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0 released

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt2
- Drop python2 support.

* Tue Jan 22 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1.1.1.qa1
- NMU: applied repocop patch

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.2-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Feb 12 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1.1
- NMU: autorebuild with libsodium-1.0.16

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- initial build for ALT Sisyphus

