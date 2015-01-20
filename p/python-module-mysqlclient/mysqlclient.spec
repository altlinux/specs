%define oname mysqlclient

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.3.4
Release: alt1.git20150105
Summary: Python interface to MySQL
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/mysqlclient/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/PyMySQL/mysqlclient-python.git
Source: %name-%version.tar

BuildPreReq: libmysqlclient-devel zlib-devel libssl-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
%endif

Conflicts: python-module-MySQLdb
Conflicts: python-module-MySQLdb2
%py_provides MySQLdb

%description
mysqlclient is a fork of MySQL-python. It add Python 3.3 support and
merges some pull requests.

%package -n python3-module-%oname
Summary: Python interface to MySQL
Group: Development/Python3
Conflicts: python3-module-MySQLdb
Conflicts: python3-module-MySQLdb2
%py3_provides MySQLdb

%description -n python3-module-%oname
mysqlclient is a fork of MySQL-python. It add Python 3.3 support and
merges some pull requests.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
mysqlclient is a fork of MySQL-python. It add Python 3.3 support and
merges some pull requests.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
mysqlclient is a fork of MySQL-python. It add Python 3.3 support and
merges some pull requests.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc HISTORY *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc HISTORY *.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20150105
- New snapshot

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20141102
- Initial build for Sisyphus

