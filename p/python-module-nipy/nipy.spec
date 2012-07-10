%define oname nipy

%def_disable docs

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20120705
Summary: The neuroimaging in python (NIPY) project
License: MIT
Group: Development/Python
Url: http://neuroimaging.scipy.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/nipy/nipy.git
Source: %oname-%version.tar.gz

Requires: %oname-data

BuildPreReq: python-devel python-module-nifti python-module-scipy
BuildPreReq: python-module-sympy liblapack-goto-devel python-module-matplotlib
BuildPreReq: /proc gcc-fortran %oname-data libnumpy-devel sympy
BuildPreReq: python-module-sympy dvipng libniftilib-devel
BuildPreReq: python-module-nibabel python-module-Cython
BuildPreReq: python-module-sphinx-devel python-module-Pygments
BuildPreReq: graphviz ghostscript-utils
%setup_python_module %oname

%description
The neuroimaging in python (NIPY) project is an environment for the
analysis of structural and functional neuroimaging data. It currently
has a full system for general linear modeling of functional magnetic
resonance imaging (fMRI).

%package examples
Summary: Examples for neuroimaging in python (NIPY) project
Group: Development/Documentation
Requires: %name = %version-%release

%description examples
The neuroimaging in python (NIPY) project is an environment for the
analysis of structural and functional neuroimaging data. It currently
has a full system for general linear modeling of functional magnetic
resonance imaging (fMRI).

This package contains examples for NIPY.

%package tests
Summary: Tests for neuroimaging in python (NIPY) project
Group: Development/Python
Requires: %name = %version-%release

%description tests
The neuroimaging in python (NIPY) project is an environment for the
analysis of structural and functional neuroimaging data. It currently
has a full system for general linear modeling of functional magnetic
resonance imaging (fMRI).

This package contains tests for NIPY.

%if_enabled docs

%package docs
Summary: Documentation for neuroimaging in python (NIPY) project
Group: Development/Documentation
BuildArch: noarch

%description docs
The neuroimaging in python (NIPY) project is an environment for the
analysis of structural and functional neuroimaging data. It currently
has a full system for general linear modeling of functional magnetic
resonance imaging (fMRI).

This package contains documentation for NIPY.

%package pickles
Summary: Pickles for neuroimaging in python (NIPY) project
Group: Development/Python

%description pickles
The neuroimaging in python (NIPY) project is an environment for the
analysis of structural and functional neuroimaging data. It currently
has a full system for general linear modeling of functional magnetic
resonance imaging (fMRI).

This package contains pickles for NIPY.

%endif

%prep
%setup

%if_enabled docs
sed -i 's|@PYVER@|%_python_version|g' doc/Makefile
%prepare_sphinx .
%endif

rm -f doc/labs/image_registration.rst

%build
%python_build_debug

%install
%python_install
export PYTHONPATH=%buildroot%python_sitelibdir

mkdir -p ~/.matplotlib
cp %python_sitelibdir/matplotlib/mpl-data/matplotlibrc ~/.matplotlib/
sed -i 's|^\(backend\).*|\1 : PDF|' ~/.matplotlib/matplotlibrc

%if_enabled docs
%make -C doc pickle
%make -C doc html
#make -C doc pdf
%endif

install fff2.py %buildroot%python_sitelibdir
cp -fR examples %buildroot%python_sitelibdir/%oname/

%if_enabled docs
#mkdir -p doc/pdf
#for i in $(find doc -name '*.pdf'); do
#	cp -f $i doc/pdf/
#done

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%files
%doc LICENSE README THANKS
%_bindir/*
%python_sitelibdir/*
%if_enabled docs
%exclude %python_sitelibdir/%oname/pickle
%endif
%exclude %python_sitelibdir/*/examples
%exclude %python_sitelibdir/*/testing
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/testing
%exclude %python_sitelibdir/*/*/*/*/tests
#exclude %python_sitelibdir/*/*/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/test

%if_enabled docs
%files docs
%doc doc/build/html/*
#doc doc/pdf

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle
%endif

%files examples
%python_sitelibdir/*/examples

%files tests
%python_sitelibdir/*/*/*/test
%python_sitelibdir/*/testing
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/testing
%python_sitelibdir/*/*/*/*/tests
#python_sitelibdir/*/*/*/*/*/tests

%changelog
* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20120705
- Version 0.2.0
- Disabled docs (what's wrong in girar-builder?)

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt2.git20110404.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2.git20110404
- Enabled docs (except pdf)

* Tue Nov 15 2011 Dmitry V. Levin <ldv@altlinux.org> 0.1.2-alt1.git20110404.2
- Removed Mayavi from package requirements.

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt1.git20110404.1
- Rebuild with Python-2.7

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20110404
- New snapshot
- Build with GotoBLAS2 instead of ATLAS

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20101104.2
- Rebuilt with python-module-sphinx-devel

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20101104.1
- Rebuilt for debuginfo

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20101104
- New snapshot

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20100828.2
- Fixed underlinking

* Tue Sep 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20100828.1
- Moved all tests into tests package

* Mon Sep 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20100828
- New snapshot
- Fixed build of docs

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20100601
- New snapshot

* Sun Mar 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.bzr20100301
- New snapshot
- Extracted examples and tests into separate packages
- Added docs and pickles packages

* Mon Jan 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.bzr20090924.3
- Rebuilt with new NumPy

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.bzr20090924.2
- Rebuilt with python 2.6

* Fri Oct 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.bzr20090924.1
- Added necessary requitements: nipy-data, python2.x(enthought)

* Fri Sep 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.bzr20090924
- Initial build for Sisyphus

