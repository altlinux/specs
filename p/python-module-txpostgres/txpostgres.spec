%define oname txpostgres

%def_without python3

Name: python-module-%oname
Version: 1.2.0.1
Release: alt2.git20140624.1
Summary: Twisted wrapper for asynchronous PostgreSQL connections
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/txpostgres/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wulczer/txpostgres.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-twisted-core-test python-module-psycopg2
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-twisted-core-test python3-module-psycopg2
%endif

%py_provides %oname
%py_requires twisted.python

%description
A Twisted wrapper for asynchronous PostgreSQL connections.

Based on the interface exposed from the native Postgres C library by the
Python psycopg2 driver.

Can be used as a drop-in replacement for Twisted's adbapi module when
working with PostgreSQL. The only part that does not provide 100%%
compatibility is connection pooling, although pooling provided by
txpostgres is very similar to the one Twisted adbapi offers.

%if_with python3
%package -n python3-module-%oname
Summary: Twisted wrapper for asynchronous PostgreSQL connections
Group: Development/Python3
%py3_provides %oname
%py3_requires twisted.python

%description -n python3-module-%oname
A Twisted wrapper for asynchronous PostgreSQL connections.

Based on the interface exposed from the native Postgres C library by the
Python psycopg2 driver.

Can be used as a drop-in replacement for Twisted's adbapi module when
working with PostgreSQL. The only part that does not provide 100%%
compatibility is connection pooling, although pooling provided by
txpostgres is very similar to the one Twisted adbapi offers.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A Twisted wrapper for asynchronous PostgreSQL connections.

Based on the interface exposed from the native Postgres C library by the
Python psycopg2 driver.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A Twisted wrapper for asynchronous PostgreSQL connections.

Based on the interface exposed from the native Postgres C library by the
Python psycopg2 driver.

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

%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
popd
%endif

%files
%doc NEWS NOTICE *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html doc/*.py

%if_with python3
%files -n python3-module-%oname
%doc NEWS NOTICE *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.0.1-alt2.git20140624.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Mar 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0.1-alt2.git20140624
- Fixed build

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0.1-alt1.git20140624
- Initial build for Sisyphus

