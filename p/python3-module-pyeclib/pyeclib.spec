%define oname pyeclib

Name:           python3-module-%oname
Version:        1.6.1
Release:        alt1

Summary:        Python interface to erasure codes

Group:          Development/Python3
License:        BSD
URL:            https://pypi.org/project/pyeclib

Source0:        %oname-%version.tar

BuildRequires:  liberasurecode-devel >= 1.0.7
BuildRequires:  chrpath

Requires:       liberasurecode >= 1.0.7

%description
This library provides a simple Python interface for implementing erasure
codes. A number of back-end implementations is supported either directly
or through the C interface liberasurecode.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

find "%buildroot%python3_sitelibdir" -name "pyeclib_c.*.so" | xargs chrpath -d

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
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
