# original spec file get from
# https://opensvn.csie.org/traccgi/pyvault/browser/rpms/trunk/pyfort/pyfort.spec?rev=175
%define origname pyfort

Name:           python-module-%origname
Version:        8.5.5
Release:        alt3.1
Summary:        Python - Fortran Connection Tool
Group:          Development/Python
License:        BSD
URL:            http://pyfortran.sourceforge.net
BuildArch: noarch
# cvs -z3 -d:pserver:anonymous@pyfortran.cvs.sourceforge.net:/cvsroot/pyfortran \
#   co -P pyfort
Source:        %origname-%version.tar.gz
Source1: http://pyfortran.sourceforge.net/pyfort/pyfort_reference.pdf
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires(pre): rpm-build-python
BuildPreReq: gcc-fortran python-devel
%setup_python_module Pyfort
%py_provides Pyfort

%description
Pyfort is a tool for creating extensions to the Python language with Fortran
routines. It supports F77-interfaced routines now, with plans for supporting
more of F90 later.

%package doc
Summary: Pyfort reference manual
BuildArch: noarch
Group: Development/Documentation

%description doc
Pyfort reference manual.

%prep
%setup -n %origname-%version
cp %SOURCE1 ./

%build
%python_build

%install
%python_install --optimize=2

mkdir -pv %buildroot%_docdir/Pyfort
mv *.pdf %buildroot%_docdir/Pyfort/

%files
%doc README
%_bindir/*
%python_sitelibdir/*

%files doc
%_docdir/Pyfort

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 8.5.5-alt3.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.5.5-alt3
- Rebuilt with python 2.6

* Sun Jul 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.5.5-alt2
- Rebuild as noarch package

* Mon Mar 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.5.5-alt1
- Initial build for Sisyphus

* Sat Jan 22 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 8.5.1-1
- new rpm

