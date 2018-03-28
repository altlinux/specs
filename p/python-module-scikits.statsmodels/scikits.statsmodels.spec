%define mname scikits
%define oname %mname.statsmodels

%def_with python3
%def_without doc
%def_disable check

Name: python-module-%oname
Epoch: 1
Version: 0.8.0
Release: alt1
Summary: Statistical computations and models for use with SciPy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/statsmodels/

# https://github.com/statsmodels/statsmodels.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: libnumpy-devel python-module-Cython python-module-ipyparallel python-module-numpy-testing python-module-pandas-tests
%if_with doc
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: fonts-bitmap-misc python-module-alabaster python-module-matplotlib-sphinxext
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: libnumpy-py3-devel python3-module-Cython python3-module-ipyparallel python3-module-numexpr-tests python3-module-numpy-testing
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

%if_with python3
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
%endif

%if_with doc
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
%endif

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

%if_with doc
python setup.py build_ext -i
export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/
%endif

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
%if_with doc
%exclude %python_sitelibdir/*/pickle
%endif

%files tests -f %oname.tests

%if_with doc
%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples docs/*.pdf docs/build/html
%endif

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
* Wed Mar 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.8.0-alt1
- Updated to upstream version 0.8.0.
- Disabled docs generation.

* Wed Mar 30 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.7.0-alt4.git20150731.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Mar 30 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.7.0-alt4.git20150731
- rm inessential BR: python3-module-pandas{,-tests} (incorrectly detected by buildreq).

* Fri Mar 25 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.7.0-alt3.git20150731
- BRs fixed with buildreq again (cleared off self-dependence and other
  unneeded pkgs with python-module-setuptools-18.1-alt3,
  python-2.7.11-alt2, and python-module-Cython-0.23.4-alt3).

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:0.7.0-alt2.git20150731.1
- NMU: Use buildreq for BR.

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150731
- New snapshot

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150323
- New snapshot

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150216
- Added requires statsmodels.stats.multitest

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt1.git20150216
- Initial build for Sisyphus

