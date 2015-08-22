%define mname scikits
%define oname %mname.statsmodels

%def_with python3
%def_disable check

Name: python-module-%oname
Epoch: 1
Version: 0.7.0
Release: alt2.git20150731
Summary: Statistical computations and models for use with SciPy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/statsmodels/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/statsmodels/statsmodels.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython libnumpy-devel
BuildPreReq: python-module-scipy python-module-pandas
BuildPreReq: python-module-patsy python-module-matplotlib
BuildPreReq: python-module-cvxopt python-module-nose
BuildPreReq: python-module-coverage python-module-zmq
BuildPreReq: python-module-sphinx-devel pandoc xvfb-run
BuildPreReq: python-module-matplotlib-sphinxext ipython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython libnumpy-py3-devel
BuildPreReq: python3-module-scipy python3-module-pandas
BuildPreReq: python3-module-patsy python3-module-matplotlib
BuildPreReq: python3-module-cvxopt python3-module-nose
BuildPreReq: python3-module-coverage
%endif

%py_provides %oname
%py_requires numpy scipy pandas patsy matplotlib cvxopt
%py_requires statsmodels.stats.multitest
%add_python_req_skip models

%description
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip rpy

%description tests
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Statistical computations and models for use with SciPy
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy scipy pandas patsy matplotlib cvxopt
%py3_requires statsmodels.stats.multitest
%add_python3_req_skip models

%description -n python3-module-%oname
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip rpy

%description -n python3-module-%oname-tests
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python
%add_python_req_skip load_macrodata var_plots

%description pickles
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
for i in $(find %buildroot%python_sitelibdir -name '*test*') \
	$(find %buildroot%python_sitelibdir -name '*xamp*')
do
	echo $i |sed 's|%buildroot\(.*\)|%%exclude \1\*|' >>%oname.notests
	echo $i |sed 's|%buildroot\(.*\)|\1\*|' >>%oname.tests
done

%if_with python3
pushd ../python3
%python3_install
for i in $(find %buildroot%python3_sitelibdir -name '*test*') \
	$(find %buildroot%python3_sitelibdir -name '*xamp*')
do
	echo $i |sed 's|%buildroot\(.*\)|%%exclude \1\*|' >>%oname.notests
	echo $i |sed 's|%buildroot\(.*\)|\1\*|' >>%oname.tests
done
popd
%endif

python setup.py build_ext -i
export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
xvfb-run python setup.py test
%if_with python3
pushd ../python3
xvfb-run python3 setup.py test
popd
%endif

%files -f %oname.notests
%doc *.md *.rst README_l1.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files tests -f %oname.tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples docs/*.pdf docs/build/html

%if_with python3
%files -n python3-module-%oname -f ../python3/%oname.notests
%doc *.md *.rst README_l1.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/*/*/example*
%exclude %python3_sitelibdir/*/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests -f ../python3/%oname.tests
%python3_sitelibdir/*/*/*/*/example*
%python3_sitelibdir/*/*/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150731
- New snapshot

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150323
- New snapshot

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150216
- Added requires statsmodels.stats.multitest

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt1.git20150216
- Initial build for Sisyphus

