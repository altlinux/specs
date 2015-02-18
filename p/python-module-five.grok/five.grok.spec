%define oname five.grok
Name: python-module-%oname
Version: 1.4
Release: alt2.dev.git20141215
Summary: Grok-like layer for Zope 2
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/five.grok/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/five.grok.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-martian python-module-docutils
BuildPreReq: python-module-grokcore.formlib-tests
BuildPreReq: python-module-five.formlib
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-grokcore.layout
BuildPreReq: python-module-five.localsitemanager
BuildPreReq: python-module-grokcore.annotation-tests
BuildPreReq: python-module-grokcore.component-tests
BuildPreReq: python-module-grokcore.security-tests
BuildPreReq: python-module-grokcore.site-tests
BuildPreReq: python-module-grokcore.view-tests
BuildPreReq: python-module-grokcore.viewlet-tests
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.traversing

%py_provides %oname
Requires: python-module-Zope2
%py_requires five grokcore.formlib five.formlib zope.formlib
%py_requires grokcore.layout five.localsitemanager grokcore.annotation
%py_requires grokcore.component grokcore.security grokcore.site
%py_requires grokcore.view grokcore.viewlet zope.annotation
%py_requires zope.component zope.container zope.contentprovider
%py_requires zope.interface zope.location zope.pagetemplate
%py_requires zope.publisher zope.traversing

%description
five.grok is a development layer for Zope 2, based on Grok framework
concepts.

The development techniques are similar to the ones used with Grok
framework.

It is based on grokcore namespace packages that were factored out of
Grok framework.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires grokcore.component.testing grokcore.annotation.testing
%py_requires grokcore.security.testing grokcore.site.testing
%py_requires grokcore.view.testing grokcore.viewlet.testing
%py_requires grokcore.formlib.testing

%description tests
five.grok is a development layer for Zope 2, based on Grok framework
concepts.

The development techniques are similar to the ones used with Grok
framework.

It is based on grokcore namespace packages that were factored out of
Grok framework.

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
%doc *.txt docs/*
%python_sitelibdir/five/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/five/*/*test*

%files tests
%python_sitelibdir/five/*/*test*

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt2.dev.git20141215
- New snapshot

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt2.dev.git20130411
- Added necessary requirements for tests

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.dev.git20130411
- Initial build for Sisyphus

