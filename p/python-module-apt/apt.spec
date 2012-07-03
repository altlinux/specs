%define oname apt

Name: python-module-%oname
Version: 0.5.15cnc6
Release: alt4.1

Summary: Python module for APT
Group: Development/Python
License: GPL
Requires: lib%oname >= 0.5.15lorg2
URL: http://apt-rpm.org
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: %oname-%version.tar
Source1: http://apt-rpm.org/python/apt-get.py

BuildPreReq: python-devel swig libapt-devel gcc-c++ liblua5-devel

%description
This package contains Python module for APT.

This package is still under development.

%prep
%setup
rm -f python/*.cxx
install -p -m644 %SOURCE1 .

%build
%make_build -C python

%install
install -d %buildroot%python_sitelibdir
install -m644 python/*.so python/*.py %buildroot%python_sitelibdir

%files
%doc apt-get.py
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.15cnc6-alt4.1
- Rebuild with Python-2.7

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.15cnc6-alt4
- Rebuilt for debuginfo

* Fri Jan 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.15cnc6-alt3
- Rebuilt with apt 0.5.15lorg2-alt37

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.15cnc6-alt2
- Rebuilt for soname set-versions

* Thu Aug 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.15cnc6-alt1
- Initial build for Sisyphus (ALT #23667)

