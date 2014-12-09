%define oname scikit-nano

%def_with python3
# very slow:
%def_disable check

Name: python-module-%oname
Version: 0.3.6
Release: alt1.git20141208
Summary: Python toolkit for nanoscience
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikit-nano/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/androomerrill/scikit-nano.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-scipy libnumpy-devel
BuildPreReq: python-module-nose python-module-six
BuildPreReq: python-module-sphinx-devel ipython python-module-numpydoc
BuildPreReq: python-module-matplotlib-sphinxext python-module-PyQt4
BuildPreReq: python-module-sphinx-argparse
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-scipy libnumpy-py3-devel
BuildPreReq: python3-module-nose python3-module-six
%endif

%py_provides sknano
%py_requires PyQt4

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
* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1.git20141208
- Version 0.3.6

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1.git20141129
- Version 0.3.4

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1.git20141125
- Version 0.3.3

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20141124
- Initial build for Sisyphus

