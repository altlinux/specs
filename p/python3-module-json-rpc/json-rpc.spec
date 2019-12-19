%define oname json-rpc

Name: python3-module-%oname
Version: 1.9.0
Release: alt2

Summary: JSON-RPC transport realisation
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/json-rpc/
BuildArch: noarch

# https://github.com/pavlov99/json-rpc.git
Source: %name-%version.tar
Patch0: port-on-new-django.patch

BuildRequires(Pre): rpm-build-python3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-mock python3-module-nose


%description
JSON-RPC2.0 and JSON-RPC1.0 transport specification implementation.
Supports python2.6+, python3.2+, PyPy. 200+ tests.

This implementation does not have any transport functionality
realization, only protocol. Any client or server realization is easy
based on current code, but requires transport libraries, such as
requests, gevent or zmq, see examples.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
JSON-RPC2.0 and JSON-RPC1.0 transport specification implementation.
Supports python2.6+, python3.2+, PyPy. 200+ tests.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
JSON-RPC2.0 and JSON-RPC1.0 transport specification implementation.
Supports python2.6+, python3.2+, PyPy. 200+ tests.

This package contains pickles for %oname.

%prep
%setup
%patch0 -p1

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
rm -fR jsonrpc/tests/test_backend_django
%__python3 setup.py test

%files
%doc changelog *.rst examples docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files pickles
%python3_sitelibdir/*/pickle


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.9.0-alt2
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.9.0-alt1.git20150324.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt1.git20150324.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.9.0-alt1.git20150324.1
- NMU: Use buildreq for BR.

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.git20150324
- Initial build for Sisyphus

