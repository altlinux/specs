%define oname feval
Name: python-module-%oname
Version: 0.2
Release: alt3.1
Summary: Python Finite Element Evaluator
License: GPL
Group: Development/Python
Url: http://feval.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn checkout svn://svn.berlios.de/feval/trunk feval
Source: %oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-numpy gcc-fortran
%setup_python_module %oname

%description
FEVal, the Finite Element Evaluator written in Python, provides easy conversion
for many Finite Element data formats (both binary and ascii). Mesh modification
is very easy. Values of model results can be accessed given coordinates in
physical space.

%package doc
Summary: Documentation for Finite Element Evaluator (FEVal)
Group: Development/Documentation

%description doc
FEVal, the Finite Element Evaluator written in Python, provides easy conversion
for many Finite Element data formats (both binary and ascii). Mesh modification
is very easy. Values of model results can be accessed given coordinates in
physical space.

This package contains documentation for FEVal.

%package examples
Summary: Examples for Finite Element Evaluator (FEVal)
Group: Development/Documentation
Requires: %name = %version-%release

%description examples
FEVal, the Finite Element Evaluator written in Python, provides easy conversion
for many Finite Element data formats (both binary and ascii). Mesh modification
is very easy. Values of model results can be accessed given coordinates in
physical space.

This package contains examples for FEVal.

%prep
%setup

%build
%python_build

%install
%python_install

install -d %buildroot%python_sitelibdir/%oname/examples
install -d %buildroot%_docdir/%oname

install -p -m644 examples/* \
	%buildroot%python_sitelibdir/%oname/examples
install -p -m644 doc/%oname.ps %buildroot%_docdir/%oname
cp -fR data %buildroot%python_sitelibdir/%oname/

%files
%doc README COPYING
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/examples
%exclude %python_sitelibdir/%oname/data

%files doc
%_docdir/%oname

%files examples
%python_sitelibdir/%oname/examples
%python_sitelibdir/%oname/data

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt3.1
- Rebuild with Python-2.7

* Mon Dec 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Rebuilt without python-module-Numeric

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Rebuilt with python 2.6

* Sun Sep 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

