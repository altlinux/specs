%define oname repoze.what-quickstart
Name: python-module-%oname
Version: 1.0.10
Release: alt1.git20111129
Summary: The repoze.what Quickstart plugin
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.what-quickstart
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.what-quickstart.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel python-module-repoze.what-sql
BuildPreReq: python-module-repoze.who.plugins.sa python-module-webob
BuildPreReq: python-module-repoze.what python-module-zope.interface
BuildPreReq: python-module-SQLAlchemy python-module-repoze.who-testutil
BuildPreReq: python-module-PasteDeploy python-module-nose
BuildPreReq: python-module-coverage python-module-pysqlite2
BuildPreReq: python-module-repoze.who-friendlyform

%py_requires repoze.what.plugins repoze.what repoze.who
Requires: python-module-repoze.who.plugins.sa
Requires: python-module-repoze.what-sql
Requires: python-module-repoze.who-friendlyform

%description
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

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
export PYTHONPATH=%python_sitelibdir:%python_sitelibdir_noarch:$PWD
%python_build

pushd docs
%make pickle
%make html
popd

%install
export PYTHONPATH=%python_sitelibdir:%python_sitelibdir_noarch:$PWD
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

