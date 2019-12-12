%define oname repoze.who-testutil

Name: python3-module-%oname
Version: 1.0.2
Release: alt3

Summary: Test utilities for repoze.who-powered applications
License: BSD
Group: Development/Python3
Url: http://code.gustavonarea.net/repoze.who-testutil/

# http://svn.repoze.org/whoplugins/whotestutil/trunk/
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3 python3-module-sphinx

%py3_provides repoze.who-testutil
%py3_requires repoze.who zope.interface paste paste.deploy


%description
repoze.who-testutil is a repoze.who plugin which modifies repoze.who's
original middleware to make it easier to forge authentication, without
bypassing identification (this is, running the metadata providers).

It's been created in order to ease testing of repoze.who-powered
applications, in a way independent of the identifiers, authenticators
and challengers used originally by your application, so that you won't
have to update your test suite as your application grows and the
authentication method changes.

%package pickles
Summary: Pickles for repoze.who-testutil
Group: Development/Python3

%description pickles
repoze.who-testutil is a repoze.who plugin which modifies repoze.who's
original middleware to make it easier to forge authentication, without
bypassing identification (this is, running the metadata providers).

It's been created in order to ease testing of repoze.who-powered
applications, in a way independent of the identifiers, authenticators
and challengers used originally by your application, so that you won't
have to update your test suite as your application grows and the
authentication method changes.

This package contains pickles for repoze.who-testutil.

%package docs
Summary: Documentation for repoze.who-testutil
Group: Development/Documentation
BuildArch: noarch

%description docs
repoze.who-testutil is a repoze.who plugin which modifies repoze.who's
original middleware to make it easier to forge authentication, without
bypassing identification (this is, running the metadata providers).

It's been created in order to ease testing of repoze.who-powered
applications, in a way independent of the identifiers, authenticators
and challengers used originally by your application, so that you won't
have to update your test suite as your application grows and the
authentication method changes.

This package contains documentation for repoze.who-testutil.

%prep
%setup

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
%doc README.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/tests
%exclude %python3_sitelibdir/%oname/pickle

%files pickles
%python3_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*


%changelog
* Thu Dec 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt3
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt2.svn20100816.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt2.svn20100816.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt2.svn20100816.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt2.svn20100816.1
- NMU: Use buildreq for BR.

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2.svn20100816
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1.svn20100816.1.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.svn20100816.1
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.svn20100816
- Initial build for Sisyphus

