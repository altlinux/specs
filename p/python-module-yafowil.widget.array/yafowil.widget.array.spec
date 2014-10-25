%define mname yafowil.widget
%define oname %mname.array
Name: python-module-%oname
Version: 1.2.1
Release: alt1.git20140803
Summary: Array Widget for YAFOWIL
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/yafowil.widget.array/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bluedynamics/yafowil.widget.array.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-yafowil-tests

%py_provides %oname
Requires: python-module-%mname = %EVR

%description
This is an array widget for for YAFOWIL.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires yafowil.tests

%description tests
This is an array widget for for YAFOWIL.

This package contains tests for %oname

%package -n python-module-%mname
Summary: Core files for %mname
Group: Development/Python
%py_provides %mname
%py_requires yafowil

%description -n python-module-%mname
Core files for %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/yafowil/widget/__init__.py \
	%buildroot%python_sitelibdir/yafowil/widget/

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/yafowil/widget/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/yafowil/widget/*/tests.*
%exclude %python_sitelibdir/yafowil/widget/__init__.py*

%files tests
%python_sitelibdir/yafowil/widget/*/tests.*

%files -n python-module-%mname
%dir %python_sitelibdir/yafowil/widget
%python_sitelibdir/yafowil/widget/__init__.py*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.git20140803
- Initial build for Sisyphus

