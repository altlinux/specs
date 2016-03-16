%define oname repoze.who-testutil

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt2.svn20100816.1.1
Summary: Test utilities for repoze.who-powered applications
License: BSD
Group: Development/Python
Url: http://code.gustavonarea.net/repoze.who-testutil/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.repoze.org/whoplugins/whotestutil/trunk/
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-PasteDeploy
#BuildPreReq: python-module-zope.interface python-module-repoze.who
#BuildPreReq: python-module-nose python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

%py_provides repoze.who-testutil
%py_requires repoze.who zope.interface paste paste.deploy

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-paste python-module-pytz python-module-repoze python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base
BuildRequires: python-module-PasteDeploy python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-repoze.who python3-module-setuptools rpm-build-python3 time

%description
repoze.who-testutil is a repoze.who plugin which modifies repoze.who's
original middleware to make it easier to forge authentication, without
bypassing identification (this is, running the metadata providers).

It's been created in order to ease testing of repoze.who-powered
applications, in a way independent of the identifiers, authenticators
and challengers used originally by your application, so that you won't
have to update your test suite as your application grows and the
authentication method changes.

%package -n python3-module-%oname
Summary: Test utilities for repoze.who-powered applications
Group: Development/Python3
%py3_provides repoze.who-testutil
%py3_requires repoze.who zope.interface paste paste.deploy

%description -n python3-module-%oname
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
%doc README.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc README.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/tests
%endif

%changelog
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

