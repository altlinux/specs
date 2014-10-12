%define oname plone.supermodel
Name: python-module-%oname
Version: 1.2.6
Release: alt1.dev0.git20141012
Summary: Serialize Zope schema definitions to and from XML
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.supermodel/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.supermodel.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.schema python-module-lxml
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.deferredimport
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-z3c.zcmlhook
BuildPreReq: python-module-plone.rfc822

%py_provides %oname
%py_requires plone zope.schema zope.component zope.i18nmessageid
%py_requires zope.interface zope.deferredimport zope.dottedname
%py_requires z3c.zcmlhook plone.rfc822

%description
plone.supermodel provides XML import and export for schema interfaces
based on zope.schema fields.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
plone.supermodel provides XML import and export for schema interfaces
based on zope.schema fields.

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
%exclude %python_sitelibdir/plone/*/tests.*

%files tests
%python_sitelibdir/plone/*/tests.*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt1.dev0.git20141012
- Initial build for Sisyphus

