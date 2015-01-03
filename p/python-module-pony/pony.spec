%define oname pony

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.6.1
Release: alt1.dev.git20141229
Summary: Pony Object-Relational Mapper
License: AGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pony/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

#https://github.com/ponyorm/pony.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-modules-sqlite3
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-modules-sqlite3
%endif

%py_provides %oname
%py_requires sqlite3
%add_python_req_skip cx_Oracle

%description
Pony ORM is easy to use and powerful object-relational mapper for
Python. Using Pony, developers can create and maintain database-oriented
software applications faster and with less effort. One of the most
interesting features of Pony is its ability to write queries to the
database using generator expressions. Pony then analyzes the abstract
syntax tree of a generator and translates it to its SQL equivalent.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Pony ORM is easy to use and powerful object-relational mapper for
Python. Using Pony, developers can create and maintain database-oriented
software applications faster and with less effort. One of the most
interesting features of Pony is its ability to write queries to the
database using generator expressions. Pony then analyzes the abstract
syntax tree of a generator and translates it to its SQL equivalent.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Pony Object-Relational Mapper
Group: Development/Python3
%py3_provides %oname
%py3_requires sqlite3
%add_python3_req_skip cx_Oracle

%description -n python3-module-%oname
Pony ORM is easy to use and powerful object-relational mapper for
Python. Using Pony, developers can create and maintain database-oriented
software applications faster and with less effort. One of the most
interesting features of Pony is its ability to write queries to the
database using generator expressions. Pony then analyzes the abstract
syntax tree of a generator and translates it to its SQL equivalent.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Pony ORM is easy to use and powerful object-relational mapper for
Python. Using Pony, developers can create and maintain database-oriented
software applications faster and with less effort. One of the most
interesting features of Pony is its ability to write queries to the
database using generator expressions. Pony then analyzes the abstract
syntax tree of a generator and translates it to its SQL equivalent.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Pony ORM is easy to use and powerful object-relational mapper for
Python. Using Pony, developers can create and maintain database-oriented
software applications faster and with less effort. One of the most
interesting features of Pony is its ability to write queries to the
database using generator expressions. Pony then analyzes the abstract
syntax tree of a generator and translates it to its SQL equivalent.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Pony ORM is easy to use and powerful object-relational mapper for
Python. Using Pony, developers can create and maintain database-oriented
software applications faster and with less effort. One of the most
interesting features of Pony is its ability to write queries to the
database using generator expressions. Pony then analyzes the abstract
syntax tree of a generator and translates it to its SQL equivalent.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/
ln -s conf/conf.py doc/

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

pushd doc
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
popd

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/orm/examples
%exclude %python_sitelibdir/*/orm/tests

%files pickles
%python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/orm/examples
%python_sitelibdir/*/orm/tests

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/orm/examples
%exclude %python3_sitelibdir/*/orm/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/orm/examples
%python3_sitelibdir/*/orm/tests
%endif

%changelog
* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.dev.git20141229
- Initial build for Sisyphus

