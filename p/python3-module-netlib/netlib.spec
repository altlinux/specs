%define oname netlib

%def_disable check

Name: python3-module-%oname
Version: 0.11
Release: alt1.git20140816.1.1
Summary: A collection of network utilities used by pathod and mitmproxy
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/netlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mitmproxy/netlib.git
# branch: python3
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
#BuildPreReq: libssl-devel
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pyasn1 python3-module-OpenSSL
#BuildPreReq: python3-module-passlib python3-module-mock
#BuildPreReq: python3-module-nose python3-module-nose-cov
#BuildPreReq: python3-module-coveralls python-tools-2to3

%py3_provides %oname
%py3_requires OpenSSL

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-logging python3 python3-base
BuildRequires: python-modules-compiler python-modules-encodings python-tools-2to3 rpm-build-python3 time

%description
Netlib is a collection of network utility classes, used by the pathod
and mitmproxy projects. It differs from other projects in some
fundamental respects, because both pathod and mitmproxy often need to
violate standards. This means that protocols are implemented as small,
well-contained and flexible functions, and are designed to allow
misbehaviour when needed.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Netlib is a collection of network utility classes, used by the pathod
and mitmproxy projects. It differs from other projects in some
fundamental respects, because both pathod and mitmproxy often need to
violate standards. This means that protocols are implemented as small,
well-contained and flexible functions, and are designed to allow
misbehaviour when needed.

This package contains tests for %oname

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=$PWD
python3 setup.py test
py.test-%_python3_version

%files
%doc *.mkd
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

#files tests
#python3_sitelibdir/*/test.*
#python3_sitelibdir/*/*/test.*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11-alt1.git20140816.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.11-alt1.git20140816.1
- NMU: Use buildreq for BR.

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.git20140816
- Initial build for Sisyphus

