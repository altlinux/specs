%define oname filterpy

%def_with python3

Name: python-module-%oname
Version: 0.0.16
Release: alt1.git20150217.1
Summary: Kalman filtering and optimal estimation library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/filterpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rlabbe/filterpy.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-scipy python-module-matplotlib
#BuildPreReq: python-module-mock libnumpy-devel
#BuildPreReq: python-module-nose python-module-pytz
#BuildPreReq: python-module-pygobject3 python-module-pycairo
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-scipy python3-module-matplotlib
#BuildPreReq: python3-module-mock libnumpy-py3-devel
#BuildPreReq: python3-module-nose python3-module-pytz
#BuildPreReq: python3-module-pygobject3 python3-module-pycairo
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-cycler python-module-dateutil python-module-funcsigs python-module-future python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mpmath python-module-numpy python-module-pbr python-module-pyparsing python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-cycler python3-module-dateutil python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-numpy python3-module-pip python3-module-pycparser python3-module-pyparsing python3-module-pytest python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-matplotlib python-module-mock python-module-nose python-module-objects.inv python-module-pygobject3 python-module-scipy python-module-setuptools-tests python3-module-html5lib python3-module-matplotlib python3-module-nose python3-module-pbr python3-module-pycairo python3-module-pygobject3 python3-module-pytz python3-module-scipy python3-module-setuptools-tests python3-module-unittest2 rpm-build-python3 time

%description
This library provides Kalman filtering and various related optimal and
non-optimal filtering software written in Python. It contains Kalman
filters, Extended Kalman filters, Unscented Kalman filters, Kalman
smoothers, Least Squares filters, fading memory filters, g-h filters,
discrete Bayes, and more.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip SigmaPoints

%description tests
This library provides Kalman filtering and various related optimal and
non-optimal filtering software written in Python. It contains Kalman
filters, Extended Kalman filters, Unscented Kalman filters, Kalman
smoothers, Least Squares filters, fading memory filters, g-h filters,
discrete Bayes, and more.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Kalman filtering and optimal estimation library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This library provides Kalman filtering and various related optimal and
non-optimal filtering software written in Python. It contains Kalman
filters, Extended Kalman filters, Unscented Kalman filters, Kalman
smoothers, Least Squares filters, fading memory filters, g-h filters,
discrete Bayes, and more.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip SigmaPoints

%description -n python3-module-%oname-tests
This library provides Kalman filtering and various related optimal and
non-optimal filtering software written in Python. It contains Kalman
filters, Extended Kalman filters, Unscented Kalman filters, Kalman
smoothers, Least Squares filters, fading memory filters, g-h filters,
discrete Bayes, and more.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This library provides Kalman filtering and various related optimal and
non-optimal filtering software written in Python. It contains Kalman
filters, Extended Kalman filters, Unscented Kalman filters, Kalman
smoothers, Least Squares filters, fading memory filters, g-h filters,
discrete Bayes, and more.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This library provides Kalman filtering and various related optimal and
non-optimal filtering software written in Python. It contains Kalman
filters, Extended Kalman filters, Unscented Kalman filters, Kalman
smoothers, Least Squares filters, fading memory filters, g-h filters,
discrete Bayes, and more.

This package contains documentation for %oname.

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

rm -f requirements.txt

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/examples

%files tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/examples

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/examples

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/examples
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.16-alt1.git20150217.1
- NMU: Use buildreq for BR.

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.16-alt1.git20150217
- Version 0.0.16

* Mon Dec 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20141130
- Version 0.0.7

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt2.git20141122
- Moved examples into tests subpackage

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20141122
- Initial build for Sisyphus

