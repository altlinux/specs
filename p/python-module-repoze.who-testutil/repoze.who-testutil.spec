%define oname repoze.who-testutil
Name: python-module-%oname
Version: 1.0.2
Release: alt1.svn20100816.1.1
Summary: Test utilities for repoze.who-powered applications
License: BSD
Group: Development/Python
Url: http://code.gustavonarea.net/repoze.who-testutil/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.repoze.org/whoplugins/whotestutil/trunk/
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel python-module-PasteDeploy
BuildPreReq: python-module-zope.interface python-module-repoze.who
BuildPreReq: python-module-nose python-module-coverage

%py_provides repoze.who-testutil
%py_requires repoze.who zope.interface paste paste.deploy

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
Group: Development/Python

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

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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
%doc README.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1.svn20100816.1.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.svn20100816.1
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.svn20100816
- Initial build for Sisyphus

