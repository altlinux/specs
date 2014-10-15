%define oname Products.PortalTransforms
Name: python-module-%oname
Version: 2.1.5
Release: alt2.dev0.git20140907
Summary: MIME based content transformations
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PortalTransforms/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.PortalTransforms.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.intelligenttext
BuildPreReq: python-module-zope.structuredtext
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.MimetypesRegistry
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Pillow python-module-markdown
BuildPreReq: python-module-Products.Archetypes

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.intelligenttext zope.interface zope.structuredtext
%py_requires Products.CMFCore Products.CMFDefault ZODB3
%py_requires Products.MimetypesRegistry
%add_python_req_skip com pythoncom pywintypes reStructuredText uno
%add_python_req_skip unohelper win32api win32com

%description
This Zope product provides two new tools for the CMF in order to make
MIME types based transformations on the portal contents, and so an easy
to way to plugin some new transformations for previously unsupported
content types.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing
%py_requires Products.Archetypes
%add_python_req_skip rigging

%description tests
This Zope product provides two new tools for the CMF in order to make
MIME types based transformations on the portal contents, and so an easy
to way to plugin some new transformations for previously unsupported
content types.

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
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.5-alt2.dev0.git20140907
- Added necessary requirements

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.5-alt1.dev0.git20140907
- Initial build for Sisyphus

