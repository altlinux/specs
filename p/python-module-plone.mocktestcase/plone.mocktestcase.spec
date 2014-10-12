%define oname plone.mocktestcase
Name: python-module-%oname
Version: 1.0
Release: alt1.b4.git20090712
Summary: Mock unit test case based on ``mocker``
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.mocktestcase/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.mocktestcase.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-mocker

%py_provides %oname
%py_requires plone

%description
This package contains a unittest test class based on the one from the
Mocker mock library (http://labix.org/mocker).

This class provides support for registering Zope 3 components
(utilities, adapters, subscription adapters and event handlers) from
mocks and tearing down the global component registry during test
tear-down.

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
%doc *.txt docs/*
%python_sitelibdir/*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.b4.git20090712
- Initial build for Sisyphus

