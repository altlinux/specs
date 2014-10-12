%define oname Products.CMFCalendar
Name: python-module-%oname
Version: 2.2.3
Release: alt1
Summary: Calendar product for the Zope Content Management Framework
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CMFCalendar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore-tests
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.DCWorkflow
BuildPreReq: python-module-zope.testrunner
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.traversing-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-zope.app.form python-module-eggtestinfo

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore Products.CMFDefault Products.GenericSetup
%py_requires zope.app.form

%description
The CMFCalendar product is an example of creating a CMF Product. The
CMFCalendar product is also expected to be a generally useful out of the
box and skinnable to accomodate customization within your existing CMF
instance. To see how to go about building a CMF product, this hopefully
allows a developer to follow through the process of registering their
product, skins, and help with the CMF by example. It shows how an object
is created and registered with the types_tool, necessary skins added to
the skins_tool, with the Calendar skins directory added to the skin
paths, and providing portal_metadatool with an Element policy for the
content_type of the object.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing Products.DCWorkflow

%description tests
The CMFCalendar product is an example of creating a CMF Product. The
CMFCalendar product is also expected to be a generally useful out of the
box and skinnable to accomodate customization within your existing CMF
instance. To see how to go about building a CMF product, this hopefully
allows a developer to follow through the process of registering their
product, skins, and help with the CMF by example. It shows how an object
is created and registered with the types_tool, necessary skins added to
the skins_tool, with the Calendar skins directory added to the skin
paths, and providing portal_metadatool with an Element policy for the
content_type of the object.

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
%exclude %python_sitelibdir/Products/*/*/test*

%files tests
%python_sitelibdir/Products/*/test*
%python_sitelibdir/Products/*/*/test*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.3-alt1
- Initial build for Sisyphus

