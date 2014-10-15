%define oname Products.ExternalEditor
Name: python-module-%oname
Version: 1.1.0
Release: alt1
Summary: Zope External Editor
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ExternalEditor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests

%py_provides %oname
Requires: python-module-Zope2

%description
The Zope External Editor is a new way to integrate Zope more seamlessly
with client-side tools.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The Zope External Editor is a new way to integrate Zope more seamlessly
with client-side tools.

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

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

