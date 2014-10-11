%define oname Products.LDAPUserFolder
Name: python-module-%oname
Version: 2.27
Release: alt1
Summary: A LDAP-enabled Zope 2 user folder
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.LDAPUserFolder/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-ldap python-module-dataflake.fakeldap
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.GenericSetup

%py_provides %oname
Requires: python-module-Zope2
%py_requires dataflake.fakeldap Products.CMFDefault
%py_requires Products.GenericSetup

%description
This product is a replacement for a Zope user folder. It does not store
its own user objects but builds them on the fly after authenticating a
user against the LDAP database.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This product is a replacement for a Zope user folder. It does not store
its own user objects but builds them on the fly after authenticating a
user against the LDAP database.

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
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.27-alt1
- Initial build for Sisyphus

