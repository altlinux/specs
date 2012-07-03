%define oname dataflake.ldapconnection
Name: python-module-%oname
Version: 1.2
Release: alt1.1
Summary: LDAP connection library
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/dataflake.ldapconnection/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ldap zope.interface dataflake.cache

%description
This package provides an abstraction layer on top of python-ldap. It
offers a connection object with simplified methods for inserting,
modifying, searching and deleting records in the LDAP directory tree.
Failover/redundancy can be achieved by supplying connection data for
more than one LDAP server.

%package tests
Summary: Tests for dataflake.ldapconnection
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides an abstraction layer on top of python-ldap. It
offers a connection object with simplified methods for inserting,
modifying, searching and deleting records in the LDAP directory tree.
Failover/redundancy can be achieved by supplying connection data for
more than one LDAP server.

This package contains tests for dataflake.ldapconnection.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

