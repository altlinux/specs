%define oname pysubnettree

Name: python3-module-%oname
Version: 0.37
Release: alt1

Summary: Provides maps subnets given in CIDR notation to Python objects

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/pysubnettree

Source: pysubnettree-%version.tar.gz

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++

%description
The PySubnetTree package provides a Python data structure SubnetTree
which maps subnets given in CIDR notation to Python objects. Lookups are
performed by longest-prefix matching.

%prep
%setup -n pysubnettree-%version

%build
# Unfortunately build and install steps should be done at once
# because otherwise .pyo files won't get into INSTALLED_FILES
# record
%add_optflags -fno-strict-aliasing
%python3_build_debug \
    install --optimize=2 \
        --root=`pwd`/buildroot

%install
cp -pr buildroot %buildroot

install -d %buildroot%python3_sitelibdir
cp -fR buildroot/%python3_sitelibdir/* %buildroot%python3_sitelibdir/

%files
%doc CHANGES COPYING README
%python3_sitelibdir/SubnetTree.py
%python3_sitelibdir/_SubnetTree.cpython*.so
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Sat May 25 2024 Grigory Ustinov <grenka@altlinux.org> 0.37-alt1
- Build new version.

* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 0.35-alt1
- Build new version.

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 0.23-alt2
- Drop python2 support.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.23-alt1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.23-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

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
