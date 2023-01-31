%define oname pycryptodome

Name:     python3-module-%oname
Version:  3.17.0
Release:  alt1

Summary:  A self-contained cryptographic library for Python

# The source code in PyCryptodome is partially in the public domain
# and partially released under the BSD 2-Clause license.
# In either case, there are minimal if no restrictions on the redistribution,
# modification and usage of the software.
License:  BSD-2-Clause
Group:    Development/Python3
Url:      https://www.pycryptodome.org
# https://github.com/Legrandin/pycryptodome

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-python3

Conflicts: python3-module-Crypto < %EVR
Conflicts: python3-module-pycrypto < %EVR
Obsoletes: python3-module-Crypto < %EVR
Obsoletes: python3-module-pycrypto < %EVR
Provides: python3-module-Crypto = %EVR
Provides: python3-module-pycrypto = %EVR
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

# hotfix for version
sed -i 's/17/17, 0/' lib/Crypto/__init__.py

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
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/*/SelfTest

%files tests
%python3_sitelibdir/*/SelfTest

%changelog
* Tue Jan 31 2023 Grigory Ustinov <grenka@altlinux.org> 3.17.0-alt1
- Automatically updated to 3.17.0.

* Tue Nov 29 2022 Grigory Ustinov <grenka@altlinux.org> 3.16.0-alt1
- Automatically updated to 3.16.0.

* Sat Jun 25 2022 Grigory Ustinov <grenka@altlinux.org> 3.15.0-alt1
- Automatically updated to 3.15.0.

* Thu Apr 14 2022 Grigory Ustinov <grenka@altlinux.org> 3.14.1-alt1
- Automatically updated to 3.14.1.

* Mon Dec 06 2021 Grigory Ustinov <grenka@altlinux.org> 3.11.0-alt2
- Fixed build for python3.10.

* Tue Oct 12 2021 Grigory Ustinov <grenka@altlinux.org> 3.11.0-alt1
- Automatically updated to 3.11.0.

* Wed Mar 17 2021 Grigory Ustinov <grenka@altlinux.org> 3.10.1-alt1
- Automatically updated to 3.10.1.

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 3.9.9-alt1
- Automatically updated to 3.9.9.

* Mon Sep 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.9.8-alt2
- NMU: fixed conflicts and obsoletes, updated provides.

* Thu Jun 25 2020 Grigory Ustinov <grenka@altlinux.org> 3.9.8-alt1
- Automatically updated to 3.9.8.

* Thu May 28 2020 Grigory Ustinov <grenka@altlinux.org> 3.9.7-alt1
- Automatically updated to 3.9.7.

* Mon Dec 09 2019 Grigory Ustinov <grenka@altlinux.org> 3.9.4-alt1
- Initial build for Sisyphus.
