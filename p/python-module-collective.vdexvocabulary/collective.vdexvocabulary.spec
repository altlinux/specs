%define mname collective
%define oname %mname.vdexvocabulary
Name: python-module-%oname
Version: 0.2
Release: alt1.dev.git20140205
Summary: IMS VDEX Vocabularies as Zope Vocabulary
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.vdexvocabulary/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.vdexvocabulary.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-imsvdex python-module-ipdb
BuildPreReq: python-module-interlude
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.ucol

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFCore zope.schema zope.interface
%py_requires zope.component zope.configuration zope.i18n zope.ucol
%py_requires zope.i18nmessageid

%description
IMS VDEX is a standard for exchanging vocabularies.
collective.vdexvocabulary create bridge between vdex vocabularies and
zope vocabularies, so you can easily use it in systems like
Plone / Zope.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
IMS VDEX is a standard for exchanging vocabularies.
collective.vdexvocabulary create bridge between vdex vocabularies and
zope vocabularies, so you can easily use it in systems like
Plone / Zope.

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
nosetests

%files
%doc *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.dev.git20140205
- Initial build for Sisyphus

