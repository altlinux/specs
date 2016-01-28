%define oname meta

%def_with python3

Name: python-module-%oname
Version: 0.4.0
Release: alt2.git20120510.1
Summary: Framework to manipulate and analyze python ast's and bytecode
License: BSD-like
Group: Development/Python
Url: http://numba.pydata.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: rpm-build-python python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-module-setuptools rpm-build-python3 time

%description
A Pure Python module containing a framework to manipulate and analyze
python ast's and bytecode.

%package -n python3-module-%oname
Summary: Framework to manipulate and analyze python ast's and bytecode
Group: Development/Python3

%description -n python3-module-%oname
A Pure Python module containing a framework to manipulate and analyze
python ast's and bytecode.

%package -n python3-module-%oname-tests
Summary: Tests for Meta
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A Pure Python module containing a framework to manipulate and analyze
python ast's and bytecode.

This package contains tests for Meta.

%package tests
Summary: Tests for Meta
Group: Development/Python
Requires: %name = %EVR

%description tests
A Pure Python module containing a framework to manipulate and analyze
python ast's and bytecode.

This package contains tests for Meta.

%package pickles
Summary: Pickles for Meta
Group: Development/Python

%description pickles
A Pure Python module containing a framework to manipulate and analyze
python ast's and bytecode.

This package contains pickles for Meta.

%package docs
Summary: Documentation for Meta
Group: Development/Documentation

%description docs
A Pure Python module containing a framework to manipulate and analyze
python ast's and bytecode.

This package contains documentation for Meta.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR _build/pickle %buildroot%python_sitelibdir/meta/

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/testing.py*
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc _build/html/*

%files tests
%python_sitelibdir/*/testing.py*
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/testing.py*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/testing.py*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt2.git20120510.1
- NMU: Use buildreq for BR.

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2.git20120510
- Added module for Python 3

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20120510
- Initial build for Sisyphus

