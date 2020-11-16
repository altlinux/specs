%define python_ver 2.7

Name: python-base
Version: %python_ver.18
Release: alt1

Summary: Base python modules and executables
Group: Development/Python
BuildArch: noarch
License: PSF
Group: Development/Python
URL: http://www.python.org/
Packager: Python Development Team <python@packages.altlinux.org>

Requires: /usr/bin/python%python_ver
Requires: python2-base = %version

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

%files
%_bindir/python

%changelog
* Mon Nov 16 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.7.18-alt1
- Bumped version.
- Added versioned dependency to python2-base.
- Removed temporary hacks.
- Made it noarch.

* Mon Nov 11 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.7.17-alt3
- Separated to independent package (former subpackage of python package).


