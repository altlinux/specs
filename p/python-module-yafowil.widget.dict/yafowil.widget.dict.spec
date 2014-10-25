%define mname yafowil.widget
%define oname %mname.dict
Name: python-module-%oname
Version: 1.5
Release: alt1.dev0.git20140806
Summary: Dict/Mapping Widget for YAFOWIL
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/yafowil.widget.dict/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bluedynamics/yafowil.widget.dict.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-yafowil-tests

%py_provides %oname
%py_requires %mname

%description
This is a dictionary widget for for YAFOWIL - Yet Another Form Widget
Library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires yafowil.tests

%description tests
This is a dictionary widget for for YAFOWIL - Yet Another Form Widget
Library.

This package contains tests for %oname

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/yafowil/widget/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/yafowil/widget/*/tests.*

%files tests
%python_sitelibdir/yafowil/widget/*/tests.*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.dev0.git20140806
- Initial build for Sisyphus

