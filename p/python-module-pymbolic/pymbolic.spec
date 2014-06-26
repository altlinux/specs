%define oname pymbolic
Name: python-module-%oname
Version: 2014.1.1
Release: alt1
Summary: A package for symbolic computation
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pymbolic
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-sphinx-devel

%description
Pymbolic is a small expression tree and symbolic manipulation library.
Two things set it apart from other libraries of its kind:

* Users can easily write their own symbolic operations, simply by
  deriving from the builtin visitor classes.
* Users can easily add their own symbolic entities to do calculations
  with.

Pymbolic currently understands regular arithmetic expressions,
derivatives, sparse polynomials, fractions, term substitution,
expansion. It automatically performs constant folding, and it can
compile its expressions into Python bytecode for fast(er) execution.

%package pickles
Summary: Pickles for Pymbolic
Group: Development/Python

%description pickles
Pymbolic is a small expression tree and symbolic manipulation library.
Two things set it apart from other libraries of its kind:

* Users can easily write their own symbolic operations, simply by
  deriving from the builtin visitor classes.
* Users can easily add their own symbolic entities to do calculations
  with.

Pymbolic currently understands regular arithmetic expressions,
derivatives, sparse polynomials, fractions, term substitution,
expansion. It automatically performs constant folding, and it can
compile its expressions into Python bytecode for fast(er) execution.

This package contains pickles for Pymbolic.

%package doc
Summary: Documentation for Pymbolic
Group: Development/Documentation
BuildArch: noarch

%description doc
Pymbolic is a small expression tree and symbolic manipulation library.
Two things set it apart from other libraries of its kind:

* Users can easily write their own symbolic operations, simply by
  deriving from the builtin visitor classes.
* Users can easily add their own symbolic entities to do calculations
  with.

Pymbolic currently understands regular arithmetic expressions,
derivatives, sparse polynomials, fractions, term substitution,
expansion. It automatically performs constant folding, and it can
compile its expressions into Python bytecode for fast(er) execution.

This package contains documentation for Pymbolic.

%prep
%setup

%build
%python_build_debug

%make -C doc pickle
%make -C doc html

%install
%python_install

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc LITERATURE README.rst TODO
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files doc
%doc doc/_build/html/*

%changelog
* Thu Jun 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.1.1-alt1
- Initial build for Sisyphus

