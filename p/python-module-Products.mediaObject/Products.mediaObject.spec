%define oname Products.mediaObject
Name: python-module-%oname
Version: 0.1
Release: alt1.git20141113
Summary: Information about a collectible object used by museums
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.mediaObject
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/intk/Products.mediaObject.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-PasteDeploy python-module-PasteScript
BuildPreReq: python-module-unittest2 python-module-argparse
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.directives
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires paste.script paste.deploy plone.app.dexterity zope.schema
%py_requires plone.namedfile plone.dexterity plone.directives z3c.form
%py_requires plone.app.textfield zope.i18nmessageid zope.interface

%description
Dexterity type that stores information about a collectible object used
by museums.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Dexterity type that stores information about a collectible object used
by museums.

This package contains tests for %oname.

%prep
%setup

rm -fR build dist Paste*

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

pushd Products/mediaObject
cp -fR configure.zcml locales models \
	object_templates profiles resources \
	%buildroot%python_sitelibdir/Products/mediaObject/
popd

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests.*

%files tests
%python_sitelibdir/Products/*/tests.*

%changelog
* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141113
- Initial build for Sisyphus

