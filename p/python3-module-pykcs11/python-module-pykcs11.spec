Name: python3-module-pykcs11
Version: 1.4.3
Release: alt2

Summary: A complete PKCS#11 wrapper for Python
Group: Development/Python3
License: GPLv2
URL: https://github.com/LudovicRousseau/PyKCS11

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++


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
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_install

%install
%python3_install

%files
%python3_sitelibdir/*

%files docs
%doc README.md samples/


%changelog
* Mon Dec 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4.3-alt2
- python2 disabled

* Fri Jul 14 2017 Lenar Shakirov <snejok@altlinux.ru> 1.4.3-alt1
- Initial build for ALT
