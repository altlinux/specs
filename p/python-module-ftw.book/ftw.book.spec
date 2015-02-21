%define mname ftw
%define oname %mname.book
Name: python-module-%oname
Version: 3.0.4
Release: alt1.dev0.git20150219
Summary: Produce books with Plone and export them in a high quality PDF
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.book/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.book.git
Source: %name-%version.tar

BuildPreReq: %_bindir/convert
BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-BeautifulSoup python-module-lxml
BuildPreReq: python-module-mocker python-module-transaction
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-ftw.tabbedview
BuildPreReq: python-module-ftw.table
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.DataGridField
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.TinyMCE
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-ftw.contentpage
BuildPreReq: python-module-ftw.pdfgenerator
BuildPreReq: python-module-ftw.profilehook
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-plone.app.contentmenu
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-simplelayout.base
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-ftw.inflator
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.mocktestcase
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.browser
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.viewlet

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname ftw.tabbedview ftw.table Products.LinguaPlone lxml
%py_requires BeautifulSoup Products.ATContentTypes Products.Archetypes
%py_requires Products.CMFCore Products.CMFPlone Products.DataGridField
%py_requires Products.GenericSetup Products.TinyMCE ftw.contentpage
%py_requires Products.statusmessages archetypes.schemaextender zope.i18n
%py_requires ftw.pdfgenerator ftw.profilehook ftw.upgrade plone.indexer
%py_requires plone.app.contentmenu plone.app.layout plone.app.portlets
%py_requires plone.portlets simplelayout.base zope.annotation
%py_requires zope.component zope.dottedname zope.i18nmessageid
%py_requires zope.interface zope.publisher zope.schema plone.portlets

%description
This package provides content types for creating a book which can be
exported as PDF.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.GenericSetup ftw.builder.testing ftw.inflator
%py_requires ftw.testbrowser ftw.testing mocker plone.app.testing
%py_requires plone.browserlayer plone.mocktestcase transaction unittest2
%py_requires zope.app.component zope.browser zope.configuration
%py_requires zope.i18n zope.traversing zope.viewlet

%description tests
This package provides content types for creating a book which can be
exported as PDF.

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
* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt1.dev0.git20150219
- Initial build for Sisyphus

