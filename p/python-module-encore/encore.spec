%define oname encore
Name: python-module-%oname
Version: 0.1
Release: alt1.git20120119
Summary: A Collection of core-level utility modules for Enthought projects
License: BSD
Group: Development/Python
Url: https://github.com/enthought/encore
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/enthought/encore.git
Source: %oname-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-sphinx-devel graphviz
BuildPreReq: python-module-pydot

%description
This package consists of a collection of core utility packages useful for
building Python applications.  This package is intended to be at the
bottom of the software stack and have zero required external dependencies
aside from the Python Standard Library.

%package docs
Summary: Documentation for encore
Group: Development/Documentation

%description docs
This package consists of a collection of core utility packages useful for
building Python applications.  This package is intended to be at the
bottom of the software stack and have zero required external dependencies
aside from the Python Standard Library.

This package contains documentation for encore.

%package pickles
Summary: Pickles for encore
Group: Development/Python

%description pickles
This package consists of a collection of core utility packages useful for
building Python applications.  This package is intended to be at the
bottom of the software stack and have zero required external dependencies
aside from the Python Standard Library.

This package contains pickles for encore.

%prep
%setup

%prepare_sphinx docs
ln -s ../objects.inv docs/source

%build
%python_build_debug

%make -C docs html
%make -C docs pickle

%install
%python_install

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc LICENSE.txt README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*

%files pickles
%python_sitelibdir/%oname/pickle

%changelog
* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20120119
- Initial build for Sisyphus

