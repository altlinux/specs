%define mname p4a
%define oname %mname.subtyper
Name: python-module-%oname
Version: 2.0
Release: alt1.git20130808
Summary: Subtyping framework for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/p4a.subtyper/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/p4a.subtyper.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-p4a.z2utils
BuildPreReq: python-module-p4a.common
BuildPreReq: python-module-plone.app.contentmenu
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.app.annotation
BuildPreReq: python-module-zope.browsermenu
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-nose

%py_provides %oname
Requires: python-module-Zope2
%py_requires p4a.z2utils p4a.common plone.app.contentmenu zope.schema
%py_requires Products.Archetypes Products.CMFCore zope.component
%py_requires Products.CMFDynamicViewFTI Products.statusmessages
%py_requires zope.i18nmessageid zope.interface zope.event
%py_requires zope.annotation zope.app.annotation zope.browsermenu

%description
p4a.subtyper is a subtyping framework for Plone. In this context,
subtyping means to provide additional specific types onto existing
content types. An example to standard Plone would be to have only one
File content type (and no Image content type). The Image content type
would then become a sub-type of the File content type.

It also exposes the possible sub-types for a given object in the content
menu with a sub-types dropdown menu.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase
%py_requires zope.testing zope.component.testing zope.security.testing

%description tests
p4a.subtyper is a subtyping framework for Plone. In this context,
subtyping means to provide additional specific types onto existing
content types. An example to standard Plone would be to have only one
File content type (and no Image content type). The Image content type
would then become a sub-type of the File content type.

It also exposes the possible sub-types for a given object in the content
menu with a sub-types dropdown menu.

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
nosetests

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*
%exclude %python_sitelibdir/%mname/*/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*
%python_sitelibdir/%mname/*/*/tests.*

%changelog
* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20130808
- Initial build for Sisyphus

