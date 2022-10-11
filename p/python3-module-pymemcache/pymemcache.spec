%define oname pymemcache

Name: python3-module-%oname
Version: 3.5.2
Release: alt1

Summary: A comprehensive, fast, pure Python memcached client

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/pymemcache

# https://github.com/pinterest/pymemcache.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six

BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-mock

%description
A comprehensive, fast, pure-Python memcached client.

pymemcache supports the following features:

* Complete implementation of the memcached text protocol.
* Connections using UNIX sockets, or TCP over IPv4 or IPv6.
* Configurable timeouts for socket connect and send/recv calls.
* Access to the "noreply" flag, which can significantly increase the speed of writes.
* Flexible, modular and simple approach to serialization and deserialization.
* The (optional) ability to treat network and memcached errors as cache misses.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This pakage contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test3 -v

%files
%doc *.rst *.md *.txt
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/*/test

%files tests
%python3_sitelibdir/*/test

%changelog
* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 3.5.2-alt1
- Automatically updated to 3.5.2.

* Tue Jun 01 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.3-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.3-alt1
- Updated to upstream release 1.4.3.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.7-alt1.git20141125.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7-alt1.git20141125
- Initial build for Sisyphus

