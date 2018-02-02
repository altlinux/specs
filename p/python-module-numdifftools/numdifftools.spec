# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.git20150828.1.1.1
%define oname numdifftools

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.9.12
#Release: alt1.git20150828.1
Summary: Solves automatic numerical differentiation problems in one or more variables
License: BSD
Group: Development/Python
Url: http://code.google.com/p/numdifftools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pbrod/numdifftools.git
Source: Numdifftools-%version.tar
#BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-scipy git xvfb-run
BuildPreReq: python-module-numpy-addons python-module-matplotlib
BuildPreReq: python-module-coverage python-module-setuptools
BuildPreReq: python-module-setuptools_scm python-module-six
BuildPreReq: python-module-algopy python-module-numpydoc
BuildPreReq: python-module-pytest-runner python-module-pycairo
BuildPreReq: python-module-pytest-cov python-module-nose
BuildPreReq: python-module-sphinx-devel python-module-pygobject3
BuildPreReq: python-module-sphinx_rtd_theme texlive-latex-recommended
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-scipy
BuildPreReq: python3-module-numpy-addons python3-module-matplotlib
BuildPreReq: python3-module-coverage python3-module-setuptools
BuildPreReq: python3-module-setuptools_scm python3-module-six
BuildPreReq: python3-module-algopy python3-module-nose
BuildPreReq: python3-module-pytest-runner
BuildPreReq: python3-module-pytest-cov
%endif

%py_provides %oname
%py_requires numpy scipy algopy

%description
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

%package -n python3-module-%oname
Summary: Solves automatic numerical differentiation problems in one or more variables
Group: Development/Python3

%description -n python3-module-%oname
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

%package -n python3-module-%oname-test
Summary: Test suite for Numdifftools
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-test
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

This package contains test suite for Numdifftools.

%package pickles
Summary: Pickles for Numdifftools
Group: Development/Python

%description pickles
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

This package contains pickles for Numdifftools.

%package test
Summary: Test suite for Numdifftools
Group: Development/Python
Requires: %name = %version-%release

%description test
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

This package contains test suite for Numdifftools.

%package doc
Summary: Documentation for Numdifftools
Group: Development/Documentation

%description doc
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

This package contains documentation for Numdifftools.

%prep
%setup

git config --global user.email "real at atlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

export PYTHONPATH=$PWD
python setup.py test ||:
xvfb-run python setup.py docs
xvfb-run make -C docs pickle

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=%buildroot%python_sitelibdir
mkdir -p ~/.matplotlib
cp %_libdir/python%_python_version/site-packages/matplotlib/mpl-data/matplotlibrc \
	~/.matplotlib/
sed -i 's|^\(backend\).*|\1 : Agg|' ~/.matplotlib/matplotlibrc
pushd ~
xvfb-run python -c "import numdifftools as nd; nd.test(coverage=True)"
popd
xvfb-run py.test -vv -rsxXf
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd ~
xvfb-run python3 -c "import numdifftools as nd; nd.test(coverage=True)"
popd
xvfb-run py.test-%_python3_version -vv -rsxXf
popd
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test*
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files test
%python_sitelibdir/%oname/test*

%files doc
%doc docs/*.pdf docs/_build/html

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test*
%exclude %python3_sitelibdir/%oname/*/test*

%files -n python3-module-%oname-test
%python3_sitelibdir/%oname/test*
%python3_sitelibdir/%oname/*/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.12-alt1.git20150828.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.12-alt1.git20150828.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.12-alt1.git20150828.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.12-alt1.git20150828
- Version 0.9.12

* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1.git20141217
- Version 0.7.3

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2.svn20140221
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.svn20140221
- Version 0.6.0

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Version 0.4.0

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1
- Version 0.3.5

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.4-alt1.1
- Rebuild with Python-2.7

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus

