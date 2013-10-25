%define oname tabular

%def_without python3

Name: python-module-%oname
Version: 0.1
Release: alt1

Summary: Tabular data container and associated convenience routines in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tabular/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-sphinx-devel
BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Tabular data can be easily represented in Python using the language's
native objects -- e.g. by lists of tuples representing the records of
the data set. Though easy to create, these kind of representations
typically do not enable important tabular data manipulations, like
efficient column selection, matrix mathematics, or spreadsheet-style
operations.

Tabular is a package of Python modules for working with tabular data.
Its main object is the tabarray class, a data structure for holding and
manipulating tabular data. By putting data into a tabarray object,
you'll get a representation of the data that is more flexible and
powerful than a native Python representation.

%package pickles
Summary: Pickles for Tabular
Group: Development/Python

%description pickles
Tabular data can be easily represented in Python using the language's
native objects -- e.g. by lists of tuples representing the records of
the data set. Though easy to create, these kind of representations
typically do not enable important tabular data manipulations, like
efficient column selection, matrix mathematics, or spreadsheet-style
operations.

Tabular is a package of Python modules for working with tabular data.
Its main object is the tabarray class, a data structure for holding and
manipulating tabular data. By putting data into a tabarray object,
you'll get a representation of the data that is more flexible and
powerful than a native Python representation.

This package contains pickles for Tabular.

%package docs
Summary: Documentation for Tabular
Group: Development/Documentation

%description docs
Tabular data can be easily represented in Python using the language's
native objects -- e.g. by lists of tuples representing the records of
the data set. Though easy to create, these kind of representations
typically do not enable important tabular data manipulations, like
efficient column selection, matrix mathematics, or spreadsheet-style
operations.

Tabular is a package of Python modules for working with tabular data.
Its main object is the tabarray class, a data structure for holding and
manipulating tabular data. By putting data into a tabarray object,
you'll get a representation of the data that is more flexible and
powerful than a native Python representation.

This package contains documentation for Tabular.

%if_with python3
%package -n python3-module-%oname
Summary: Tabular data container and associated convenience routines in Python
Group: Development/Python3

%description -n python3-module-%oname
Tabular data can be easily represented in Python using the language's
native objects -- e.g. by lists of tuples representing the records of
the data set. Though easy to create, these kind of representations
typically do not enable important tabular data manipulations, like
efficient column selection, matrix mathematics, or spreadsheet-style
operations.

Tabular is a package of Python modules for working with tabular data.
Its main object is the tabarray class, a data structure for holding and
manipulating tabular data. By putting data into a tabarray object,
you'll get a representation of the data that is more flexible and
powerful than a native Python representation.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
#find -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
#find -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%make -C docs pickle
%make -C docs html

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

