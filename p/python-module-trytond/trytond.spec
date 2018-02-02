%define _unpackaged_files_terminate_build 1
%define oname trytond

%def_without python3

Name: python-module-%oname
Version: 4.2.1
Release: alt1.1
Summary: Tryton server
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/trytond/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/17/f7/c7981ea71084c8dc4adf61627bd9265716407bc7cedf13bc746dd51cde76/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-lxml python-module-relatorio
BuildPreReq: python-module-genshi python-module-dateutil
BuildPreReq: python-module-polib python-module-sql
BuildPreReq: python-module-psycopg2 python-module-MySQLdb2
BuildPreReq: python-module-pywebdav unoconv python-module-pydot
BuildPreReq: python-module-simplejson python-module-cdecimal
BuildPreReq: python-module-bcrypt python-module-Levenshtein
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-lxml
BuildPreReq: python3-module-genshi python3-module-dateutil
BuildPreReq: python3-module-polib python3-module-sql
BuildPreReq: python3-module-psycopg2 python3-module-MySQLdb
BuildPreReq: python3-module-pywebdav unoconv python3-module-pydot
BuildPreReq: python3-module-simplejson python3-module-cdecimal
BuildPreReq: python3-module-py3k-bcrypt python3-module-Levenshtein
%endif

%py_provides %oname

%description
The server of the Tryton application platform. A three-tiers high-level
general purpose application platform written in Python and use
Postgresql as main database engine. It is the core base of an Open
Source ERP. It provides modularity, scalability and security.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The server of the Tryton application platform. A three-tiers high-level
general purpose application platform written in Python and use
Postgresql as main database engine. It is the core base of an Open
Source ERP. It provides modularity, scalability and security.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
The server of the Tryton application platform. A three-tiers high-level
general purpose application platform written in Python and use
Postgresql as main database engine. It is the core base of an Open
Source ERP. It provides modularity, scalability and security.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The server of the Tryton application platform. A three-tiers high-level
general purpose application platform written in Python and use
Postgresql as main database engine. It is the core base of an Open
Source ERP. It provides modularity, scalability and security.

This package contains documentation for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Tryton server
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The server of the Tryton application platform. A three-tiers high-level
general purpose application platform written in Python and use
Postgresql as main database engine. It is the core base of an Open
Source ERP. It provides modularity, scalability and security.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The server of the Tryton application platform. A three-tiers high-level
general purpose application platform written in Python and use
Postgresql as main database engine. It is the core base of an Open
Source ERP. It provides modularity, scalability and security.

This package contains tests for %oname.
%endif

%prep
%setup -q -n %{oname}-%{version}

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc CHANGELOG README COPYRIGHT PKG-INFO doc
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG README COPYRIGHT PKG-INFO doc
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1
- automated PyPI update

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.2-alt1
- Version 3.4.2

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Version 3.4.0

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.3-alt1
- Initial build for Sisyphus

