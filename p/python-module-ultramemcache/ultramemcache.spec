%define oname ultramemcache
Name: python-module-%oname
Version: 1.6.3
Release: alt1.git20130215
Summary: Ultra fast memcache client written in highly optimized C++ with Python bindings
License: BSD
Group: Development/Python
Url: https://github.com/esnme/ultramemcache
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/esnme/ultramemcache.git
Source: %name-%version.tar

BuildPreReq: python-devel gcc-c++

%description
ultramemcache is an ultra fast Memcache client written in highly
optimized C++ with Python bindings.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.3-alt1.git20130215
- Initial build for Sisyphus

