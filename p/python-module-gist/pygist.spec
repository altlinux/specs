BuildRequires(pre): rpm-build-python

%define oname gist
%define gistpath %python_sitelibdir/%oname/g

Name: python-module-%oname
Version: 1.5.28
%define cflags %optflags %optflags_shared -I%_builddir/%name-%version/src/gist
Release: alt6.1.1
Summary: Scientific graphics (plotting) library
License: Free for non-commercial using
Group: Development/Python
Url: http://hifweb.lbl.gov/public/software/gist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://hifweb.lbl.gov/public/software/gist/pygist-1.5.28.tar.gz
Source1: http://hifweb.lbl.gov/public/software/gist/pygist.pdf
Source2: sigfpe.h

BuildPreReq: python-devel libX11-devel libreadline-devel
BuildPreReq: libnumpy-devel liblapack-goto-devel
BuildPreReq: python-module-arrayfns
%setup_python_module %oname
%py_requires numpy

%description
Gist is a scientific graphics library written by David H. Munro of
Lawrence Livermore National Laboratory. It produces x-vs-y plots, 2-D
quadrilateral mesh plots with contours, filled contours, vector fields,
or pseudocolor maps on such meshes. Some 3-D plot capabilities are also
available.

%package tests
Summary: Tests for Gist
Group: Development/Python

%description tests
Gist is a scientific graphics library written by David H. Munro of
Lawrence Livermore National Laboratory. It produces x-vs-y plots, 2-D
quadrilateral mesh plots with contours, filled contours, vector fields,
or pseudocolor maps on such meshes. Some 3-D plot capabilities are also
available.

This package contains tests and demos for Gist.

%package doc
Summary: Documentation for Gist
Group: Documentation
BuildArch: noarch

%description doc
Gist is a scientific graphics library written by David H. Munro of
Lawrence Livermore National Laboratory. It produces x-vs-y plots, 2-D
quadrilateral mesh plots with contours, filled contours, vector fields,
or pseudocolor maps on such meshes. Some 3-D plot capabilities are also
available.

This package contains documentation for Gist.

%prep
%setup
sed -i 's|@PYVER@|%__python_version|g' src/Makepyg
sed -i 's|@GISTPATH@|%gistpath|g' \
	src/gist/Makefile \
	src/Makefile.gist \
	src/gist/gread.c \
	setup.py

#cp src/play/unix/config.h src/play/unix/gist_config.h
install -m644 %SOURCE2 src/gist

%build
ln VERSION src

python setup.py config
%add_optflags %cflags -DFPU_GCC_I86
%python_build_debug

LGIST=$(find $PWD -name 'gistC.so')
sed -i "s|@LGIST@|$LGIST|g" src/gist/Makefile src/Makefile.gist
pushd src
export CFLAGS="%cflags -DFPU_GCC_I86"
export CPPFLAGS=$CFLAGS
%make_build Y_SITE=%buildroot%prefix ysite
%make_build config
%make_build
popd

%install
export CFLAGS="%cflags"
%python_install
pushd src
%makeinstall_std
popd

install -d %buildroot%gistpath
mv %buildroot%prefix/g/* %buildroot%gistpath/

install -d %buildroot%_docdir/%name
install -p -m644 %SOURCE1 %buildroot%_docdir/%name
mv %buildroot%_includedir/config.h \
	%buildroot%_includedir/gist_config.h

%files
%doc ChangeLog HISTORY NOTES.developer README RELEASE release.msg
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/*test*
%_bindir/%oname
%_includedir/*

%files tests
%python_sitelibdir/%oname/*test*

%files doc
%_docdir/%name

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.28-alt6.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.28-alt6.1
- Rebuild with Python-2.7

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.28-alt6
- Built with GotoBLAS2 instead of ATLAS

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.28-alt5
- Rebuilt for debuginfo

* Sun Mar 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.28-alt4
- Rebuilt without python-module-Numeric
- Extracted tests into separate package

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.28-alt3
- Rebuilt with python 2.6

* Tue Sep 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.28-alt2
- Avoided file conflict with libbobpp-devel

* Mon Sep 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.28-alt1
- Initial build for Sisyphus

