%define oname plone.resourceeditor
Name: python-module-%oname
Version: 1.0.1
Release: alt1.dev0.git20140826
Summary: Integrates ACE editor into Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.resourceeditor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.resourceeditor.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.resource
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone zope.interface zope.component zope.publisher
%py_requires zope.schema plone.resource

%description
This package contains resources for integrating ACE (http://ace.ajax.org/)
into Plone, with a file manager that can edit plone.resource resource
directories in the ZODB.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
This package contains resources for integrating ACE (http://ace.ajax.org/)
into Plone, with a file manager that can edit plone.resource resource
directories in the ZODB.

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/test*

%files tests
%python_sitelibdir/plone/*/test*

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.dev0.git20140826
- Initial build for Sisyphus

