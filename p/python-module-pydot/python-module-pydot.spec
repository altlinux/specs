%define oname pydot
Name: python-module-%oname
Version: 1.0.28
Release: alt1

Summary: Python interface to Graphiz's Dot

License: GPL
Group: Development/Python
Url: http://pydot.googlecode.com

Packager: Vitaly Lipatov <lav@altlinux.ru>
Source: http://pydot.googlecode.com/files/%oname-%version.tar.bz2

BuildArch: noarch

%setup_python_module %oname

# Automatically added by buildreq on Sun Sep 16 2007
BuildRequires: python-devel python-module-pyparsing python-modules-compiler

%description
An interface for creating both directed and non directed graphs from
Python. Currently all attributes implemented in the Dot language are
supported (up to Graphviz 1.16).

Output can be inlined in Postscript into interactive scientific
environments like TeXmacs, or output in any of the format's supported
by the Graphviz tools dot, neato, twopi.

%prep
%setup -q -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc README
%python_sitelibdir/*

%changelog
* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.28-alt1
- Version 1.0.28

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.1
- Rebuilt with python 2.6

* Thu Jun 19 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)

* Sun Sep 16 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.10-alt1
- initial build for ALT Linux Sisyphus
