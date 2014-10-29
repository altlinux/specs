%define oname Products.AROfficeTransforms
Name: python-module-%oname
Version: 0.12
Release: alt1.dev0.svn20120817
Summary: Module to add conversion from office format to HTML in portal_transforms tool
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.AROfficeTransforms
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/Products.AROfficeTransforms/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.MimetypesRegistry
BuildPreReq: python-module-Products.CMFCore-tests
BuildPreReq: python-module-plone.app.upgrade
BuildPreReq: python-module-Products.Archetypes-tests
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
Requires: python-module-Zope2 xlhtml wv xsltproc unzip
Requires: %_bindir/pdftohtml elinks
%py_requires Products.PortalTransforms Products.CMFDefault
%py_requires Products.MimetypesRegistry Products.CMFCore
%py_requires plone.app.upgrade zope.interface

%description
This packages contains new portal_transforms. This version includes the
following transforms :

* MS Excel to html
* MS Word to html
* MS Word to text
* MS Powerpoint to html
* OpenOffice V1 (sxw, sxc, sxi) to html
* OpenOffice V2 / OASIS OpenDocument (odt, odc, odp) to html
* PDF to html
* Zip to Text

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.Archetypes.tests zope.testing
%py_requires zope.component.testing zope.security.testing
%py_requires Products.CMFCore.testing
%add_python_req_skip rigging

%description tests
This packages contains new portal_transforms. This version includes the
following transforms :

* MS Excel to html
* MS Word to html
* MS Word to text
* MS Powerpoint to html
* OpenOffice V1 (sxw, sxc, sxi) to html
* OpenOffice V2 / OASIS OpenDocument (odt, odc, odp) to html
* PDF to html
* Zip to Text

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
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt1.dev0.svn20120817
- Initial build for Sisyphus

