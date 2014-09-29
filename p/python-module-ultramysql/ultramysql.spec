%define oname ultramysql
Name: python-module-%oname
Version: 2.61
Release: alt1.git20140512
Summary: A fast MySQL driver written in pure C/C++ for Python
License: BSD
Group: Development/Python
Url: https://github.com/esnme/ultramysql
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/esnme/ultramysql.git
Source: %name-%version.tar

BuildPreReq: python-devel gcc-c++

%description
A fast MySQL driver written in pure C/C++ for Python.
Compatible with gevent through monkey patching

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

%files
%doc README
%python_sitelibdir/*

%changelog
* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.61-alt1.git20140512
- Initial build for Sisyphus

