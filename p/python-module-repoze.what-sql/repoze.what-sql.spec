%define oname repoze.what-sql
Name: python-module-%oname
Version: 1.0.1
Release: alt1.git20110412.1.1
Summary: The repoze.what 1.0 SQLAlchemy plugin
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.what-sql
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.what-sql.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel python-module-SQLAlchemy
BuildPreReq: python-module-repoze.what python-module-PasteDeploy
BuildPreReq: python-module-repoze.who-testutil python-module-nose
BuildPrereq: python-module-zope.interface python-module-coverage
BuildPrereq: python-module-pysqlite2

%py_requires repoze.what.plugins repoze.what sqlalchemy

%description
This is an adapters plugin for repoze.what.

The SQL plugin makes repoze.what support sources defined in
SQLAlchemy-managed databases by providing one group adapter, one
permission adapter and one utility to configure both in one go
(optionally, when the group source and the permission source have a
relationship).

%package pickles
Summary: Pickles for repoze.what-sql
Group: Development/Python

%description pickles
This is an adapters plugin for repoze.what.

The SQL plugin makes repoze.what support sources defined in
SQLAlchemy-managed databases by providing one group adapter, one
permission adapter and one utility to configure both in one go
(optionally, when the group source and the permission source have a
relationship).

This package contains pickles for repoze.what-sql.

%package docs
Summary: Documentation for repoze.what-sql
Group: Development/Documentation
BuildArch: noarch

%description docs
This is an adapters plugin for repoze.what.

The SQL plugin makes repoze.what support sources defined in
SQLAlchemy-managed databases by providing one group adapter, one
permission adapter and one utility to configure both in one go
(optionally, when the group source and the permission source have a
relationship).

This package contains documentation for repoze.what-sql.

%package -n python-module-repoze.what.plugins
Summary: Core package for repoze.what.plugins
Group: Development/Python
%py_provides repoze.what.plugins
Requires: python-module-repoze.what

%description -n python-module-repoze.what.plugins
Core package for repoze.what.plugins.

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

touch %buildroot%python_sitelibdir/repoze/what/plugins/__init__.py

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc README.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/repoze/what/plugins/__init__.*
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*

%files -n python-module-repoze.what.plugins
%python_sitelibdir/repoze/what/plugins/__init__.*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt1.git20110412.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20110412.1
- Added necessary requirements
- Excluded *.pth

* Thu Jun 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20110412
- Initial build for Sisyphus

