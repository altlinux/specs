%define mname ftw
%define oname %mname.testing
Name: python-module-%oname
Version: 1.8.2
Release: alt1.dev0.git20150108
Summary: Provides helpers for writing tests
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.testing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.testing.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-splinter
BuildPreReq: python-module-unittest2 python-module-lxml
BuildPreReq: python-module-cssselect python-module-Plone
BuildPreReq: python-module-openid python-module-path
BuildPreReq: python-module-plone.mocktestcase python-module-mocker
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.PloneHotfix20121106
BuildPreReq: python-module-Products.MailHost
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFQuickInstallerTool
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-zc.buildout-tests
BuildPreReq: python-module-Products.kupu-tests
BuildPreReq: python-module-ftw.contentpage-tests

%py_provides %oname
Requires: python-module-Products.kupu-tests
%py_requires %mname plone.mocktestcase plone.testing zope.component
%py_requires zope.configuration zope.interface zope.publisher Plone
%py_requires plone.app.testing Products.PloneHotfix20121106
%py_requires Products.MailHost Products.CMFCore Products.CMFPlone
%py_requires Products.CMFQuickInstallerTool plone.app.dexterity
%py_requires zc.buildout.testing
%py_requires ftw.contentpage.tests

%description
This package provides some testing helpers and an advanced MockTestCase.

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

%changelog
* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.2-alt1.dev0.git20150108
- New snapshot

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.2-alt1.dev0.git20150105
- Version 1.8.2.dev0

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1.dev0.git20141231
- Version 1.8.1.dev0

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt1.dev0.git20141107
- Initial build for Sisyphus

