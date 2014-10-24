%define oname Products.i18ntestcase
Name: python-module-%oname
Version: 1.3
Release: alt1.git20130117
Summary: Simplify testing of gettext i18n files for Zope products
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.i18ntestcase/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.i18ntestcase.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests

%py_provides %oname
Requires: python-module-Zope2

%description
Products.i18ntestcase is build on top of the ZopeTestCase package. It
has been developed to simplify testing of gettext i18n files for Zope
products.

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
%python_sitelibdir/*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20130117
- Initial build for Sisyphus

