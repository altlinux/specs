%define oname LyX
%define origname pylyx
Name: python-module-%oname
Version: 0.1
Release: alt1.1
Summary: Python interface to the LyXServer
License: GPL v2 or later
Group: Development/Python
Url: http://wiki.lyx.org/Tools/PyClient
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://wiki.lyx.org/uploads/Tools/PyClient/pylyx0.1.tar.bz2
BuildArch: noarch
Requires: lyx

%setup_python_module %oname

%description
An easy to use interface for external scripts enhancing LyX.

A Python package with functions and classes to connect to LyX via the
LyXServer and make LyxFunctions available to python scripts:

  * start_lyx() start a LyX session in a separate process
  * lyxpipe() open a lyxpipe for nonblocking access
  * LyXServer basic class for communication with the LyXServer.
  (provides a file-type like object)
  * LyXClient more high level LyX client using the serverpipes
  * lfuns.py a module wrapping lyx functions (LFUNS) to python functions

And the example "end-user" scripts:

  * lyx-remote: Open a file in a running LyX or start LyX with the file
  * lyx-Mx: LyX with an interactive lyxclient ('minibuffer-console')
  * lyx-python: LyX with an interactive Python client
  * bindings help on keybindings and lyxfunctions

%package tests
Summary: Tests for Python interface to the LyXServer
Group: Development/Python
Requires: %name = %version-%release

%description tests
An easy to use interface for external scripts enhancing LyX.

This package contains tests for Python interface to the LyXServer.

%prep
%setup

%install
install -d %buildroot%python_sitelibdir/%oname
install -p -m644 *.py* %buildroot%python_sitelibdir/%oname
install -d %buildroot%_bindir
install -p -m755 examples/* %buildroot%_bindir

cp -fR doc test %buildroot%python_sitelibdir/%oname/

%files
%doc doc/changelog.txt
%_bindir/*
%python_sitelibdir/%oname
%exclude %python_sitelibdir/%oname/test

%files tests
%python_sitelibdir/%oname/test

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Thu Jan 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

