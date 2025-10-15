%define oname pyeclib

%def_with check

Name:           python3-module-%oname
Version:        1.7.0
Release:        alt1

Summary:        Python interface to erasure codes

Group:          Development/Python3
License:        BSD
URL:            https://pypi.org/project/pyeclib

Source0:        %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-wheel
BuildRequires:  liberasurecode-devel >= 1.0.7
BuildRequires:  chrpath

%if_with check
BuildRequires:  python3-module-pytest
BuildRequires:  python3-module-six
%endif

Requires:       liberasurecode >= 1.0.7

%description
This library provides a simple Python interface for implementing erasure
codes. A number of back-end implementations is supported either directly
or through the C interface liberasurecode.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

find "%buildroot%python3_sitelibdir" -name "pyeclib_c.*.so" | xargs chrpath -d

%check
%pyproject_run_pytest

%files
%doc README.rst
%_bindir/pyeclib-backend
%python3_sitelibdir/%oname
%python3_sitelibdir/pyeclib_c.abi3.so
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Wed Oct 15 2025 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- Automatically updated to 1.7.0.

* Tue Oct 29 2024 Grigory Ustinov <grenka@altlinux.org> 1.6.4-alt1
- Build new version.
- Build with check.

* Sat May 25 2024 Grigory Ustinov <grenka@altlinux.org> 1.6.1-alt1
- Build new version.

* Mon Dec 13 2021 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt4
- Fix building with python3.10.

* Mon Jan 25 2021 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt3
- Fix building with python3.9.

* Sat Feb 08 2020 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt2
- Drop python2 support.

* Fri May 31 2019 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt1
- Build new version.

* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 1.0.8-alt1
- First build for ALT
