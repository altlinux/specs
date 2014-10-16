%define mname borg
%define oname %mname.localrole

Name: python-module-%oname
Version: 3.1.1
Release: alt2.dev0.git20140921
Summary: Zope 2 PAS plugin managing local roles via an adapter lookup on the current context
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/borg.localrole/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/borg.localrole.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.deferredimport
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.keyring
BuildPreReq: python-module-collective.monkeypatcher
BuildPreReq: python-module-five.globalrequest
BuildPreReq: python-module-plone.transformchain
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.session

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires plone.memoize
%py_requires Products.PlonePAS Products.PluggableAuthService
%py_requires zope.interface Products.CMFCore Products.GenericSetup
%py_requires zope.annotation zope.component zope.deferredimport

%description
A PAS plugin which can manage local roles via an adapter lookup on the
current context.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing
%py_requires Products.ATContentTypes

%description tests
A PAS plugin which can manage local roles via an adapter lookup on the
current context.

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

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/tests.*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt2.dev0.git20140921
- Added necessary requirements
- Enabled testing

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.dev0.git20140921
- Initial build for Sisyphus

