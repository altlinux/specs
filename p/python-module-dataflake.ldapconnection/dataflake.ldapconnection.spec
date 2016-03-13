%define oname dataflake.ldapconnection

%def_with python3

Name: python-module-%oname
Version: 1.5
Release: alt2.1
Summary: LDAP connection library
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/dataflake.ldapconnection/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires ldap zope.interface dataflake.cache dataflake

%description
This package provides an abstraction layer on top of python-ldap. It
offers a connection object with simplified methods for inserting,
modifying, searching and deleting records in the LDAP directory tree.
Failover/redundancy can be achieved by supplying connection data for
more than one LDAP server.

%package -n python3-module-%oname
Summary: LDAP connection library
Group: Development/Python3
%py3_requires ldap zope.interface dataflake.cache dataflake

%description -n python3-module-%oname
This package provides an abstraction layer on top of python-ldap. It
offers a connection object with simplified methods for inserting,
modifying, searching and deleting records in the LDAP directory tree.
Failover/redundancy can be achieved by supplying connection data for
more than one LDAP server.

%package -n python3-module-%oname-tests
Summary: Tests for dataflake.ldapconnection
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides an abstraction layer on top of python-ldap. It
offers a connection object with simplified methods for inserting,
modifying, searching and deleting records in the LDAP directory tree.
Failover/redundancy can be achieved by supplying connection data for
more than one LDAP server.

This package contains tests for dataflake.ldapconnection.

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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2
- Added module for Python 3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1
- Version 1.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

