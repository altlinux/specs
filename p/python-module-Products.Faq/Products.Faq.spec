%define oname Products.Faq
Name: python-module-%oname
Version: 1.4
Release: alt1.dev0.git20131017
Summary: FAQ - An AT contenttype for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.Faq/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.Faq.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-unittest2 python-module-nose
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.testbrowser
BuildPreReq: python-module-Plone python-module-openid

%py_provides %oname
%py_requires Products.Archetypes Products.ATContentTypes
%py_requires Products.CMFCore Products.GenericSetup zope.i18nmessageid
%py_requires zope.interface

%description
This product is a simple Faq content type for Plone. It provides the
following features:

* Two new types, FaqFolder and FaqEntry. FaqFolder can contain FaqEntry
  and FaqFolder to create categories of questions.
* Questions are collapsable in the FaqEntry's view to show or hide
  answers.
* A delay can be specified to marked recent questions as new (display of
  a small icon before titles).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.testing zope.testbrowser.testing

%description tests
This product is a simple Faq content type for Plone. It provides the
following features:

* Two new types, FaqFolder and FaqEntry. FaqFolder can contain FaqEntry
  and FaqFolder to create categories of questions.
* Questions are collapsable in the FaqEntry's view to show or hide
  answers.
* A delay can be specified to marked recent questions as new (display of
  a small icon before titles).

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
rm -fR build
python setup.py test
#nosetests

%files
%doc *.rst docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/test*

%files tests
%python_sitelibdir/Products/*/test*

%changelog
* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.dev0.git20131017
- Initial build for Sisyphus

