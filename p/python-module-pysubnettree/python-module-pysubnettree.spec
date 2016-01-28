%define oname pysubnettree

%def_with python3

Summary: Provides maps subnets given in CIDR notation to Python objects
Name: python-module-%oname
Version: 0.23
Release: alt1.1
Source: pysubnettree-%version.tar.gz
License: BSD-style
Group: Development/Python
Url: http://www.icir.org/robin/pysubnettree
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Obsoletes: pysubnettree <= 0.12-alt1

#BuildPreReq: python-devel rpm-build-python libstdc++-devel gcc-c++
#BuildPreReq: python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils libstdc++-devel python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: gcc-c++ python-module-setuptools python3-devel python3-module-setuptools rpm-build-python3

%description
The PySubnetTree package provides a Python data structure SubnetTree
which maps subnets given in CIDR notation to Python objects. Lookups are
performed by longest-prefix matching.

%package -n python3-module-%oname
Summary: Provides maps subnets given in CIDR notation to Python objects
Group: Development/Python3

%description -n python3-module-%oname
The PySubnetTree package provides a Python data structure SubnetTree
which maps subnets given in CIDR notation to Python objects. Lookups are
performed by longest-prefix matching.

%prep
%setup -n pysubnettree-%version

%if_with python3
cp -fR . ../python3
%endif

%build
# Unfortunately build and install steps should be done at once
# because otherwise .pyo files won't get into INSTALLED_FILES
# record
%add_optflags -fno-strict-aliasing
%python_build_debug \
    install --optimize=2 \
        --root=`pwd`/buildroot \
        --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_build_debug \
    install --optimize=2 \
        --root=`pwd`/buildroot
popd
%endif

%install
cp -pr buildroot %buildroot

%if_with python3
install -d %buildroot%python3_sitelibdir
pushd ../python3
cp -fR buildroot/%python3_sitelibdir/* %buildroot%python3_sitelibdir/
popd
%endif

unset RPM_PYTHON

%files -f INSTALLED_FILES
%doc CHANGES COPYING README

%if_with python3
%files -n python3-module-%oname
%doc CHANGES COPYING README
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.23-alt1.1
- NMU: Use buildreq for BR.

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23-alt1
- Version 0.23
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12-alt2.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12-alt2.2.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt2.2
- Rebuilt for debuginfo

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt2.1
- Rebuilt with python 2.6

* Mon Mar 09 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12-alt2
- Rename pysubnettree to python-module-pysubnettree
- Add Obsoletes: pysubnettree <= 0.12-alt1

* Fri Oct 17 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12-alt1
- New version

* Wed May 14 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.11-alt1
- Build for ALT
