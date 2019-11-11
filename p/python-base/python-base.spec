%define python_ver 2.7

Name: python-base
Version: %python_ver.17
Release: alt3

Summary: Base python modules and executables
Group: Development/Python
#BuildArch: noarch
License: PSF
Group: Development/Python
URL: http://www.python.org/
Packager: Python Development Team <python@packages.altlinux.org>

Requires: /usr/bin/python%python_ver

%description
Python is an interpreted, interactive, object-oriented programming
language often compared to Tcl, Perl, Scheme or Java. Python includes
modules, classes, exceptions, very high level dynamic data types and
dynamic typing. Python supports interfaces to many system calls and
libraries, as well as to various windowing systems (X11, Motif, Tk,
Mac and MFC).

This package contains symlink to default python interpreter.

%install
mkdir -p %buildroot%_bindir
ln -sf python%python_ver %buildroot%_bindir/python

mkdir -p %buildroot%_libdir
# hack to make arepo (remove me in the future)
touch %buildroot%_libdir/libpython.so

%files
%_bindir/python
# hack to make arepo (remote it in the future)
%ghost %_libdir/libpython.so

%changelog
* Mon Nov 11 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.7.17-alt3
- Separated to independent package (former subpackage of python package).


