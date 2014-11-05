%define oname rql
Name: python-module-%oname
Version: 0.33.0
Release: alt1
Summary: Relationship query language (RQL) utilities
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/rql/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-yapps2
BuildPreReq: python-module-logilab-common python-module-logilab-database
BuildPreReq: python-module-logilab-constraint gcc-c++ libgecode-devel
BuildPreReq: python-module-sphinx-devel

%description
A library providing the base utilities to handle RQL queries, such as a
parser, a type inferencer.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A library providing the base utilities to handle RQL queries, such as a
parser, a type inferencer.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A library providing the base utilities to handle RQL queries, such as a
parser, a type inferencer.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug

%install
%python_install

%make -C doc pickle
%make -C doc html

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc ChangeLog README TODO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%changelog
* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.33.0-alt1
- Initial build for Sisyphus

