%define oname xlib
Name: python3-module-xlib
Version: 0.15
Release: alt1.git20140628

Summary: Python X Library

Group: Development/Python3
License: LGPL
Url: https://github.com/LiuLang/python3-xlib

# https://github.com/LiuLang/python3-xlib.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel

%description
The Python X Library is a complete X11R6 client-side implementation,
written in pure Python. It can be used to write low-levelish X Windows
client applications in Python.

%package docs
Summary: Documentation and examples for Python X Library
Group: Development/Documentation
BuildArch: noarch

%description docs
The Python X Library is a complete X11R6 client-side implementation,
written in pure Python. It can be used to write low-levelish X Windows
client applications in Python.

This package contains documentation and examples for Python X Library.

%prep
%setup

%build
%python3_build

pushd doc/html
%make SRCS=$PWD/../src TOPSRC=$PWD/../src/python-xlib.texi
popd

%install
%python3_install

# hack for x86_64 build
test -d %buildroot%_libdir || mv %buildroot%prefix/lib %buildroot%_libdir || :

%files
%doc README*
%python3_sitelibdir/*

%files docs
%doc examples doc/html/*.html

%changelog
* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15-alt1.git20140628
- Initial build for Sisyphus

