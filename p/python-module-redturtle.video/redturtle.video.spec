%define mname redturtle
%define oname %mname.video

%def_disable check

Name: python-module-%oname
Version: 1.1.1
Release: alt1.dev0.git20140711
Summary: A simple video support for Plone, mainly based on collective.flowplayer
License: GPLv2+
Group: Development/Python
Url: https://plone.org/products/redturtle.video
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/redturtle.video.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-hachoir-core
BuildPreReq: python-module-hachoir-metadata
BuildPreReq: python-module-hachoir-parser
BuildPreReq: python-module-collective.flowplayer
BuildPreReq: python-module-plone.app.imaging
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.contentmigration
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.app.pagetemplate
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-wildcard.media

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires hachoir_core hachoir_metadata hachoir_parser plone.memoize
%py_requires collective.flowplayer plone.app.imaging Products.CMFPlone
%py_requires Products.contentmigration Products.statusmessages
%py_requires Products.CMFCore Products.Archetypes plone.namedfile
%py_requires Products.ATContentTypes plone.app.textfield plone.app.form
%py_requires plone.app.vocabularies plone.app.portlets plone.portlets
%py_requires plone.app.blob zope.component zope.interface zope.formlib
%py_requires zope.app.pagetemplate zope.browserpage zope.schema
%py_requires zope.i18nmessageid zope.event wildcard.media

%description
Video content types for Plone; use collective.flowplayer but also
pluggable with external services. - Forward compatibility shim version,
for easily migrate to wildcard.media.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing Products.PloneTestCase zope.publisher
%py_requires zope.traversing

%description tests
Video content types for Plone; use collective.flowplayer but also
pluggable with external services. - Forward compatibility shim version,
for easily migrate to wildcard.media.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

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

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.dev0.git20140711
- Initial build for Sisyphus

