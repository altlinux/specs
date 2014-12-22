%define mname zopyx
%define oname %mname.existdb
Name: python-module-%oname
Version: 0.2.11.1
Release: alt1
Summary: Plone-ExistDB integration
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/zopyx.existdb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-humanize python-module-requests
BuildPreReq: python-module-fs python-module-dexml
BuildPreReq: python-module-openid
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-hurry.filesize
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname plone.directives.form zope.i18nmessageid plone.api
%py_requires plone.browserlayer dexml Products.CMFCore plone.registry
%py_requires plone.app.layout plone.app.registry plone.supermodel
%py_requires plone.dexterity zope.component zope.publisher zope.schema
%py_requires zope.interface zope.annotation

%description
zopyx.existdb integrates Plone 4.3 and higher with eXist-db providing
the following features:

* mounts an arbitary eXist-db collection into Plone
* ACE editor integration
* ZIP export from eXist-db
* ZIP import into eXist-db
* pluggable view mechanism for configuring custom views for XML database
  content by filename and view name
* create, rename or delete collections through the web
* extensible architecture through Plone Dexterity behaviors
* support for XQuery scripts called through the RESTXQ layer of eXist-db
  (allows you to call XQuery scripts and return the output format (JSON,
  HTML, XML) depending on your application requirements)
* dedicated per-connector logging facility
* small and extensible
* experimental support for mounting arbitrary WebDAV service into Plone
  (set the emulation mode to webdav in the eXist-db control panel of
  Plone)

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration

%description tests
zopyx.existdb integrates Plone 4.3 and higher with eXist-db providing
the following features:

* mounts an arbitary eXist-db collection into Plone
* ACE editor integration
* ZIP export from eXist-db
* ZIP import into eXist-db
* pluggable view mechanism for configuring custom views for XML database
  content by filename and view name
* create, rename or delete collections through the web
* extensible architecture through Plone Dexterity behaviors
* support for XQuery scripts called through the RESTXQ layer of eXist-db
  (allows you to call XQuery scripts and return the output format (JSON,
  HTML, XML) depending on your application requirements)
* dedicated per-connector logging facility
* small and extensible
* experimental support for mounting arbitrary WebDAV service into Plone
  (set the emulation mode to webdav in the eXist-db control panel of
  Plone)

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
%doc docs/source/*.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/*/*/tests

%files tests
%python_sitelibdir/%mname/*/tests
%python_sitelibdir/%mname/*/*/tests

%changelog
* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.11.1-alt1
- Initial build for Sisyphus

