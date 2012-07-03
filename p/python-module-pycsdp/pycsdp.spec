%define oname pycsdp
Name: python-module-%oname
Version: 0.1.0
Release: alt1.beta.git20100908.2.1.1
Summary: Python/Numpy interface to the semidefinite programming library CSDP
License: GPL v3 or later
Group: Development/Python
Url: http://github.com/BenjaminKern/pycsdp
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://github.com/BenjaminKern/pycsdp.git
Source: %oname-%version.tar.gz

BuildPreReq: libCoinCsdp-devel python-devel libnumpy-devel gcc-c++
BuildPreReq: liblapack-goto-devel

Conflicts: libmpeg4ip
Requires: libCoinCsdp
%py_requires numpy

%description
Python/Numpy interface to the semidefinite programming library CSDP.

%prep
%setup
sed -i 's|@LIBDIR@|%_libdir|' setup.py

%build
%python_build_debug

%install
%python_install

%filter_from_requires /^debug.*(libsdp\.so.*/s/^/libCoinCsdp-debuginfo\t/

%files
%doc COPYING Changelog README examples/*
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt1.beta.git20100908.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt1.beta.git20100908.2.1
- Rebuild with Python-2.7

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.beta.git20100908.2
- Built with GotoBLAS2 instead of ATLAS

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.beta.git20100908.1
- Rebuilt for debuginfo

* Fri Sep 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.beta.git20100908
- Initial build for Sisyphus

