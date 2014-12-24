%define mname ftw.publisher
%define oname %mname.core
Name: python-module-%oname
Version: 2.4.2
Release: alt1.dev0.git20141202
Summary: Staging and publishing addon for Plone contents
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.publisher.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.publisher.core.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-unittest2 python-module-argparse
BuildPreReq: python-module-openid
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zconfig
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Plone
BuildPreReq: python-module-collective.testcaselayer
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-collective.geo.geographer
BuildPreReq: python-module-collective.geo.contentlocations
BuildPreReq: python-module-simplelayout.base
BuildPreReq: python-module-ftw.contentpage
BuildPreReq: python-module-ftw.shop
BuildPreReq: python-module-ftw.builder-tests

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires plone.app.dexterity Products.Archetypes Products.CMFCore
%py_requires ZConfig ZODB3 plone.app.blob plone.namedfile plone.portlets
%py_requires zope.component zope.dottedname zope.i18nmessageid
%py_requires zope.interface

%description
The ftw.publisher packages provide tools for publishing plone contents
from one instance to another.

This package provides shared tools and utils used by
ftw.publisher.sender and ftw.publisher.receiver.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Plone collective.testcaselayer ftw.testing ftw.contentpage
%py_requires plone.app.testing plone.directives.form plone.namedfile
%py_requires zope.annotation zope.configuration simplelayout.base
%py_requires collective.geo.geographer collective.geo.contentlocations
%py_requires ftw.shop ftw.builder.testing

%description tests
The ftw.publisher packages provide tools for publishing plone contents
from one instance to another.

This package provides shared tools and utils used by
ftw.publisher.sender and ftw.publisher.receiver.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires ftw

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 ftw/publisher/__init__.py \
	%buildroot%python_sitelibdir/ftw/publisher/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/ftw/publisher/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/ftw/publisher/*/test*
%exclude %python_sitelibdir/ftw/publisher/__init__.py*

%files tests
%python_sitelibdir/ftw/publisher/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/ftw/publisher
%python_sitelibdir/ftw/publisher/__init__.py*

%changelog
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1.dev0.git20141202
- Initial build for Sisyphus

