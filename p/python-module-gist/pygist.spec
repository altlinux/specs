BuildRequires(pre): rpm-build-python

%define oname gist
%define gistpath %python_sitelibdir/%oname/g

%def_with python3
%define gistpath3 %python3_sitelibdir/%oname/g

Name: python-module-%oname
Version: 2.2.0
%define cflags %optflags %optflags_shared -I%_builddir/%name-%version/src/gist
Release: alt2.git20130422.1
Summary: Scientific graphics (plotting) library
License: Free for non-commercial using
Group: Development/Python
Url: http://hifweb.lbl.gov/public/software/gist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://portal.nersc.gov/project/warp/git/pygist.git
Source: pygist-%version.tar.gz
Source1: http://hifweb.lbl.gov/public/software/gist/pygist.pdf
Source2: sigfpe.h

#BuildPreReq: python-devel libX11-devel libreadline-devel
#BuildPreReq: libnumpy-devel liblapack-devel
#BuildPreReq: python-module-arrayfns
%setup_python_module %oname
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel
#BuildPreReq: libnumpy-py3-devel
%endif

%py_requires numpy

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-numpy python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-numpy xorg-xproto-devel
BuildRequires: libX11-devel libnumpy-devel python-module-numpy-testing python3-devel python3-module-numpy-testing rpm-build-python3

%description
Gist is a scientific graphics library written by David H. Munro of
Lawrence Livermore National Laboratory. It produces x-vs-y plots, 2-D
quadrilateral mesh plots with contours, filled contours, vector fields,
or pseudocolor maps on such meshes. Some 3-D plot capabilities are also
available.

%package -n python3-module-%oname
Summary: Scientific graphics (plotting) library
Group: Development/Python3
%py3_requires numpy
%add_python3_req_skip arrayfns

%description -n python3-module-%oname
Gist is a scientific graphics library written by David H. Munro of
Lawrence Livermore National Laboratory. It produces x-vs-y plots, 2-D
quadrilateral mesh plots with contours, filled contours, vector fields,
or pseudocolor maps on such meshes. Some 3-D plot capabilities are also
available.

%package -n python3-module-%oname-tests
Summary: Tests for Gist
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Gist is a scientific graphics library written by David H. Munro of
Lawrence Livermore National Laboratory. It produces x-vs-y plots, 2-D
quadrilateral mesh plots with contours, filled contours, vector fields,
or pseudocolor maps on such meshes. Some 3-D plot capabilities are also
available.

This package contains tests and demos for Gist.

%package tests
Summary: Tests for Gist
Group: Development/Python
Requires: %name = %EVR

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
install -m644 %SOURCE2 src/gist

%if_with python3
cp -fR . ../python3
pushd ../python3
sed -i 's|@PYVER@|%_python3_version%_python3_abiflags|g' \
	src/Makepyg setup.py
sed -i 's|@GISTPATH@|%gistpath3|g' \
	src/gist/Makefile \
	src/Makefile.gist \
	src/gist/gread.c \
	setup.py
sed -i 's|@BUILDROOT@|%buildroot|' setup.py
popd
%endif

sed -i 's|@PYVER@|%_python_version|g' src/Makepyg setup.py
sed -i 's|@GISTPATH@|%gistpath|g' \
	src/gist/Makefile \
	src/Makefile.gist \
	src/gist/gread.c \
	setup.py
sed -i 's|@BUILDROOT@|%buildroot|' setup.py


%build
ln VERSION src

python setup.py config
%add_optflags %cflags -DFPU_GCC_I86
%python_build_debug

pushd src
export CFLAGS="%cflags -DFPU_GCC_I86"
export CPPFLAGS=$CFLAGS
%make_build Y_SITE=%buildroot%gistpath ysite
%make_build config
%make_build
popd

%if_with python3
pushd ../python3
ln VERSION src

python3 setup.py config
%python3_build_debug

pushd src
export CFLAGS="%cflags -DFPU_GCC_I86"
export CPPFLAGS=$CFLAGS
%make_build Y_SITE=%buildroot%gistpath3 ysite
%make_build config
%make_build
popd
popd
%endif

%install
export CFLAGS="%cflags"

%if_with python3
pushd ../python3
%python3_install
pushd src
%makeinstall_std
popd
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
pushd src
%makeinstall_std
popd

install -d %buildroot%_docdir/%name
install -p -m644 %SOURCE1 %buildroot%_docdir/%name

pushd %buildroot%python_sitelibdir/gist/g/include
mv config.h gist_config.h
install -d  %buildroot%_includedir
for i in $(ls); do
	mv $i %buildroot%_includedir/
	ln -s %_includedir/$i ./
done
popd

%files
%doc ChangeLog HISTORY NOTES.developer README RELEASE release.msg
%python_sitelibdir/*
#exclude %python_sitelibdir/%oname/*test*
%_bindir/%oname
%_includedir/*

#files tests
#python_sitelibdir/%oname/*test*

%files doc
%_docdir/%name

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog HISTORY NOTES.developer README RELEASE release.msg
%python3_sitelibdir/*
#exclude %python3_sitelibdir/%oname/*test*
%_bindir/%oname.py3
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.2.0-alt2.git20130422.1
- NMU: Use buildreq for BR.

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt2.git20130422
- Added module for Python 3

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.git20130422
- New snapshot

* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.git20121210
- Version 2.2.0

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.28-alt7
- Built with OpenBLAS instead of GotoBLAS2

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

