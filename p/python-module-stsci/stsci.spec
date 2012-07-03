%define oname stsci

%def_enable docs

Name: python-module-%oname
Version: 2.12
Release: alt3.1
Summary: Python packages for a general astronomical data analysis infrastructure
License: BSD
Group: Sciences/Mathematics
Url: http://www.stsci.edu/resources/software_hardware/pyraf/stsci_python/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: stsci_python_%version.tar
#Source1: calcos.tar

BuildRequires(pre): rpm-build-python
%setup_python_module %oname
BuildPreReq: gcc-fortran libnumpy-devel libX11-devel xorg-xproto-devel
BuildPreReq: python-module-sphinx-devel
BuildPreReq: Mayavi
%add_python_req_skip AppKit numarray objc scipy_distutils

%description
STSCI_PYTHON is a collection of Python packages (with C extensions)
that has been developed to provide a general astronomical data analysis
infrastructure. They can be used standalone from within Python or as
Python tasks that are accessible from within STSDAS whens running under
PyRAF.

STSCI_PYTHON is developed by the Science Software Branch at the Space
Telescope Science Institute.

%package tests
Summary: Tests for STSCI_PYTHON
Group: Development/Python
Requires: %name = %version-%release
%py_requires nose

%description tests
STSCI_PYTHON is a collection of Python packages (with C extensions)
that has been developed to provide a general astronomical data analysis
infrastructure. They can be used standalone from within Python or as
Python tasks that are accessible from within STSDAS whens running under
PyRAF.

STSCI_PYTHON is developed by the Science Software Branch at the Space
Telescope Science Institute.

This package contains tests for STSCI_PYTHON.

%if_enabled docs

%package pickles
Summary: Pickles for STSCI
Group: Development/Python

%description pickles
STSCI_PYTHON is a collection of Python packages (with C extensions)
that has been developed to provide a general astronomical data analysis
infrastructure. They can be used standalone from within Python or as
Python tasks that are accessible from within STSDAS whens running under
PyRAF.

STSCI_PYTHON is developed by the Science Software Branch at the Space
Telescope Science Institute.

This package contains pickles for STSCI_PYTHON.

%package docs
Summary: Documentation for STSCI
Group: Development/Documentation
BuildArch: noarch

%description docs
STSCI_PYTHON is a collection of Python packages (with C extensions)
that has been developed to provide a general astronomical data analysis
infrastructure. They can be used standalone from within Python or as
Python tasks that are accessible from within STSDAS whens running under
PyRAF.

STSCI_PYTHON is developed by the Science Software Branch at the Space
Telescope Science Institute.

This package contains documentation for STSCI_PYTHON.

%endif

%prep
%setup

#tar -xf %SOURCE1
%if_enabled docs
%prepare_sphinx .
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

export STSCI_PYTHON=%buildroot%python_sitelibdir
export PYTHONPATH=%buildroot%python_sitelibdir
pushd calcos
%python_build_install
popd

#cp -f numpy-1.3.0/doc/source/conf.py $PWD
cp -f $PWD/pywcs/doc/source/conf.py %buildroot%python_sitelibdir
install -d %buildroot%python_sitelibdir/stsci
%if_enabled docs
%generate_pickles %buildroot%python_sitelibdir $PWD/pywcs/doc/source stsci
cp -fR pickle %buildroot%python_sitelibdir/stsci
%endif
rm -f %buildroot%python_sitelibdir/conf.py

%files
%doc RELEASE_NOTES
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/test*
%if_enabled docs
%exclude %python_sitelibdir/stsci/pickle
%endif

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/test*

%if_enabled docs
%files pickles
%dir %python_sitelibdir/stsci
%python_sitelibdir/stsci/pickle

#files docs
#doc stscidocs/docs/*
%endif

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.12-alt3.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Dec 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12-alt3
- Moved all tests into tests subpackage

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12-alt2
- Fixed using of _pytpm

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12-alt1
- Version 2.12

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.11-alt2
- Enabled docs

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.11-alt1.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.11-alt1
- Version 2.11

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10-alt4
- Rebuilt with python-module-sphinx-devel

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10-alt3
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10-alt2
- Fixed underlinking

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10-alt1
- Version 2.10
- Added tests

* Thu Apr 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt1
- Initial build for Sisyphus

