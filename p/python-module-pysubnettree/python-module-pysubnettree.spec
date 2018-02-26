Summary: Provides maps subnets given in CIDR notation to Python objects
Name: python-module-pysubnettree
Version: 0.12
Release: alt2.2.1.1
Source: pysubnettree-%version.tar.gz
License: BSD-style
Group: Development/Python
Url: http://www.icir.org/robin/pysubnettree
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Obsoletes: pysubnettree <= 0.12-alt1

BuildPreReq: python-devel rpm-build-python libstdc++-devel gcc-c++

%description
The PySubnetTree package provides a Python data structure SubnetTree which maps subnets 
given in CIDR notation to Python objects. Lookups are performed by longest-prefix matching.

%prep
%setup -n pysubnettree-%version

%build
# Unfortunately build and install steps should be done at once
# because otherwise .pyo files won't get into INSTALLED_FILES
# record
%add_optflags -fno-strict-aliasing
%python_build_debug \
    install --optimize=2 \
        --root=`pwd`/buildroot \
        --record=INSTALLED_FILES

%install
cp -pr buildroot %buildroot
unset RPM_PYTHON

%files -f INSTALLED_FILES
%doc LICENSE README README.html

%changelog
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
