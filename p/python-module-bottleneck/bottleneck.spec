%define oname bottleneck

%def_with python3

Name: python-module-%oname
Version: 0.8.0
Release: alt1.1

Summary: Fast NumPy array functions written in Cython
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Bottleneck/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-Cython libnumpy-devel
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils ipython python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-numpy python-module-pexpect python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base python3-module-numpy
BuildRequires: libnumpy-devel python-module-alabaster python-module-html5lib python-module-notebook python-module-numpy-testing python-module-objects.inv python3-devel python3-module-numpy-testing rpm-build-python3 time

#BuildRequires: python3-devel libnumpy-py3-devel
#BuildPreReq: python-tools-2to3
%endif

%description
Bottleneck is a collection of fast NumPy array functions written in
Cython.

%package tests
Summary: Tests for Bottleneck
Group: Development/Python
Requires: %name = %EVR

%description tests
Bottleneck is a collection of fast NumPy array functions written in
Cython.

This package contains tests for Bottleneck.

%package pickles
Summary: Pickles for Bottleneck
Group: Development/Python

%description pickles
Bottleneck is a collection of fast NumPy array functions written in
Cython.

This package contains pickles for Bottleneck.

%package docs
Summary: Documentation for Bottleneck
Group: Development/Documentation
BuildArch: noarch

%description docs
Bottleneck is a collection of fast NumPy array functions written in
Cython.

This package contains documentation for Bottleneck.

%if_with python3
%package -n python3-module-%oname
Summary: Fast NumPy array functions written in Cython
Group: Development/Python3

%description -n python3-module-%oname
Bottleneck is a collection of fast NumPy array functions written in
Cython.

%package -n python3-module-%oname-tests
Summary: Tests for Bottleneck
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Bottleneck is a collection of fast NumPy array functions written in
Cython.

This package contains tests for Bottleneck.
%endif


%prep
%setup

for i in $(find %oname -type d); do
	touch $i/__init__.py
done

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
#find -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
#find -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%add_optflags -fno-strict-aliasing

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
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.1
- NMU: Use buildreq for BR.

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1
- Version 0.8.0

* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

