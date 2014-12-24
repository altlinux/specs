%define mname eea
%define oname %mname.forms
Name: python-module-%oname
Version: 6.4
Release: alt1.dev.git20141223
Summary: A collection of custom AT Widgets and Fields
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.forms/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eea/eea.forms.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-collective.quickupload
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.EEAContentTypes
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.app.pagetemplate
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.app.form
BuildPreReq: python-module-zope.component

%py_provides %oname
%py_requires %mname collective.quickupload Products.Archetypes
%py_requires Products.EEAContentTypes Products.validation zope.schema
%py_requires zope.interface zope.browserpage zope.app.pagetemplate
%py_requires zope.formlib zope.app.form zope.component

%description
This package is a collection of custom AT Widgets and Fields:

* Quick Upload Widget based on collective.quickupload
* Management Plan Widget/Field

It also provides some custom jQuery plugins:

* EEAFormsGroup -- group AT Widgets within an accordion in edit form
* EEAFormsWizard -- make schemata tabs a wizard like form with back and
  forward buttons
* EEAFormsQuickUpload -- collective.quickupload jQuery plugin to be used
  with QuickUpload Widget.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
This package is a collection of custom AT Widgets and Fields:

* Quick Upload Widget based on collective.quickupload
* Management Plan Widget/Field

It also provides some custom jQuery plugins:

* EEAFormsGroup -- group AT Widgets within an accordion in edit form
* EEAFormsWizard -- make schemata tabs a wizard like form with back and
  forward buttons
* EEAFormsQuickUpload -- collective.quickupload jQuery plugin to be used
  with QuickUpload Widget.

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

pushd %mname/forms
cp -fR *.txt *.zcml documentation locales profiles skins \
	%buildroot%python_sitelibdir/%mname/forms/
pushd browser
cp -fR *.zcml css img js \
	%buildroot%python_sitelibdir/%mname/forms/browser/
popd
install -p -m644 upgrades/*.zcml \
	%buildroot%python_sitelibdir/%mname/forms/upgrades/
install -p -m644 widgets/*.zcml widgets/*.pt \
	%buildroot%python_sitelibdir/%mname/forms/widgets/
popd

%check
python setup.py test

%files
%doc *.md *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.4-alt1.dev.git20141223
- Version 6.4-dev

* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3-alt1.dev.git20141120
- Initial build for Sisyphus

