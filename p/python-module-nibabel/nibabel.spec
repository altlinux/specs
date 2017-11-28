%define oname nibabel

%def_enable docs
%def_with python3

Name: python-module-%oname
URL:http://niftilib.sf.net/pynifti/
Summary: Easy access to NIfTI images from within Python
Version: 2.2.1
Release: alt1
License: MIT
BuildArch: noarch
Group: Development/Python

# https://github.com/nipy/nibabel.git
Source: %oname-%version.tar.gz
# https://github.com/yarikoptic/nitest-balls1
Source1: nitest-balls1.tar
# git://github.com/matthew-brett/nitest-minc2.git
Source2: nitest-minc2.tar

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-numpy-testing python-module-nose
BuildRequires: python-module-pydicom python-modules-sqlite3
BuildRequires: python-module-alabaster python-module-html5lib python-module-numpydoc python-module-objects.inv python-module-sphinx-pickles
BuildRequires: python2.7(matplotlib) python2.7(matplotlib.sphinxext.plot_directive) python2.7(texext)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-numpy-testing
%endif

%setup_python_module %oname

%description
NiBabel aims to provide easy access to NIfTI images from within Python.
It uses SWIG-generated wrappers for the NIfTI reference library and
provides the nifti.image.NiftiImage class for Python-style access to the
image data.

While NiBabel is not yet complete (i.e. doesn't support everything the
C library can do), it already provides access to the most important
features of the NIfTI-1 data format and libniftiio capabilities.

%package -n python3-module-%oname
Summary: Easy access to NIfTI images from within Python
Group: Development/Python3

%description -n python3-module-%oname
NiBabel aims to provide easy access to NIfTI images from within Python.
It uses SWIG-generated wrappers for the NIfTI reference library and
provides the nifti.image.NiftiImage class for Python-style access to the
image data.

While NiBabel is not yet complete (i.e. doesn't support everything the
C library can do), it already provides access to the most important
features of the NIfTI-1 data format and libniftiio capabilities.

%package -n python3-module-%oname-tests
Summary: Tests for NiBabel
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
NiBabel aims to provide easy access to NIfTI images from within Python.
It uses SWIG-generated wrappers for the NIfTI reference library and
provides the nifti.image.NiftiImage class for Python-style access to the
image data.

This package contains tests for NiBabel.

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

pushd nibabel-data
tar -xf %SOURCE1
tar -xf %SOURCE2
popd

%if_with python3
cp -R . ../python3
%endif

%if_enabled docs
sed -i 's|@PYVER@|%_python_version|g' doc/Makefile
%prepare_sphinx doc
ln -s ../objects.inv doc/source/
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	2to3 -w -n $i
	mv $i $i.py3
done
popd
%endif

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
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%if_enabled docs
%exclude %python_sitelibdir/%oname/pickle
%endif
%exclude %python_sitelibdir/%oname/testing
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/%oname/*/test*
%exclude %python_sitelibdir/%oname/*/*/test*

%if_enabled docs
%files doc
%_docdir/%oname

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle
%endif

%files tests
%python_sitelibdir/%oname/testing
%python_sitelibdir/*/test*
%python_sitelibdir/%oname/*/test*
%python_sitelibdir/%oname/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc AUTHOR Changelog COPYING
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.1-alt1
- Updated to upstream version 2.2.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.0-alt1.dev.git20141209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.0-alt1.dev.git20141209.1
- NMU: Use buildreq for BR.

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.dev.git20141209
- Version 2.1.0.dev

* Wed Aug 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt4.git20120903
- Added module for Python 3

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt3.git20120903
- New snapshot

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt3.git20120609
- Built with OpenBLAS instead of GotoBLAS2

* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2.git20120609
- Moved all tests into tests subpackage

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

