%define oname pythonequations
%define svnrev 334
Name: python-module-%oname
Version: 25.4
Release: alt1.svn20111127
Summary: A collection of Python equations

Group: Development/Python
License: BSD
URL: http://code.google.com/p/pythonequations/
# http://pythonequations.googlecode.com/svn/trunk
Source: %oname-%version.tar.gz
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-devel

%description
The middleware for http://zunzun.com as a collection of Python equations
that can fit themselves to both 2D and 3D data sets (curve fitting and
surface fitting), output source code in several computing languages, and
run a genetic algorithm for initial parameter estimation.

%prep
%setup
sed -i 's|@SVNREV@|%svnrev|' __init__.py

%install
install -d %buildroot%python_sitelibdir/%oname
cp -fR * %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/*.txt

%changelog
* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 25.4-alt1.svn20111127
- Version 25.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 23.5-alt1.svn20110511.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 23.5-alt1.svn20110511
- Version 23.5

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 22.0-alt1.svn20101119
- Version 22.0

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20.2-alt1.svn20100725
- Version 20.2

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.3-alt1.svn20091007.1
- Rebuilt with python 2.6

* Thu Oct 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.3-alt1.svn20091007
- Initial build for Sisyphus

