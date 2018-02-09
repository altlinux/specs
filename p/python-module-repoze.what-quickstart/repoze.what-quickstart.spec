# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.git20111129.1.1.1.1
%define oname repoze.what-quickstart

%def_with python3

Name: python-module-%oname
Version: 1.0.10
#Release: alt2.git20111129.1.1
Summary: The repoze.what Quickstart plugin
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.what-quickstart
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.what-quickstart.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-repoze.what-sql
#BuildPreReq: python-module-repoze.who.plugins.sa python-module-webob
#BuildPreReq: python-module-repoze.what python-module-zope.interface
#BuildPreReq: python-module-SQLAlchemy python-module-repoze.who-testutil
#BuildPreReq: python-module-PasteDeploy python-module-nose
#BuildPreReq: python-module-coverage python-module-pysqlite2
#BuildPreReq: python-module-repoze.who-friendlyform
#BuildPreReq: python-module-repoze.who
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.what.plugins repoze.what repoze.who
Requires: python-module-repoze.who.plugins.sa
Requires: python-module-repoze.what-sql
Requires: python-module-repoze.who-friendlyform

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: ca-certificates python-base python-devel python-module-PasteDeploy python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-paste python-module-pytest python-module-pytz python-module-repoze python-module-repoze.what python-module-repoze.what.plugins python-module-repoze.who python-module-repoze.who-testutil python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base
BuildRequires: python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-pysqlite2 python-module-repoze.what-sql python-module-repoze.who-friendlyform python-module-repoze.who.plugins.sa python-module-setuptools python3-module-setuptools rpm-build-python3 time

%description
This is an extras plugin for repoze.what.

This plugin allows you to take advantage of a rather simple, and usual, 
authentication and authorization setup, in which the users' data, the groups 
and the permissions used in the application are all stored in a SQLAlchemy 
or Elixir-managed database.

Put simply, it configures repoze.who and repoze.what in one go so that you 
can have an authentication and authorization system working quickly -- hence 
the name.

%package -n python3-module-%oname
Summary: The repoze.what Quickstart plugin
Group: Development/Python3
%py3_requires repoze.what.plugins repoze.what repoze.who
Requires: python3-module-repoze.who.plugins.sa
Requires: python3-module-repoze.what-sql
Requires: python3-module-repoze.who-friendlyform

%description -n python3-module-%oname
This is an extras plugin for repoze.what.

This plugin allows you to take advantage of a rather simple, and usual, 
authentication and authorization setup, in which the users' data, the groups 
and the permissions used in the application are all stored in a SQLAlchemy 
or Elixir-managed database.

Put simply, it configures repoze.who and repoze.what in one go so that you 
can have an authentication and authorization system working quickly -- hence 
the name.

%package pickles
Summary: Pickles for repoze.what-quickstart
Group: Development/Python
%add_python_req_skip yourproject

%description pickles
This is an extras plugin for repoze.what.

This plugin allows you to take advantage of a rather simple, and usual, 
authentication and authorization setup, in which the users' data, the groups 
and the permissions used in the application are all stored in a SQLAlchemy 
or Elixir-managed database.

Put simply, it configures repoze.who and repoze.what in one go so that you 
can have an authentication and authorization system working quickly -- hence 
the name.

This package contains pickles for repoze.what-quickstart.

%package docs
Summary: Documentation for repoze.what-quickstart
Group: Development/Documentation
BuildArch: noarch

%description docs
This is an extras plugin for repoze.what.

This plugin allows you to take advantage of a rather simple, and usual, 
authentication and authorization setup, in which the users' data, the groups 
and the permissions used in the application are all stored in a SQLAlchemy 
or Elixir-managed database.

Put simply, it configures repoze.who and repoze.what in one go so that you 
can have an authentication and authorization system working quickly -- hence 
the name.

This package contains documentation for repoze.what-quickstart.

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
export PYTHONPATH=$PWD
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.10-alt2.git20111129.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.10-alt2.git20111129.1.1.1
  for NMU.
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.10-alt2.git20111129.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt2.git20111129.1
- NMU: Use buildreq for BR.

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt2.git20111129
- Added module for Python 3

* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt1.git20111129
- Version 1.0.10

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.9-alt1.git20110412.2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt1.git20110412.2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt1.git20110412.1
- Excludes unnecessary tests

* Thu Jun 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt1.git20110412
- Initial build for Sisyphus

