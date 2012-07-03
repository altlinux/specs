%define oname scitools
Name: python-module-%oname
Version: 0.8
Release: alt1
Summary: Python library for scientific computing
License: BSD
Group: Development/Python
Url: http://code.google.com/p/scitools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar

BuildPreReq: python-devel
BuildArch: noarch

%add_python_req_skip visit

%description
SciTools is a Python package containing many useful tools for scientific
computing in Python. The package is built on top of other widely used
packages such as NumPy, SciPy, ScientificPython, Matplotlib, Gnuplot,
etc.

%package docs
Summary: Documentation for SciTools
Group: Development/Documentation

%description docs
SciTools is a Python package containing many useful tools for scientific
computing in Python. The package is built on top of other widely used
packages such as NumPy, SciPy, ScientificPython, Matplotlib, Gnuplot,
etc.

This package contains documentation for SciTools.

%prep
%setup

%build
%python_build_debug

%install
%python_install

cp -fR doc/api/sphinx-html api

%files
%doc ChangeLog LICENSE README
%_bindir/*
%_man1dir/*
%python_sitelibdir/*

%files docs
%doc api doc/easyviz

%changelog
* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Initial build for Sisyphus

