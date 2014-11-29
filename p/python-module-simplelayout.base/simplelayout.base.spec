%define mname simplelayout
%define oname %mname.base

%def_disable check

Name: python-module-%oname
Version: 4.0.4
Release: alt1.dev0.git20141107
Summary: SimpleLayout is an easy to use plone package for creating content pages
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/simplelayout.base/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/simplelayout.base.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-ftw.builder
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.mocktestcase
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.contentmenu
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.fieldsets
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-plone.app.upgrade
BuildPreReq: python-module-plone.app.content
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-zope.browsermenu
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.lifecycleevent
#BuildPreReq: python-module-simplelayout.ui.base
#BuildPreReq: python-module-simplelayout.types.common
#BuildPreReq: python-module-simplelayout.ui.dragndrop

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires zope.i18nmessageid zope.annotation zope.lifecycleevent
%py_requires zope.contentprovider zope.event zope.formlib zope.viewlet
%py_requires zope.component zope.interface zope.browsermenu zope.schema
%py_requires plone.app.upgrade plone.app.content plone.indexer
%py_requires plone.app.controlpanel plone.fieldsets plone.app.blob
%py_requires plone.app.contentmenu plone.app.layout plone.app.form
%py_requires Products.CMFPlone Products.statusmessages plone.protect
%py_requires archetypes.schemaextender Products.CMFCore plone.memoize
#py_requires simplelayout.ui.base simplelayout.ui.dragndrop

%description
SimpleLayout provides an intuitive way of adding and arranging the
different elements of a page such as paragraphs, images, files and links
using drag-and-drop functionality. These elements are implemented as
addable and easily arrangeable "blocks". Because of the restricted
dimensions of text, images and other content elements, the general
result is content with a uniform look and feel throughout the site.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.builder ftw.testbrowser ftw.testing plone.app.testing
%py_requires plone.mocktestcase Products.Archetypes zope.configuration
#py_requires simplelayout.types.common

%description tests
SimpleLayout provides an intuitive way of adding and arranging the
different elements of a page such as paragraphs, images, files and links
using drag-and-drop functionality. These elements are implemented as
addable and easily arrangeable "blocks". Because of the restricted
dimensions of text, images and other content elements, the general
result is content with a uniform look and feel throughout the site.

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
%doc *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev0.git20141107
- Initial build for Sisyphus

