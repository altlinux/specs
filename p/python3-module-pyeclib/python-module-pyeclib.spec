%define oname pyeclib

Name:           python3-module-%oname
Version:        1.6.0
Release:        alt1
Summary:        Python interface to erasure codes
Group:          Development/Python3

License:        BSD
URL:            https://pypi.org/project/pyeclib
Source0:        %oname-%version.tar

BuildRequires:  python3-devel
BuildRequires:  python3-module-setuptools
BuildRequires:  liberasurecode-devel >= 1.0.7

%if "3"=="3"
BuildRequires:  chrpath
%endif

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

%if "3"=="3"
chrpath -d "%buildroot%python3_sitelibdir/pyeclib_c.cpython-37m.so"
%endif

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Fri May 31 2019 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt1
- Build new version.

* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 1.0.8-alt1
- First build for ALT
