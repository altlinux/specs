%define mname collective
%define oname %mname.flowplayer
Name: python-module-%oname
Version: 4.2.2
Release: alt1.dev0.git20140707
Summary: A simple package using Flowplayer for video and audio content
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.flowplayer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.flowplayer.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.jquerytools
BuildPreReq: python-module-Plone
BuildPreReq: python-module-hachoir-core
BuildPreReq: python-module-hachoir-metadata
BuildPreReq: python-module-hachoir-parser
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-plone.rfc822
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-zope.cachedescriptors
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-plone.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname plone.app.jquerytools Plone Products.CMFCore
%py_requires archetypes.schemaextender Products.ATContentTypes
%py_requires Products.Archetypes plone.rfc822 plone.memoize
%py_requires plone.portlets plone.app.portlets plone.app.vocabularies
%py_requires plone.app.form zope.component zope.interface zope.schema
%py_requires zope.cachedescriptors zope.annotation zope.formlib
%py_requires zope.i18nmessageid

%description
collective.flowplayer integrates the GPL version of Flowplayer with
Plone 4.x. It can play .flv Flash Video files, mp4 files or links as
well as .mp3 files or links.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing Products.CMFPlone zope.configuration
%py_requires plone.testing

%description tests
collective.flowplayer integrates the GPL version of Flowplayer with
Plone 4.x. It can play .flv Flash Video files, mp4 files or links as
well as .mp3 files or links.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.2-alt1.dev0.git20140707
- Initial build for Sisyphus

