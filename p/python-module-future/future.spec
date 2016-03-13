%define oname future

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.15.0
Release: alt1.git20150725.1.1
Summary: Clean single-source support for Python 3 and 2
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/future
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/PythonCharmers/python-future.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-sphinx-devel
#BuildPreReq: python-module-setuptools-tests
#BuildPreReq: python-module-sphinx-bootstrap-theme python-tools-2to3
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-Fabric python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-ecdsa python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-nose python-module-pycrypto python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-pytest python-module-sphinx-bootstrap-theme python3-module-pytest rpm-build-python3 time

%description
future is the missing compatibility layer between Python 3 and Python 2.
It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 3 and Python 2 with minimal overhead.

%package tests
Summary: Tests for future
Group: Development/Python
Requires: %name = %EVR

%description tests
future is the missing compatibility layer between Python 3 and Python 2.
It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 3 and Python 2 with minimal overhead.

This package contains tests for future.

%package pickles
Summary: Pickles for future
Group: Development/Python

%description pickles
future is the missing compatibility layer between Python 3 and Python 2.
It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 3 and Python 2 with minimal overhead.

This package contains pickles for future.

%package docs
Summary: Documentation for future
Group: Development/Documentation

%description docs
future is the missing compatibility layer between Python 3 and Python 2.
It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 3 and Python 2 with minimal overhead.

This package contains docs for future.

%package -n python3-module-%oname
Summary: Clean single-source support for Python 3 and 2
Group: Development/Python3

%description -n python3-module-%oname
future is the missing compatibility layer between Python 3 and Python 2.
It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 3 and Python 2 with minimal overhead.

%package -n python3-module-%oname-tests
Summary: Tests for future
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
future is the missing compatibility layer between Python 3 and Python 2.
It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 3 and Python 2 with minimal overhead.

This package contains tests for future.

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
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/
export PYTHONPATH=

%check
python setup.py build_ext -i
export PYTHONPATH=$PWD/src
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
export PYTHONPATH=$PWD/src
python3 setup.py test -v
popd
%endif

%files
%doc *.txt *.rst
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/test
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/*/test
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/notebooks docs/other docs/build/html

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.15.0-alt1.git20150725.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.15.0-alt1.git20150725.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt1.git20150725
- Version 0.15.0

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.3-alt1.git20150203
- Version 0.14.3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.3-alt1
- Initial build for Sisyphus

