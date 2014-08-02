%define oname fastbit

%def_with python3

Name: python-module-%oname
Version: 20100914
Release: alt3
Summary: Python bindings for FastBit, "An Efficient Compressed Bitmap Index Technology".
License: LGPL
Group: Development/Python
Url: http://code.google.com/p/pyfastbit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://pyfastbit.googlecode.com/svn/trunk
Source: py%oname-%version.tar.gz

BuildPreReq: python-devel python-module-Cython libfastbit-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-Cython
%endif

%description
Python bindings for FastBit, "An Efficient Compressed Bitmap Index
Technology".

%package -n python3-module-%oname
Summary: Python bindings for FastBit, "An Efficient Compressed Bitmap Index Technology".
Group: Development/Python3

%description -n python3-module-%oname
Python bindings for FastBit, "An Efficient Compressed Bitmap Index
Technology".

%prep
%setup
rm %oname.c

%if_with python3
cp -fR . ../python3
sed -i 's|python|python3|g' ../python3/Makefile
%endif

%build
%make_build

%if_with python3
pushd ../python3
%add_optflags -DPyString_AsStringAndSize=PyBytes_AsStringAndSize
%add_optflags -I%_includedir/fastbit
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc BUGS README *test*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc BUGS README *test*
%python3_sitelibdir/*
%endif

%changelog
* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100914-alt3
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 20100914-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20100914-alt2.1
- Rebuild with Python-2.7

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100914-alt2
- Rebuilt for debuginfo

* Thu Sep 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100914-alt1
- Initial build for Sisyphus

