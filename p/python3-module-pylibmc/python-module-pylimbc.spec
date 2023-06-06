%define oname pylibmc

Name: python3-module-%oname
Version: 1.6.3
Release: alt1
Summary: Quick and small memcached client for Python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/pylibmc
Source: pylibmc-%version.tar.gz

BuildRequires: libmemcached-devel zlib-devel
BuildRequires(pre): rpm-build-python3

%description
Pylibmc is a Python client for memcached (<http://memcached.org/>)
written in C.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst docs
%doc README.rst docs
%python3_sitelibdir/*%{oname}*

%changelog
* Mon Dec 12 2022 Grigory Ustinov <grenka@altlinux.org> 1.6.3-alt1
- Updated for python3.11.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.2-alt2
- Drop python2 support.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.2-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 1.5.2-alt1
- Autobuild version bump to 1.5.2

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 1.5.1-alt1
- Autobuild version bump to 1.5.1

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.0-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Dec 02 2015 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1.1
- Rebuild with new libmemcached 1.0.1

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 1.5.0-alt1
- Autobuild version bump to 1.5.0

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 1.4.2-alt1
- Autobuild version bump to 1.4.2

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1
- Version 1.4.1
- Added module for Python 3

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 1.3.0-alt1
- Autobuild version bump to 1.3.0

* Wed Jul 17 2013 Fr. Br. George <george@altlinux.ru> 1.2.3-alt1
- Initial build from upstream PKG-INFO

