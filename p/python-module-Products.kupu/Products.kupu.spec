%define oname Products.kupu
Name: python-module-%oname
Version: 1.5.2
Release: alt1
Summary: Cross-browser WYWSIWYG editor
License: BSD & LGPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.kupu/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-i18ndude
BuildPreReq: python-module-plone.outputfilters
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.MimetypesRegistry
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.i18ntestcase
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.untrustedpython

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.outputfilters zope.interface zope.schema zope.i18n
%py_requires zope.i18nmessageid Products.Archetypes Products.CMFCore
%py_requires Products.GenericSetup Products.CMFPlone zope.app.component
%py_requires Products.MimetypesRegistry Products.PortalTransforms

%description
Kupu is a cross-browser WYWSIWYG editor. It allows the comfortable
editing of the body of an HTML document.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.ATContentTypes Products.i18ntestcase
%py_requires Products.PloneTestCase

%description tests
Kupu is a cross-browser WYWSIWYG editor. It allows the comfortable
editing of the body of an HTML document.

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
%python_sitelibdir/Products/kupu
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/kupu/test*
%exclude %python_sitelibdir/Products/kupu/*/test*
%exclude %python_sitelibdir/Products/kupu/*/*/test*

%files tests
%python_sitelibdir/Products/kupu/test*
%python_sitelibdir/Products/kupu/*/test*
%python_sitelibdir/Products/kupu/*/*/test*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1
- Initial build for Sisyphus

