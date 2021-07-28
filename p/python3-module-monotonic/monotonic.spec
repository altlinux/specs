%define _unpackaged_files_terminate_build 1
%define oname monotonic

Name: python3-module-%oname
Version: 1.5
Release: alt2
Summary: An implementation of time.monotonic() for Python 2 & Python 3
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/monotonic/

# https://github.com/atdt/monotonic.git
Source: %name-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
This module provides a monotonic() function which returns the value (in
fractional seconds) of a clock which never goes backwards.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/monotonic.py
%python3_sitelibdir/__pycache__/monotonic.cpython-*
%python3_sitelibdir/monotonic-%version-py%_python3_version.egg-info/

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 1.5-alt2
- Drop python2 support.

* Sat Apr 27 2019 Stanislav Levin <slev@altlinux.org> 1.5-alt1
- 1.2 -> 1.5.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1
- automated PyPI update

* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- 1.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.4-alt1
- 0.4

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141129
- Initial build for Sisyphus

