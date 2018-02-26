%define oname repoze.who.plugins.ldap
Name: python-module-%oname
Version: 1.1a1
Release: alt1.1
Summary: repoze.who.plugins.ldap -- LDAP Authentication for WSGI Applications
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.who.plugins.ldap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-epydoc python-module-sphinx-devel

%py_requires repoze.who.plugins repoze.who ldap zope.interface

%description
repoze.who.plugins.ldap is an LDAP plugin for the identification and
authentication framework for WSGI applications, repoze.who, which acts
as WSGI middleware.

It provides you with an straightforward solution to enable LDAP support
in your applications. Yes, you read well: "straightforward", "LDAP" and
"applications" are in the same sentence. In fact, you may make your
application LDAP-aware in few minutes and with few lines of code.

%package tests
Summary: Tests for repoze.who.plugins.ldap
Group: Development/Python
Requires: %name = %version-%release
%py_requires dataflake.ldapconnection

%description tests
repoze.who.plugins.ldap is an LDAP plugin for the identification and
authentication framework for WSGI applications, repoze.who, which acts
as WSGI middleware.

It provides you with an straightforward solution to enable LDAP support
in your applications. Yes, you read well: "straightforward", "LDAP" and
"applications" are in the same sentence. In fact, you may make your
application LDAP-aware in few minutes and with few lines of code.

This package contains tests for repoze.who.plugins.ldap.

%package pickles
Summary: Pickles for repoze.who.plugins.ldap
Group: Development/Python

%description pickles
repoze.who.plugins.ldap is an LDAP plugin for the identification and
authentication framework for WSGI applications, repoze.who, which acts
as WSGI middleware.

It provides you with an straightforward solution to enable LDAP support
in your applications. Yes, you read well: "straightforward", "LDAP" and
"applications" are in the same sentence. In fact, you may make your
application LDAP-aware in few minutes and with few lines of code.

This package contains pickles for repoze.who.plugins.ldap.

%package docs
Summary: Documentation for repoze.who.plugins.ldap
Group: Development/Documentation
BuildArch: noarch

%description docs
repoze.who.plugins.ldap is an LDAP plugin for the identification and
authentication framework for WSGI applications, repoze.who, which acts
as WSGI middleware.

It provides you with an straightforward solution to enable LDAP support
in your applications. Yes, you read well: "straightforward", "LDAP" and
"applications" are in the same sentence. In fact, you may make your
application LDAP-aware in few minutes and with few lines of code.

This package contains documentation for repoze.who.plugins.ldap.

%prep
%setup

%build
%python_build

export PYTHONPATH=$PWD
pushd docs
%make pickle
%make html
popd

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc LICENSE README
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/*/tests.*
%exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/*/*/*/tests.*

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1a1-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1a1-alt1
- Initial build for Sisyphus

