%define oname pymemcache

Name: python3-module-%oname
Version: 1.4.3
Release: alt2
Summary: A comprehensive, fast, pure Python memcached client
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/pymemcache/

# https://github.com/pinterest/pymemcache.git
Source: %name-%version.tar
BuildArch: noarch
Patch1: %oname-%version-alt-tests.patch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-six python3-module-nose
BuildRequires: python3-module-mock
BuildRequires: python3-module-pytest

%description
pymemcache supports the following features:

* Complete implementation of the memcached text protocol.
* Configurable timeouts for socket connect and send/recv calls.
* Access to the "noreply" flag, which can significantly increase the
  speed of writes.
* Flexible, simple approach to serialization and deserialization.
* The (optional) ability to treat network and memcached errors as cache
  misses.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
pymemcache supports the following features:

* Complete implementation of the memcached text protocol.
* Configurable timeouts for socket connect and send/recv calls.
* Access to the "noreply" flag, which can significantly increase the
  speed of writes.
* Flexible, simple approach to serialization and deserialization.
* The (optional) ability to treat network and memcached errors as cache
  misses.

This pakage contains tests for %oname.

%prep
%setup
%patch1 -p1

%build
%python3_build

%install
%python3_install

%check
py.test3

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files tests
%python3_sitelibdir/*/test

%changelog
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

