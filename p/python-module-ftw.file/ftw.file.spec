%define mname ftw
%define oname %mname.file
Name: python-module-%oname
Version: 1.10.1
Release: alt1.dev0.git20141216
Summary: A file content type for gov usecases
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.file/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.file.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Pillow python-module-pyquery
BuildPreReq: python-module-openid
BuildPreReq: python-module-ftw.journal
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-ftw.calendarwidget
BuildPreReq: python-module-ftw.profilehook
BuildPreReq: python-module-ftw.colorbox
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-ftw.activity
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.mocktestcase
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.MimetypesRegistry
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.contentmigration
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.contentrules
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.annotation zope.i18nmessageid
%py_requires zope.traversing zope.interface zope.app.component
%py_requires plone.app.layout zope.component zope.publisher
%py_requires plone.app.blob plone.registry plone.app.contentrules
%py_requires Products.Archetypes Products.contentmigration zope.event
%py_requires Products.validation Products.MimetypesRegistry zope.i18n
%py_requires Products.CMFCore Products.ATContentTypes Products.CMFPlone
%py_requires %mname ftw.journal plone.app.registry ftw.upgrade PIL
%py_requires ftw.calendarwidget ftw.profilehook ftw.colorbox plone.api

%description
This is a file content for plone which provides some useful functions,
such as:

* Write downloader-name in history (ftw.journal)
* Image preview
* New FileField (stores more information in the RESPONSE header)

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.activity ftw.builder.testing ftw.testbrowser
%py_requires ftw.testing plone.app.testing plone.mocktestcase
%py_requires zope.configuration

%description tests
This is a file content for plone which provides some useful functions,
such as:

* Write downloader-name in history (ftw.journal)
* Image preview
* New FileField (stores more information in the RESPONSE header)

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
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1.dev0.git20141216
- Initial build for Sisyphus

