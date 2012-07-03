%define oname nlpy
Name: python-module-%oname
Version: 20090325
Release: alt6.1
Summary: Python package for numerical optimization
License: LGPL v2.1 or later
Group: Development/Python
Url: http://nlpy.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://nlpy.svn.sourceforge.net/svnroot/nlpy
Source: %oname-%version.tar.gz
Source1: makedefs-path

Requires: libcsrch libicfs libmcsrch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel libcsrch-devel libnumpy-devel
BuildPreReq: python-module-pysparse gcc-c++ gcc-fortran libicfs-devel
BuildPreReq: libmetis-devel libcsrch-devel liblapack-goto-devel
%setup_python_module %oname
%add_python_req_skip amplpy _amplpy

%description
NLPy is a Python package for numerical optimization. Its aim is to
provide a toolbox for solving linear and nonlinear programming problems
that is both easy to use and is extensible. It is applicable to problems
that are smooth, have no derivatives, or have integer data.

%package doc
Summary: Documentation and examples for NLPy
Group: Development/Documentation
BuildArch: noarch

%description doc
NLPy is a Python package for numerical optimization. Its aim is to
provide a toolbox for solving linear and nonlinear programming problems
that is both easy to use and is extensible. It is applicable to problems
that are smooth, have no derivatives, or have integer data.

This package contains documentation and examples for NLPy.

%package -n libmcsrch
Summary: Shared library of Jorge Nocedal's safeguarded modification of CSRCH
Group: System/Libraries

%description -n libmcsrch
MCSRCH is Jorge Nocedal's safeguarded modification of the More and
Thuente linesearch ensuring satisfaction of the strong Wolfe conditions.

%package -n libmcsrch-devel
Summary: Shared library of Jorge Nocedal's safeguarded modification of CSRCH
Group: System/Libraries
Requires: libmcsrch = %version-%release
Requires: %name = %version-%release

%description -n libmcsrch-devel
MCSRCH is Jorge Nocedal's safeguarded modification of the More and
Thuente linesearch ensuring satisfaction of the strong Wolfe conditions.

This package contains development files of MCSRCH.

%prep
%setup
install -m644 %SOURCE1 .

%build
export HOME=$PWD
mkdir Lib
sed -i 's|@PYVER@|%_python_version|g' makedefs-path
sed -i 's|@PYTHON_SITELIBDIR@|%python_sitelibdir|g' makedefs-path Src/Makefile
sed -i 's|@LIBDIR@|%_libdir|g' Src/Makefile

%make_build

%install
install -d %buildroot%python_sitelibdir
install -d %buildroot%_libdir
install -d %buildroot%_includedir/%oname
install -d %buildroot%_docdir/%name

install -m644 Lib/* NLPy/* %buildroot%python_sitelibdir
install -p -m644 Include/* %buildroot%_includedir/%oname
install -p -m644 Doc/pygltr.html Doc/*.pdf %buildroot%_docdir/%name
cp -fR Examples %buildroot%_docdir/%name/

pushd %buildroot%_libdir
mv %buildroot%python_sitelibdir/libmcsrch.so ./libmcsrch.so.0.0.0
ln -s libmcsrch.so.0.0.0 libmcsrch.so.0
ln -s libmcsrch.so.0 libmcsrch.so
popd

%files
%doc COPYING-GLPL FAQ LICENSE TODO
%python_sitelibdir/*
%exclude %python_sitelibdir/utsolve.*
%exclude %python_sitelibdir/slacks.*
%exclude %python_sitelibdir/lib*.so
%_includedir/*

%files doc
%_docdir/%name
%exclude %_docdir/%name/Examples/demo_triangular_sys_python.py

%files -n libmcsrch
%_libdir/*.so.*

%files -n libmcsrch-devel
%_libdir/*.so

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20090325-alt6.1
- Rebuild with Python-2.7

* Wed May 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090325-alt6
- Rebuilt with new pysparse

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090325-alt5
- Built with GotoBLAS2 instead of ATLAS

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090325-alt4
- Rebuilt for debuginfo

* Fri Feb 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090325-alt3
- Rebuilt with reformed NumPy

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090325-alt2
- Rebuilt with python 2.6

* Wed Sep 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090325-alt1
- Initial build for Sisyphus

