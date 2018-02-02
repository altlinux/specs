%define _unpackaged_files_terminate_build 1
%define oname rql
Name: python-module-%oname
Version: 0.34.1
Release: alt1.1
Summary: Relationship query language (RQL) utilities
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/rql/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/2f/b9/72b37bb153c150521acfe49168b4e404cad93546feabd4e2c680f6dd6ad9/%{oname}-%{version}.tar.gz

BuildPreReq: python-module-setuptools python-module-yapps2
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
%setup -q -n %{oname}-%{version}

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.34.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.34.1-alt1
- automated PyPI update

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.33.0-alt1
- Initial build for Sisyphus

