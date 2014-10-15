%define oname plone.app.locales
Name: python-module-%oname
Version: 4.3.4
Release: alt1.dev0.git20141006
Summary: Translation files for Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.locales/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/plone.app.locales.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests

%py_provides %oname
%py_requires plone.app

%description
This package contains the translation files for Plone Core and the
following non core add-ons:

* LinguaPlone
* plone.app.caching
* plone.app.ldap

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
%doc *.txt *.rst docs
%python_sitelibdir/*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.4-alt1.dev0.git20141006
- Initial build for Sisyphus

