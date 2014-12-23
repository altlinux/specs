%define mname collective
%define oname %mname.colorbox
Name: python-module-%oname
Version: 0.1.6
Release: alt1.rc2
Summary: A jQuery plugin that provides lightboxes in Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.colorbox/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2
BuildPreReq: python-module-PasteScript
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
%py_requires %mname

%description
Very useful for creating an image gallery.
This product loads the colorbox plugin for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-Zope2
%py_requires Products.PloneTestCase

%description tests
Very useful for creating an image gallery.
This product loads the colorbox plugin for Plone.

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
rm -fR build
py.test %mname/colorbox/tests.py

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.rc2
- Initial build for Sisyphus

