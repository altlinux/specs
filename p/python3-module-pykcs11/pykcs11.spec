Name: python3-module-pykcs11
Version: 1.5.16
Release: alt1

Summary: A complete PKCS#11 wrapper for Python

Group: Development/Python3
License: GPLv2
URL: https://pypi.org/project/PyKCS11
VCS: https://github.com/LudovicRousseau/PyKCS11

Source: %name-%version.tar

BuildRequires: gcc-c++ swig
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
A complete PKCS#11 wrapper for Python. You can use any PKCS#11 (aka CryptoKi)
module such as the PSM which comes as part of mozilla or the various modules
supplied by vendors of hardware crypto tokens, and almost all PKCS#11 functions
and data types. The wrapper has been generated with the help of the SWIG
compiler.

%package docs
Summary: A complete PKCS#11 wrapper for Python
Group: Development/Documentation

%description docs
A complete PKCS#11 wrapper for Python. You can use any PKCS#11 (aka CryptoKi)
module such as the PSM which comes as part of mozilla or the various modules
supplied by vendors of hardware crypto tokens, and almost all PKCS#11 functions
and data types. The wrapper has been generated with the help of the SWIG
compiler.

This package contains documentation.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/PyKCS11
%python3_sitelibdir/PyKCS11-%version.dist-info

%files docs
%doc README.md samples/

%changelog
* Sat May 25 2024 Grigory Ustinov <grenka@altlinux.org> 1.5.16-alt1
- Automatically updated to 1.5.16.

* Fri Jan 01 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.10-alt1
- Automatically updated to 1.5.10.

* Wed Sep 16 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.9-alt1
- Automatically updated to 1.5.9.
- Drop python2 support.

* Tue Sep 08 2020 Andrey Cherepanov <cas@altlinux.org> 1.4.3-alt3
- Return to Sisyphus

* Wed Apr 22 2020 Lenar Shakirov <snejok@altlinux.org> 1.4.3-alt2
- Fix python3 build

* Fri Jul 14 2017 Lenar Shakirov <snejok@altlinux.ru> 1.4.3-alt1
- Initial build for ALT
