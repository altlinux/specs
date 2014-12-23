%define oname schematics

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1.git20141219
Summary: Structured Data for Humans
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/schematics/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/schematics/schematics.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-coverage python-module-z4r-coveralls
BuildPreReq: python-module-dateutil python-module-pymongo
BuildPreReq: python-module-tox python-module-virtualenv
BuildPreReq: python-module-sh
BuildPreReq: python-module-sphinx-devel python-module-ordereddict
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-coverage python3-module-z4r-coveralls
BuildPreReq: python3-module-dateutil python3-module-pymongo
BuildPreReq: python3-module-tox python3-module-virtualenv
BuildPreReq: python3-module-sh
%endif

%py_provides %oname
%py_requires dateutil ordereddict z4r_coveralls

%description
Schematics is a Python library to combine types into structures,
validate them, and transform the shapes of your data based on simple
descriptions.

The internals are similar to ORM type systems, but there is no database
layer in Schematics. Instead, we believe that building a database layer
is made significantly easier when Schematics handles everything but
writing the query.

%package -n python3-module-%oname
Summary: Structured Data for Humans
Group: Development/Python3
%py3_provides %oname
%py3_requires dateutil z4r_coveralls

%description -n python3-module-%oname
Schematics is a Python library to combine types into structures,
validate them, and transform the shapes of your data based on simple
descriptions.

The internals are similar to ORM type systems, but there is no database
layer in Schematics. Instead, we believe that building a database layer
is made significantly easier when Schematics handles everything but
writing the query.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Schematics is a Python library to combine types into structures,
validate them, and transform the shapes of your data based on simple
descriptions.

The internals are similar to ORM type systems, but there is no database
layer in Schematics. Instead, we believe that building a database layer
is made significantly easier when Schematics handles everything but
writing the query.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Schematics is a Python library to combine types into structures,
validate them, and transform the shapes of your data based on simple
descriptions.

The internals are similar to ORM type systems, but there is no database
layer in Schematics. Instead, we believe that building a database layer
is made significantly easier when Schematics handles everything but
writing the query.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20141219
- Initial build for Sisyphus

