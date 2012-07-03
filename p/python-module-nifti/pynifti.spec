%def_enable docs

%define oname nifti
Name: python-module-%oname
URL:http://niftilib.sf.net/pynifti/
Summary: Python interface to the NIfTI I/O libraries
Version: 0.20090303.2
Release: alt3.git20090924
License: MIT
Group: Development/Python

# git://git.debian.org/git/pkg-exppsy/pynifti.gi
Source: py%oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: libnumpy-devel libatlas-devel liblapack-devel
BuildRequires: python-devel swig libniftilib-devel zlib-devel
BuildRequires: gcc-c++

%if_enabled docs
BuildPreReq: python-module-sphinx-devel python-module-Pygments
%endif

%setup_python_module %oname

%description
Using PyNIfTI one can easily read and write NIfTI and ANALYZE images
from within Python. The NiftiImage class provides Python-style access to
the full header information. Image data is made available via NumPy
arrays.

%if_enabled docs

%package doc
Summary: Documentation and examples for PyNIfTI
Group: Development/Documentation
BuildArch: noarch

%description doc
Using PyNIfTI one can easily read and write NIfTI and ANALYZE images
from within Python. The NiftiImage class provides Python-style access to
the full header information. Image data is made available via NumPy
arrays.

This package contains documentation and examples for PyNIfTI.

%package pickles
Summary: Pickles for PyNIfTI
Group: Development/Python

%description pickles
Using PyNIfTI one can easily read and write NIfTI and ANALYZE images
from within Python. The NiftiImage class provides Python-style access to
the full header information. Image data is made available via NumPy
arrays.

This package contains pickles for PyNIfTI.

%endif

%prep
%setup

sed -i 's|@PYVER@|%_python_version|g' doc/Makefile setup.py
%if_enabled docs
%prepare_sphinx doc
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

export PYTHONPATH=$(find $PWD -name _clib.so|sed 's|/%oname/_clib.so||')

%if_enabled docs
pushd doc
%make html
popd
%endif

%install
%python_install --prefix=%prefix --record=INSTALLED_FILES

install -d %buildroot%_docdir/py%oname
install -d %buildroot%_man1dir
install -d %buildroot%python_sitelibdir/%oname

%if_enabled docs
cp -fR build/html tests/data/* doc/examples.txt \
	%buildroot%_docdir/py%oname/
cp -fR build/pickle %buildroot%python_sitelibdir/%oname/
install -m644 man/* %buildroot%_man1dir
%endif

%files -f INSTALLED_FILES
%doc AUTHOR Changelog COPYING TODO
%_bindir/*
%if_enabled docs
%_man1dir/*
%exclude %python_sitelibdir/%oname/pickle
%endif
%python_sitelibdir/*

%if_enabled docs
%files doc
%_docdir/py%oname

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle
%endif

%changelog
* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20090303.2-alt3.git20090924
- Fixed build

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.20090303.2-alt2.git20090924.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20090303.2-alt2.git20090924
- Enabled docs (except pdf)

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.20090303.2-alt1.git20090924.6.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20090303.2-alt1.git20090924.6
- Rebuilt with python-module-sphinx-devel

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20090303.2-alt1.git20090924.5
- Rebuilt for debuginfo

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20090303.2-alt1.git20090924.4
- Rebuilt with niftilib 0.20100720

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20090303.2-alt1.git20090924.3
- Fixed underlinking

* Fri Mar 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20090303.2-alt1.git20090924.2
- Rebuilt with reformed NumPy
- Added pickles package

* Mon Jan 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20090303.1-alt1.git20090924.2
- Rebuilt with new NumPy

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20090303.1-alt1.git20090924.1
- Rebuilt with python 2.6

* Fri Sep 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20090303.1-alt1.git20090924
- Initial build for Sisyphus

* Tue Mar 3 2009 - Michael Hanke <michael.hanke@gmail.com> - 0.20090303.1-1
  New bugfix release.

* Thu Feb 5 2009 - Michael Hanke <michael.hanke@gmail.com> - 0.20090205.1-1
  New upstream version.

* Fri Oct 17 2008 - Michael Hanke <michael.hanke@gmail.com> - 0.20081017.1-1
  New upstream version.

* Sat Oct 4 2008 - Michael Hanke <michael.hanke@gmail.com> - 0.20080710.1-1
- Initial release
