%define oname fipy

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 3.1
Release: alt3.dev120.git20150826
Summary: Partial differential equation (PDE) solver
License: Public
Group: Development/Python
Url: http://www.ctcms.nist.gov/fipy
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: FiPy-%version.tar
Source1: %oname-%version.pdf
#Source2: reference-2.0.2.pdf
BuildArch: noarch

BuildPreReq: texlive-latex-recommended
BuildPreReq: python-devel libnumpy-devel python-module-pysparse git
BuildPreReq: python-module-setuptools-tests python-module-bitten
BuildPreReq: python-module-scipy python-module-gist xvfb-run
BuildPreReq: python-module-matplotlib python-module-gnuplot
BuildPreReq: python-module-sphinx-devel python-module-numpydoc
BuildPreReq: python-module-sphinxcontrib.traclinks python-module-vtk6.2
BuildPreReq: python-module-bibtex python-module-PyQt4
%setup_python_module %oname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel libnumpy-py3-devel python3-module-scipy
BuildPreReq: python3-module-setuptools-tests
BuildPreReq: python3-module-matplotlib python3-module-gist
BuildPreReq: python-tools-2to3 python3-module-gnuplot
%endif

Requires: python-module-gnuplot
%py_requires gist numpy pysparse scipy mayavi

%description
FiPy is an object oriented, partial differential equation (PDE) solver,
written in Python, based on a standard finite volume (FV) approach

The solution of coupled sets of PDEs is ubiquitous to the numerical
simulation of science problems.  Numerous PDE solvers exist, using a
variety of languages and numerical approaches. Many are proprietary,
expensive and difficult to customize.  As a result, scientists spend
considerable resources repeatedly developing limited tools for
specific problems.  Our approach, combining the FV method and Python_,
provides a tool that is extensible, powerful and freely available. A
significant advantage to Python_ is the existing suite of tools for
array calculations, sparse matrices and data rendering.

%package -n python3-module-%oname
Summary: Partial differential equation (PDE) solver
Group: Development/Python3
Requires: python3-module-gnuplot
%py3_requires gist numpy scipy
%add_python3_req_skip mayavi pysparse

%description -n python3-module-%oname
FiPy is an object oriented, partial differential equation (PDE) solver,
written in Python, based on a standard finite volume (FV) approach

The solution of coupled sets of PDEs is ubiquitous to the numerical
simulation of science problems.  Numerous PDE solvers exist, using a
variety of languages and numerical approaches. Many are proprietary,
expensive and difficult to customize.  As a result, scientists spend
considerable resources repeatedly developing limited tools for
specific problems.  Our approach, combining the FV method and Python_,
provides a tool that is extensible, powerful and freely available. A
significant advantage to Python_ is the existing suite of tools for
array calculations, sparse matrices and data rendering.

%package -n python3-module-%oname-tests
Summary: Tests for FiPy
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
FiPy is an object oriented, partial differential equation (PDE) solver,
written in Python, based on a standard finite volume (FV) approach

This package contains tests for FiPy.

%package pickles
Summary: Pickles for FiPy
Group: Development/Python

%description pickles
FiPy is an object oriented, partial differential equation (PDE) solver,
written in Python, based on a standard finite volume (FV) approach

This package contains pickles for FiPy.

%package tests
Summary: Tests for FiPy
Group: Development/Python
Requires: %name = %version-%release

%description tests
FiPy is an object oriented, partial differential equation (PDE) solver,
written in Python, based on a standard finite volume (FV) approach

This package contains tests for FiPy.

%package examples
Summary: Examples for FiPy
Group: Development/Documentation
Requires: %name = %version-%release

%description examples
FiPy is an object oriented, partial differential equation (PDE) solver,
written in Python, based on a standard finite volume (FV) approach

This package contains examples for FiPy.

%package doc
Summary: Documentation for FiPy
Group: Development/Documentation
BuildArch: noarch

%description doc
FiPy is an object oriented, partial differential equation (PDE) solver,
written in Python, based on a standard finite volume (FV) approach

This package contains documentation for FiPy.

%prep
%setup
#sed -i 's|with|with_|' \
#	fipy/viewers/gnuplotViewer/gnuplot1DViewer.py

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "version-%version" version-%version
python setup.py egg_info

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

install -p -m644 %SOURCE1 .

%prepare_sphinx .
ln -s ../objects.inv documentation/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

#install -d %buildroot%python_sitelibdir/%oname/utils
#install -p -m644 utils/* \
#	%buildroot%python_sitelibdir/%oname/utils

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
xvfb-run python setup.py build_docs --pickle
xvfb-run python setup.py build_docs --html
install -d %buildroot%_docdir/%name
cp -fR documentation/_build/html %buildroot%_docdir/%name/
cp -fR documentation/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
xvfb-run python setup.py test
%if_with python3
#if 0
pushd ../python3
xvfb-run python3 setup.py test
popd
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

%files examples
%doc examples/*

%files doc
%doc *.rst *.pdf
%_docdir/%name

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Wed Feb 10 2016 Denis Medvedev <nbr@altlinux.org>  3.1-alt3.dev120.git20150826
- NMU

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt2.dev120.git20150826
- Version 3.1-dev120

* Thu Apr 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt2.dev76.git20150409
- Version 3.1-dev76

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt2
- Added module for Python 3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1
- Version 3.1

* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Version 3.0

* Mon Jun 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.3-alt1
- Version 2.1.3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.2-alt1.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1
- Version 2.1.2

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt2
- Added BuildPreReq: python-module-setuptools-tests

* Tue Jul 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1
- Version 2.1

* Sun Mar 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt5
- Extracted examples and tests into separate package

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt4
- Rebuilt with python 2.6

* Thu Oct 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt3
- Rebuilt with fixed python2.x(Gnuplot) by upsream

* Mon Sep 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt2
- Added requirement on python2.x(gist)
- Renamed field in class PlotItem of python2.6(gnuplot): with -> style

* Sun Sep 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Initial build for Sisyphus

