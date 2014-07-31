%define oname repoze.who.plugins.ldap

%def_with python3

Name: python-module-%oname
Version: 1.1a1
Release: alt2
Summary: repoze.who.plugins.ldap -- LDAP Authentication for WSGI Applications
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.who.plugins.ldap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-epydoc python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.who.plugins repoze.who ldap zope.interface

%description
repoze.who.plugins.ldap is an LDAP plugin for the identification and
authentication framework for WSGI applications, repoze.who, which acts
as WSGI middleware.

It provides you with an straightforward solution to enable LDAP support
in your applications. Yes, you read well: "straightforward", "LDAP" and
"applications" are in the same sentence. In fact, you may make your
application LDAP-aware in few minutes and with few lines of code.

%package -n python3-module-%oname
Summary: repoze.who.plugins.ldap -- LDAP Authentication for WSGI Applications
Group: Development/Python3
%py3_requires repoze.who.plugins repoze.who ldap zope.interface

%description -n python3-module-%oname
repoze.who.plugins.ldap is an LDAP plugin for the identification and
authentication framework for WSGI applications, repoze.who, which acts
as WSGI middleware.

It provides you with an straightforward solution to enable LDAP support
in your applications. Yes, you read well: "straightforward", "LDAP" and
"applications" are in the same sentence. In fact, you may make your
application LDAP-aware in few minutes and with few lines of code.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.who.plugins.ldap
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires dataflake.ldapconnection

%description -n python3-module-%oname-tests
repoze.who.plugins.ldap is an LDAP plugin for the identification and
authentication framework for WSGI applications, repoze.who, which acts
as WSGI middleware.

It provides you with an straightforward solution to enable LDAP support
in your applications. Yes, you read well: "straightforward", "LDAP" and
"applications" are in the same sentence. In fact, you may make your
application LDAP-aware in few minutes and with few lines of code.

This package contains tests for repoze.who.plugins.ldap.

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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

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

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/*/tests.*
%endif

%changelog
* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1a1-alt2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1a1-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1a1-alt1
- Initial build for Sisyphus

