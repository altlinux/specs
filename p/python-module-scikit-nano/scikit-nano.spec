%define oname scikit-nano

%def_with python3
# very slow:
%def_disable check

Name: python-module-%oname
Version: 0.3.6
Release: alt1.git20141208.1
Summary: Python toolkit for nanoscience
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikit-nano/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/androomerrill/scikit-nano.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-scipy libnumpy-devel
#BuildPreReq: python-module-nose python-module-six
#BuildPreReq: python-module-sphinx-devel ipython python-module-numpydoc
#BuildPreReq: python-module-matplotlib-sphinxext python-module-PyQt4
#BuildPreReq: python-module-sphinx-argparse
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-scipy libnumpy-py3-devel
#BuildPreReq: python3-module-nose python3-module-six
%endif

%py_provides sknano
%py_requires PyQt4

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: fontconfig ipython libnumpy-devel libqt4-core libqt4-gui python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cssselect python-module-cycler python-module-dateutil python-module-decorator python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-greenlet python-module-ipykernel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-mpmath python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-notebook python-module-numpy python-module-numpydoc python-module-path python-module-pexpect python-module-pickleshare python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-simplegeneric python-module-sip python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-numpy
BuildRequires: libnumpy-py3-devel python-module-PyQt4 python-module-alabaster python-module-html5lib python-module-ipyparallel python-module-matplotlib-sphinxext python-module-numpy-testing python-module-objects.inv python-module-scipy python-module-sphinx-argparse python3-module-numpy-testing python3-module-scipy python3-module-six rpm-build-python3 time

%description
scikit-nano is a python toolkit for generating and analyzing
nanostructure data.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
scikit-nano is a python toolkit for generating and analyzing
nanostructure data.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python toolkit for nanoscience
Group: Development/Python3
%py3_provides sknano
%py3_requires PyQt4

%description -n python3-module-%oname
scikit-nano is a python toolkit for generating and analyzing
nanostructure data.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
scikit-nano is a python toolkit for generating and analyzing
nanostructure data.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
scikit-nano is a python toolkit for generating and analyzing
nanostructure data.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
scikit-nano is a python toolkit for generating and analyzing
nanostructure data.

This package contains documentaiton for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%install
%if_with python3
pushd ../python3
%python3_install
popd
#pushd %buildroot%_bindir
#for i in $(ls); do
#	mv $i $i.py3
#done
#popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
#_bindir/*
#if_with python3
#exclude %_bindir/*.py3
#endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/testing
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%files tests
%python_sitelibdir/*/testing
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
#_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/testing
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/testing
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.6-alt1.git20141208.1
- NMU: Use buildreq for BR.

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1.git20141208
- Version 0.3.6

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1.git20141129
- Version 0.3.4

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1.git20141125
- Version 0.3.3

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20141124
- Initial build for Sisyphus

