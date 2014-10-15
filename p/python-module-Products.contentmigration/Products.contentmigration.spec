%define oname Products.contentmigration
Name: python-module-%oname
Version: 2.1.10
Release: alt2.dev0.git20140907
Summary: A generic content migration framework for Plone
License: LGPL
Group: Development/Python
Url: http://crd.lbl.gov/~dhbailey/mpdist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.contentmigration.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires archetypes.schemaextender

%description
This is a generic content migration framework, which should help you
write your own content migrations. It has no UI and no value on its own,
but makes it easy to write certain type of content migrations.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase Products.CMFPlone

%description tests
This is a generic content migration framework, which should help you
write your own content migrations. It has no UI and no value on its own,
but makes it easy to write certain type of content migrations.

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
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/test*

%files tests
%python_sitelibdir/Products/*/test*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.10-alt2.dev0.git20140907
- Added necessary requirements

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.10-alt1.dev0.git20140907
- Initial build for Sisyphus

