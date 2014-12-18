%define mname p4a
%define oname %mname.fileimage
Name: python-module-%oname
Version: 1.0.2
Release: alt1
Summary: File/Image widget for Zope 3
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/p4a.fileimage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.app.form
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.cachedescriptors
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname zope.component zope.schema zope.app.form
%py_requires zope.interface zope.cachedescriptors

%description
p4a.file is a field/widget pair for handling fields that contain binary
data.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.testing

%description tests
p4a.file is a field/widget pair for handling fields that contain binary
data.

This package contains tests for %oname.

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
py.test p4a/fileimage/tests.py

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Thu Dec 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

