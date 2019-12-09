%define oname pycryptodome

Name:     python3-module-%oname
Version:  3.9.4
Release:  alt1

Summary:  A self-contained cryptographic library for Python

# The source code in PyCryptodome is partially in the public domain
# and partially released under the BSD 2-Clause license.
# In either case, there are minimal if no restrictions on the redistribution,
# modification and usage of the software.
License:  BSD 2-Clause
Group:    Development/Python3
Url:      https://www.pycryptodome.org
# https://github.com/Legrandin/pycryptodome

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-python3

Conflicts: python3-module-Crypto < %EVR
Conflicts: python3-module-pyrypto < %EVR
Obsoletes: python3-module-Crypto < %EVR
Obsoletes: python3-module-pyrypto < %EVR
Provides: python3-module-Crypto = %EVR
%py3_provides Crypto

%description
PyCryptodome is a self-contained Python package of low-level
cryptographic primitives.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
PyCryptodome is a self-contained Python package of low-level
cryptographic primitives.

This package contains tests for %oname.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc AUTHORS.rst Changelog.rst README.rst
%python3_sitelibdir/Crypto
%python3_sitelibdir/%oname-%version-py?.?.egg-info
%exclude %python3_sitelibdir/*/SelfTest

%files tests
%python3_sitelibdir/*/SelfTest

%changelog
* Mon Dec 09 2019 Grigory Ustinov <grenka@altlinux.org> 3.9.4-alt1
- Initial build for Sisyphus.
