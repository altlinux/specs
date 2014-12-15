%define oname plone.namedfile
Name: python-module-%oname
Version: 3.0.2
Release: alt1.dev0.git20141023
Summary: File types and fields for images, files and blob files with filenames
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.namedfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.namedfile.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.browserpage python-module-lxml
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-plone.rfc822
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.scale
BuildPreReq: python-module-plone.schemaeditor

%py_provides %oname
%py_requires plone zope.browserpage zope.component zope.security
%py_requires zope.traversing plone.rfc822
%py_requires plone.supermodel plone.scale
%py_requires plone.schemaeditor

%description
This package contains fields and wrapper objects for storing:

* A file with a filename
* An image with a filename

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains fields and wrapper objects for storing:

* A file with a filename
* An image with a filename

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
%doc *.rst docs/*
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests

%files tests
%python_sitelibdir/plone/*/tests

%changelog
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt1.dev0.git20141023
- Version 3.0.2.dev0

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt2.dev0.git20141007
- Added necessary requirements

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.dev0.git20141007
- Initial build for Sisyphus

