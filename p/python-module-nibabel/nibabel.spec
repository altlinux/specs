%define oname nibabel

%def_enable docs

Name: python-module-%oname
URL:http://niftilib.sf.net/pynifti/
Summary: Easy access to NIfTI images from within Python
Version: 1.3.0
Release: alt1.git20120609
License: MIT
Group: Development/Python

# http://anonscm.debian.org/git/pkg-exppsy/pynifti.git
Source: %oname-%version.tar.gz
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: libnumpy-devel liblapack-goto-devel python-module-nose
BuildRequires: python-devel swig libniftilib-devel zlib-devel
BuildRequires: gcc-c++ python-module-sphinx-devel python-module-Pygments
BuildPreReq: python-module-pydicom
%setup_python_module %oname

%description
NiBabel aims to provide easy access to NIfTI images from within Python.
It uses SWIG-generated wrappers for the NIfTI reference library and
provides the nifti.image.NiftiImage class for Python-style access to the
image data.

While NiBabel is not yet complete (i.e. doesn't support everything the
C library can do), it already provides access to the most important
features of the NIfTI-1 data format and libniftiio capabilities.

%package tests
Summary: Tests for NiBabel
Group: Development/Python
Requires: %name = %version-%release

%description tests
NiBabel aims to provide easy access to NIfTI images from within Python.
It uses SWIG-generated wrappers for the NIfTI reference library and
provides the nifti.image.NiftiImage class for Python-style access to the
image data.

This package contains tests for NiBabel.

%if_enabled docs

%package doc
Summary: Documentation and examples for NiBabel
Group: Development/Documentation
BuildArch: noarch

%description doc
NiBabel aims to provide easy access to NIfTI images from within Python.
It uses SWIG-generated wrappers for the NIfTI reference library and
provides the nifti.image.NiftiImage class for Python-style access to the
image data.

This package contains documentation and examples for NiBabel.

%package pickles
Summary: Pickles for NiBabel
Group: Development/Python

%description pickles
NiBabel aims to provide easy access to NIfTI images from within Python.
It uses SWIG-generated wrappers for the NIfTI reference library and
provides the nifti.image.NiftiImage class for Python-style access to the
image data.

This package contains pickles for NiBabel.

%endif

%prep
%setup

%if_enabled docs
sed -i 's|@PYVER@|%_python_version|g' doc/Makefile
%prepare_sphinx .
%endif

%build
%python_build

%install
%python_install

%if_enabled docs
cp -f doc/source/conf.py %buildroot%python_sitelibdir
export PYTHONPATH=%buildroot%python_sitelibdir
pushd doc
%make html
popd

#install -d %buildroot%_docdir/%oname/pdf
install -d %buildroot%_docdir/%oname
cp -fR build/html %buildroot%_docdir/%oname/
#install -m644 build/latex/*.pdf %buildroot%_docdir/%oname/pdf
cp -fR build/pickle %buildroot%python_sitelibdir/%oname/
%endif

rm -f %buildroot%python_sitelibdir/conf.py

%files
%doc AUTHOR Changelog COPYING
%_bindir/*
%python_sitelibdir/*
%if_enabled docs
%exclude %python_sitelibdir/%oname/pickle
%endif
%exclude %python_sitelibdir/%oname/testing
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/nicom/tests
%exclude %python_sitelibdir/nisext/test*

%if_enabled docs
%files doc
%_docdir/%oname

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle
%endif

%files tests
%python_sitelibdir/%oname/testing
%python_sitelibdir/%oname/tests
%python_sitelibdir/%oname/nicom/tests
%python_sitelibdir/nisext/test*

%changelog
* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20120609
- Version 1.3.0

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.git20101014
- Enabled docs (except pdf)

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.git20101014.1
- Rebuild with Python-2.7

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20101014
- New snapshot

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100725.2
- Rebuilt with python-module-sphinx-devel

* Wed Aug 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100725.1
- Excluded %oname/dicom/tests

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100725
- New snapshot

* Fri Apr 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100326.2
- Rebuilt

* Fri Apr 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100326.1
- Fixed build error

* Wed Mar 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100326
- New snapshot

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100203
- Initial build for Sisyphus

