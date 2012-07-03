%define oname pysparse

%def_enable docs

Name: python-module-%oname
Version: 1.2
Release: alt2.svn20110511.1
Summary: Fast sparse matrix library for Python
License: MIT
Group: Development/Python
Url: http://pysparse.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://pysparse.svn.sourceforge.net/svnroot/pysparse/trunk
Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python rpm-macros-sphinx
BuildPreReq: python-devel libnumpy-devel liblapack-goto-devel
BuildPreReq: gcc-c++ gcc-fortran libsuperlu-devel libsuitesparse-devel
BuildPreReq: python-module-sphinx-devel python-module-Pygments
%setup_python_module %oname

%description
Pysparse is a fast sparse matrix library for Python. It provides several
sparse matrix storage formats and conversion methods. It also implements
a number of iterative solvers, preconditioners, and interfaces to
efficient factorization packages. Both low-level and high-level
interfaces are available, each with different strengths.

%if_enabled docs
%package pickles
Summary: Documentation and examples for Pysparse
Group: Development/Documentation

%description pickles
Pysparse is a fast sparse matrix library for Python. It provides several
sparse matrix storage formats and conversion methods. It also implements
a number of iterative solvers, preconditioners, and interfaces to
efficient factorization packages. Both low-level and high-level
interfaces are available, each with different strengths.

This package contains pickles for Pysparse.

%package doc
Summary: Documentation and examples for Pysparse
Group: Development/Documentation
BuildArch: noarch

%description doc
Pysparse is a fast sparse matrix library for Python. It provides several
sparse matrix storage formats and conversion methods. It also implements
a number of iterative solvers, preconditioners, and interfaces to
efficient factorization packages. Both low-level and high-level
interfaces are available, each with different strengths.

This package contains development documentation and examples for
Pysparse.

%endif

%package tests
Summary: Tests for Pysparse
Group: Development/Python
Requires: %name = %version-%release

%description tests
Pysparse is a fast sparse matrix library for Python. It provides several
sparse matrix storage formats and conversion methods. It also implements
a number of iterative solvers, preconditioners, and interfaces to
efficient factorization packages. Both low-level and high-level
interfaces are available, each with different strengths.

This package contains tests for Pysparse.

%if_enabled docs
%prepare_sphinx
%endif

%prep
%setup
sed -i 's|@PYVER@|%_python_version|g' doc/pysparse/Makefile

%build
%python_build_debug

%install
%python_install

%if_enabled docs

%make_build -C doc/pysparse html

install -d %buildroot%_docdir/%oname/test
install -p -m644 doc/*.pdf %buildroot%_docdir/%oname
cp -fR doc/pysparse/build/html \
	%buildroot%_docdir/%oname/
cp -fR examples %buildroot%_docdir/%oname/
cp -fR doc/pysparse/build/pickle \
	%buildroot%python_sitelibdir/%oname/
%endif
cp -fR test %buildroot%python_sitelibdir/%oname/
touch %buildroot%python_sitelibdir/%oname/test/__init__.py

install -d %buildroot%_includedir/python%_python_version/%oname
install -p -m644 %oname/include/* \
	%buildroot%_includedir/python%_python_version/%oname

%files
%doc CHANGES LICENSE README TODO
%python_sitelibdir/*
%if_enabled docs
%exclude %python_sitelibdir/%oname/pickle
%endif
%exclude %python_sitelibdir/%oname/test
%_includedir/python%_python_version/%oname

%if_enabled docs
%files doc
%doc %_docdir/%oname

%files pickles
%python_sitelibdir/%oname/pickle
%endif

%files tests
%python_sitelibdir/%oname/test

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt2.svn20110511.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.svn20110511
- Enabled docs

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.svn20110511.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20110511
- New snapshot

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20101006.5
- Rebuilt with GotoBLAS2 1.13-alt3

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20101006.4
- Built with GotoBLAS2 instead of ATLAS

* Mon Apr 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20101006.3
- Rebuilt with ATLAS 3.9.35

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20101006.2
- Rebuilt for debuginfo

* Mon Nov 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20101006.1
- Restored headers

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20101006
- New snapshot

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20100610.2
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20100610.1
- Fixed underlinking

* Tue Jul 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20100610
- New snapshot

* Thu Feb 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20090831.4
- Added:
  + pickles package
  + additional documentation in HML into python-module-pysparce-doc
  + tests package

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20090831.3
- Rebuilt with reformed NumPy

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20090831.2
- Rebuilt with SuperLU 4.0

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20090831.1
- Rebuilt with python 2.6

* Mon Sep 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20090831
- Initial build for Sisyphus

