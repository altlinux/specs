%define oname json-rpc

%def_with python3

Name: python-module-%oname
Version: 1.9.0
Release: alt1.git20150324.1.1.1
Summary: JSON-RPC transport realisation
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/json-rpc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pavlov99/json-rpc.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-nose python-module-mock
#BuildPreReq: python-module-coverage
#BuildPreReq: python-modules-multiprocessing python-modules-json
#BuildPreReq: python-modules-logging
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(Pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-nose python3-module-mock
#BuildPreReq: python3-module-coverage
%endif

%py_provides jsonrpc
%py_requires json logging
%add_python_req_skip django

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-funcsigs python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pbr python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-six python3-module-unittest2
BuildRequires: python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-mock python-module-nose python-module-objects.inv python-module-setuptools python3-module-coverage python3-module-html5lib python3-module-mock python3-module-nose python3-module-setuptools rpm-build-python3 time

%description
JSON-RPC2.0 and JSON-RPC1.0 transport specification implementation.
Supports python2.6+, python3.2+, PyPy. 200+ tests.

This implementation does not have any transport functionality
realization, only protocol. Any client or server realization is easy
based on current code, but requires transport libraries, such as
requests, gevent or zmq, see examples.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
JSON-RPC2.0 and JSON-RPC1.0 transport specification implementation.
Supports python2.6+, python3.2+, PyPy. 200+ tests.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: JSON-RPC transport realisation
Group: Development/Python3
%py3_provides jsonrpc
%py3_requires json logging
%add_python3_req_skip django

%description -n python3-module-%oname
JSON-RPC2.0 and JSON-RPC1.0 transport specification implementation.
Supports python2.6+, python3.2+, PyPy. 200+ tests.

This implementation does not have any transport functionality
realization, only protocol. Any client or server realization is easy
based on current code, but requires transport libraries, such as
requests, gevent or zmq, see examples.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
JSON-RPC2.0 and JSON-RPC1.0 transport specification implementation.
Supports python2.6+, python3.2+, PyPy. 200+ tests.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
JSON-RPC2.0 and JSON-RPC1.0 transport specification implementation.
Supports python2.6+, python3.2+, PyPy. 200+ tests.

This package contains pickles for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
rm -fR jsonrpc/tests/test_backend_django
python setup.py test
%if_with python3
pushd ../python3
rm -fR jsonrpc/tests/test_backend_django
python3 setup.py test
popd
%endif

%files
%doc changelog *.rst examples docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc changelog *.rst examples docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.9.0-alt1.git20150324.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt1.git20150324.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.9.0-alt1.git20150324.1
- NMU: Use buildreq for BR.

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.git20150324
- Initial build for Sisyphus

