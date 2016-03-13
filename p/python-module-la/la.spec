%define oname la

%def_with python3

Name: python-module-%oname
Version: 0.6.0
Release: alt2.1.1

Summary: Label the rows, columns, any dimension, of your NumPy arrays
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/la

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-sphinx-devel
#BuildPreReq: python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils ipython python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-numpy python-module-pexpect python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base
BuildRequires: python-module-alabaster python-module-html5lib python-module-notebook python-module-objects.inv python3-module-zope rpm-build-python3 time

#BuildRequires: python3-devel
#BuildPreReq: python-tools-2to3 python3-module-Cython
%endif

%description
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

%package tests
Summary: Tests for la
Group: Development/Python
Requires: %name = %EVR

%description tests
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

This package contains tests for la.

%package pickles
Summary: Pickles for la
Group: Development/Python

%description pickles
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

This package contains pickles for la.

%package docs
Summary: Documentation for la
Group: Development/Documentation
BuildArch: noarch

%description docs
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

This package contains documentation for la.

%if_with python3
%package -n python3-module-%oname
Summary: Label the rows, columns, any dimension, of your NumPy arrays
Group: Development/Python3

%description -n python3-module-%oname
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

%package -n python3-module-%oname-tests
Summary: Tests for la
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

This package contains tests for la.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
#find -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
#find -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
rm -f ../python3/la/src/*.c
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%make -C doc pickle
%make -C doc html

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/test*

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt2.1
- NMU: Use buildreq for BR.

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added module for Python 3

* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

