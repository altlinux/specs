%define mname ftw.publisher
%define oname %mname.receiver
Name: python-module-%oname
Version: 2.0.4
Release: alt1.dev0.git20141208
Summary: Staging and publishing addon for Plone contents
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.publisher.receiver/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.publisher.receiver.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Plone python-module-openid
BuildPreReq: python-module-ftw.publisher.core
BuildPreReq: python-module-Products.PloneFormGen
BuildPreReq: python-module-collective.testcaselayer
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.app.uuid
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname ftw.publisher.core Plone Products.PloneFormGen
%py_requires Products.CMFPlone Products.Archetypes plone.uuid zope.event
%py_requires plone.app.uuid plone.app.blob zope.component zope.interface
%py_requires zope.publisher zope.lifecycleevent

%description
The ftw.publisher packages provide tools for publishing plone contents
from one instance to another.

This package should be installed on the receiver instance. It provides
tools for unserializing publishing requests and creating, updating or
deleting objects.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires collective.testcaselayer Products.PloneTestCase

%description tests
The ftw.publisher packages provide tools for publishing plone contents
from one instance to another.

This package should be installed on the receiver instance. It provides
tools for unserializing publishing requests and creating, updating or
deleting objects.

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
%python_sitelibdir/ftw/publisher/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/ftw/publisher/*/test*

%files tests
%python_sitelibdir/ftw/publisher/*/test*

%changelog
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1.dev0.git20141208
- Initial build for Sisyphus

