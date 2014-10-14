%define oname Products.SecureMailHost
Name: python-module-%oname
Version: 2.0
Release: alt1.svn20120103
Summary: Reimplementation of Zope2 MailHost with some security and usability enhancements
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.SecureMailHost/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/SecureMailHost/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-docutils

%py_provides %oname
Requires: python-module-Zope2
%py_requires ZODB3

%description
SecureMailHost is a reimplementation of the standard Zope2 MailHost with
some security and usability enhancements.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
SecureMailHost is a reimplementation of the standard Zope2 MailHost with
some security and usability enhancements.

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
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20120103
- Initial build for Sisyphus

