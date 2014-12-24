%define mname ftw
%define oname %mname.blog
Name: python-module-%oname
Version: 1.7.1
Release: alt1.dev0.git20141202
Summary: A Blog for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.blog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.blog.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Plone python-module-pyquery
BuildPreReq: python-module-argparse python-module-openid
BuildPreReq: python-module-ftw.tabbedview
BuildPreReq: python-module-ftw.colorbox
BuildPreReq: python-module-ftw.tagging
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-ftw.profilehook
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.formwidget.contenttree
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.discussion
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-plone.app.upgrade
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-z3c.autoinclude

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname ftw.tabbedview ftw.colorbox ftw.tagging ftw.upgrade
%py_requires ftw.profilehook Plone plone.browserlayer Products.CMFCore
%py_requires plone.formwidget.contenttree Products.CMFPlone zope.i18n
%py_requires Products.Archetypes Products.LinguaPlone plone.app.layout
%py_requires Products.ATContentTypes plone.app.discussion plone.registry
%py_requires plone.portlets plone.app.portlets plone.memoize zope.schema
%py_requires plone.app.blob plone.app.upgrade zope.interface z3c.form
%py_requires zope.component zope.i18nmessageid

%description
ftw.blog provides a blog implementation for Plone featuring tags and
categories.

A user can add a new blog entry and tag it using tags and categories.
Available categories are defined by the creator of the blog, whilst tags
can be added freely by the author of a blog entry.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.builder.testing ftw.testbrowser ftw.testing
%py_requires plone.app.testing zope.configuration z3c.autoinclude

%description tests
ftw.blog provides a blog implementation for Plone featuring tags and
categories.

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
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt1.dev0.git20141202
- Initial build for Sisyphus

