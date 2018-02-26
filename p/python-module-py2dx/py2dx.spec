%define oname py2dx
Name: python-module-%oname
Version: 2.0
Release: alt1.1
Summary: A Python extension for the OpenDX visualization package
License: Free
Group: Development/Python
Url: http://www.psc.edu/general/software/packages/mfix/tools/index.php
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar

BuildPreReq: python-devel swig libopendx-devel gcc-c++

%description
The Python interface, py2dx, is basically a wrapper around the DXLink
routines. A Python program can start DX; load a network or define one on
the fly; set and change variables; and execute the network. The window
in which DX displays its graphics can be one created and managed by
Python.

%prep
%setup

%install
%make all LIBDIR=%_libdir PYTHON_VER=%_python_version \
	PYTHON_DIR=%python_sitelibdir DESTDIR=%buildroot

%files
%doc README Test
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Initial build for Sisyphus

