%define mname valentine
%define oname %mname.linguaflow
Name: python-module-%oname
Version: 4.5
Release: alt1.dev.git20130923
Summary: Multilingual extension for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/valentine.linguaflow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/valentine.linguaflow.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.monkeypatcher
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires collective.monkeypatcher Products.LinguaPlone zope.event
%py_requires Products.CMFCore Products.CMFPlone Products.Archetypes
%py_requires plone.app.layout zope.component zope.interface

%description
With this product your multilingual site will have the information to
know

* what translations are invalidate
* what has changed
* when was the change made

If you use XLIFFMarshal to export/import your translations it will also
automatically use this product to validate/re-invalidate a translation.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
With this product your multilingual site will have the information to
know

* what translations are invalidate
* what has changed
* when was the change made

If you use XLIFFMarshal to export/import your translations it will also
automatically use this product to validate/re-invalidate a translation.

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
pushd %mname/linguaflow
cp -fR *.txt *.zcml profiles skins \
	%buildroot%python_sitelibdir/%mname/linguaflow/
install -p -m644 browser/*.zcml \
	%buildroot%python_sitelibdir/%mname/linguaflow/browser/
install -p -m644 tests/*.zcml \
	%buildroot%python_sitelibdir/%mname/linguaflow/tests/
install -p -m644 upgrades/*.zcml \
	%buildroot%python_sitelibdir/%mname/linguaflow/upgrades/
install -p -m644 viewlets/*.zcml viewlets/*.pt \
	%buildroot%python_sitelibdir/%mname/linguaflow/viewlets/
popd

%check
python setup.py test
py.test valentine/linguaflow/tests/*.py

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/*/profiles/testing
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/tests
%python_sitelibdir/%mname/*/profiles/testing

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5-alt1.dev.git20130923
- Initial build for Sisyphus

