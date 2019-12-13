%define oname repoze.who.plugins.ldap

Name: python3-module-%oname
Version: 1.1a1
Release: alt3

Summary: repoze.who.plugins.ldap -- LDAP Authentication for WSGI Applications
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/repoze.who.plugins.ldap/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3 python3-module-sphinx

%py3_requires repoze.who.plugins repoze.who ldap zope.interface


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
Group: Development/Python3
Requires: %name = %version-%release
%py3_requires dataflake.ldapconnection

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
Group: Development/Python3

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

sed -i 's|implements(|# implements(|' $(find ./ -name 'plugins.py')

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

export PYTHONPATH=$PWD
pushd docs
%make pickle
%make html
popd

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/

%files
%doc LICENSE README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/*/tests.*
%exclude %python3_sitelibdir/%oname/pickle

%files tests
%python3_sitelibdir/*/*/*/*/tests.*

%files pickles
%python3_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*


%changelog
* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1a1-alt3
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.1a1-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1a1-alt2.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1a1-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1a1-alt2.1
- NMU: Use buildreq for BR.

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1a1-alt2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1a1-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1a1-alt1
- Initial build for Sisyphus

