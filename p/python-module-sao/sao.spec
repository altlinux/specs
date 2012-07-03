%define oname sao
Name: python-module-%oname
Version: 0.1
Release: alt1.b1.svn20090930.1
Summary: Python interface for the SAO developed projects, such as XPA,DS9 & Funtools
License: BSD
Group: Development/Python
Url: http://code.google.com/p/python-sao/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://python-sao.googlecode.com/svn/trunk/
Source: %oname-%version.tar

BuildPreReq: python-devel libxpa-devel

%description
This project is aimed to provide a python interface for some programs
developed by Smithsonian Astrophysical Observatory(SAO). One of the main
goal is to communicate with ds9 from python shell via the XPA protocol.
It provides a python wrapper for subset of XPA library and python module
for ds9 based on the XPA module.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc CHANGELOG LICENSE* doc/*
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.b1.svn20090930.1
- Rebuild to remove redundant libpython2.7 dependency

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.b1.svn20090930
- Initial build for Sisyphus

