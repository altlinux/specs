%define oname repoze.what-sql

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt2.git20110412.1
Summary: The repoze.what 1.0 SQLAlchemy plugin
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.what-sql
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.what-sql.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-SQLAlchemy
#BuildPreReq: python-module-repoze.what python-module-PasteDeploy
#BuildPreReq: python-module-repoze.who-testutil python-module-nose
#BuildPrereq: python-module-zope.interface python-module-coverage
#BuildPrereq: python-module-pysqlite2
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze.what.plugins repoze.what sqlalchemy

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PasteDeploy python-module-PyStemmer python-module-Pygments python-module-SQLAlchemy python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-paste python-module-pytz python-module-repoze python-module-repoze.who python-module-repoze.who-testutil python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-zope python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python3 python3-base
BuildRequires: python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-pysqlite2 python-module-repoze.what rpm-build-python3 time

%description
This is an adapters plugin for repoze.what.

The SQL plugin makes repoze.what support sources defined in
SQLAlchemy-managed databases by providing one group adapter, one
permission adapter and one utility to configure both in one go
(optionally, when the group source and the permission source have a
relationship).

%package -n python3-module-%oname
Summary: The repoze.what 1.0 SQLAlchemy plugin
Group: Development/Python3
%py3_requires repoze.what.plugins repoze.what sqlalchemy

%description -n python3-module-%oname
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

%package -n python3-module-repoze.what.plugins
Summary: Core package for repoze.what.plugins
Group: Development/Python3
%py3_provides repoze.what.plugins
Requires: python3-module-repoze.what

%description -n python3-module-repoze.what.plugins
Core package for repoze.what.plugins.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
export PYTHONPATH=%python_sitelibdir:%python_sitelibdir_noarch:$PWD
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

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

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/repoze/what/plugins/__init__.py
%endif

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

%if_with python3
%files -n python3-module-%oname
%doc README.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/repoze/what/plugins/__init__.*
%exclude %python3_sitelibdir/repoze/what/plugins/__pycache__/__init__.*

%files -n python3-module-repoze.what.plugins
%python3_sitelibdir/repoze/what/plugins/__init__.*
%python3_sitelibdir/repoze/what/plugins/__pycache__/__init__.*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt2.git20110412.1
- NMU: Use buildreq for BR.

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2.git20110412
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt1.git20110412.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20110412.1
- Added necessary requirements
- Excluded *.pth

* Thu Jun 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20110412
- Initial build for Sisyphus

