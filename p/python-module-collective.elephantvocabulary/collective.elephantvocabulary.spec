%define mname collective
%define oname %mname.elephantvocabulary
Name: python-module-%oname
Version: 0.2.4
Release: alt1.git20140826
Summary: zope vocabulary with possibility to hide/show terms
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.elephantvocabulary/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.elephantvocabulary.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-plone.testing

%py_provides %oname
%py_requires %mname zope.interface zope.component zope.schema

%description
Like elephants don't forget anything, so does not
collective.elephantvocabulary. It provides a wrapper around for existing
zope.schema vocabularies and make them not forget anything.

%package tests
Summary: Tests for %oname 
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.registry zope.dottedname plone.testing

%description tests
Like elephants don't forget anything, so does not
collective.elephantvocabulary. It provides a wrapper around for existing
zope.schema vocabularies and make them not forget anything.

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
%doc *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20140826
- Initial build for Sisyphus

