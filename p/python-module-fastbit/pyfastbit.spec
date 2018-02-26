%define oname fastbit
Name: python-module-%oname
Version: 20100914
Release: alt2.1.1
Summary: Python bindings for FastBit, "An Efficient Compressed Bitmap Index Technology".
License: LGPL
Group: Development/Python
Url: http://code.google.com/p/pyfastbit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://pyfastbit.googlecode.com/svn/trunk
Source: py%oname-%version.tar.gz

BuildPreReq: python-devel python-module-Cython libfastbit-devel

%description
Python bindings for FastBit, "An Efficient Compressed Bitmap Index
Technology".

%prep
%setup
rm %oname.c

%build
%make_build

%install
%python_install

%files
%doc BUGS README *test*
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 20100914-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20100914-alt2.1
- Rebuild with Python-2.7

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100914-alt2
- Rebuilt for debuginfo

* Thu Sep 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100914-alt1
- Initial build for Sisyphus

