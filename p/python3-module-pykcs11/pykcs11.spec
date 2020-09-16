Name: python3-module-pykcs11
Version: 1.5.9
Release: alt1
Summary: A complete PKCS#11 wrapper for Python
Group: Development/Python3
License: GPLv2
URL: https://github.com/LudovicRousseau/PyKCS11

Source: %name-%version.tar

BuildRequires: gcc-c++ swig
BuildRequires: rpm-build-python3 python3-module-setuptools python3-devel

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
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%files docs
%doc README.md samples/

%changelog
* Wed Sep 16 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.9-alt1
- Automatically updated to 1.5.9.
- Drop python2 support.

* Tue Sep 08 2020 Andrey Cherepanov <cas@altlinux.org> 1.4.3-alt3
- Return to Sisyphus

* Wed Apr 22 2020 Lenar Shakirov <snejok@altlinux.org> 1.4.3-alt2
- Fix python3 build

* Fri Jul 14 2017 Lenar Shakirov <snejok@altlinux.ru> 1.4.3-alt1
- Initial build for ALT
