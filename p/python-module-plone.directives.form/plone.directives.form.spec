%define mname plone.directives
%define oname %mname.form
Name: python-module-%oname
Version: 2.0.1
Release: alt1.dev0.git20140823
Summary: Grok-like directives configuring forms
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.directives.form/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.directives.form.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-docutils
BuildPreReq: python-module-zope.deferredimport
BuildPreReq: python-module-five.grok
BuildPreReq: python-module-grokcore.view
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-plone.rfc822

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires zope.deferredimport five.grok grokcore.view plone.autoform
%py_requires plone.z3cform Products.statusmessages plone.supermodel
%py_requires zope.i18nmessageid zope.publisher plone.rfc822

%description
This package provides optional, Grok-like directives for configuring
forms, as defined by the z3c.form library, using XML schemata as defined
by plone.supermodel and/or using widget form layout as defined by
plone.autoform. It depends on five.grok, which in turn depends on the
various re-usable grokcore.* packages, but not Grok itself.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides optional, Grok-like directives for configuring
forms, as defined by the z3c.form library, using XML schemata as defined
by plone.supermodel and/or using widget form layout as defined by
plone.autoform. It depends on five.grok, which in turn depends on the
various re-usable grokcore.* packages, but not Grok itself.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python

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

install -p -m644 plone/directives/__init__.py \
	%buildroot%python_sitelibdir/plone/directives/

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/plone/directives/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/directives/*/tests
%exclude %python_sitelibdir/plone/directives/__init__.py*

%files tests
%python_sitelibdir/plone/directives/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/plone/directives
%python_sitelibdir/plone/directives/__init__.py*

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.dev0.git20140823
- Initial build for Sisyphus

