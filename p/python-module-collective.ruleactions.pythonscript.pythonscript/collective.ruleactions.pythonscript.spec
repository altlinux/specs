%define mname collective.ruleactions.pythonscript
%define oname %mname.pythonscript
Name: python-module-%oname
Version: 0.2
Release: alt1.dev0.git20150105
Summary: Though-the-web scriptable contenrules for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.ruleactions.pythonscript/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.ruleactions.pythonscript.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.contentrules
BuildPreReq: python-module-plone.app.contentrules
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.untrustedpython

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires plone.contentrules plone.app.contentrules plone.memoize
%py_requires zope.i18n zope.security zope.schema zope.formlib
%py_requires zope.interface zope.component zope.untrustedpython

%description
Though-the-web scriptable contenrules for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.component.testing zope.testing

%description tests
Though-the-web scriptable contenrules for Plone.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires collective

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

install -p -m644 collective/ruleactions/__init__.py \
	%buildroot%python_sitelibdir/collective/ruleactions/

%check
python setup.py test
py.test collective/ruleactions/pythonscript/tests.py

%files
%doc *.rst docs/*
%python_sitelibdir/collective/ruleactions/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/ruleactions/*/tests.*
%exclude %python_sitelibdir/collective/ruleactions/__init__.py*

%files tests
%python_sitelibdir/collective/ruleactions/*/tests.*

%files -n python-module-%mname
%dir %python_sitelibdir/collective/ruleactions
%python_sitelibdir/collective/ruleactions/__init__.py*

%changelog
* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.dev0.git20150105
- Initial build for Sisyphus

