%define oname fipy
Name: python-module-%oname
Version: 2.1.3
Release: alt1
Summary: Partial differential equation (PDE) solver
License: Public
Group: Development/Python
Url: http://www.ctcms.nist.gov/fipy
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: FiPy-%version.tar.gz
Source1: %oname-%version.pdf
#Source2: reference-2.0.2.pdf
BuildArch: noarch

BuildPreReq: python-devel libnumpy-devel python-module-pysparse
BuildPreReq: python-module-setuptools-tests
%setup_python_module %oname

Requires: python-module-gnuplot
%py_requires gist

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

install -p -m644 %SOURCE1 .

%build
%python_build

%install
%python_install

#install -d %buildroot%python_sitelibdir/%oname/utils
#install -p -m644 utils/* \
#	%buildroot%python_sitelibdir/%oname/utils
cp -fR examples %buildroot%python_sitelibdir/%oname/

install -d %buildroot%_docdir/%name
cp -fR documentation/* %buildroot%_docdir/%name/

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/examples

%files tests
%python_sitelibdir/*/tests

%files examples
%python_sitelibdir/*/examples

%files doc
%doc DISCLAIMER.txt LICENSE.txt README.txt *.pdf
%_docdir/%name

%changelog
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

