%define oname geo
Name: python-module-%oname
Version: 1.0.0
Release: alt1.svn20080909.4.1
Summary: Enthought Geophysics Tool Suite

Group: Development/Python
License: BSD
URL: http://code.enthought.com
# https://svn.enthought.com/svn/enthought/Geo
Source: Geo-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-devel, python-module-setuptools
BuildPreReq: python-module-scipy gcc-c++ libnumpy-devel
BuildPreReq: python-module-sphinx python-module-Pygments

%description
Enthought Geophysics Tool Suite.

%package doc
Summary: Documentation for Enthought Geophysics Tool Suite
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation for Enthought Geophysics Tool Suite.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*

%files doc
%doc doc/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.svn20080909.4.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 29 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.svn20080909.4
- Rebuild with Python-2.7

* Fri Oct 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20080909.3
- Rebuilt with updated NumPy

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20080909.2
- Rebuilt for debuginfo

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20080909.1
- Rebuilt with python 2.6

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20080909
- Initial build for Sisyphus

