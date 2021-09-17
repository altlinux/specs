%define oname pysvn

Name: python3-module-%oname
Version: 1.9.12
Release: alt3
Summary: Subversion support for python
License: Apache-1.1
Group: Development/Python3
Url: https://pysvn.sourceforge.io/

Source0: pysvn-%version.tar

BuildRequires: gcc-c++ libcom_err-devel libexpat-devel libkrb5-devel libsubversion-devel subversion
BuildRequires: libaprutil1-devel
BuildRequires: subversion-server-common
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pycxx-devel
BuildPreReq: python3-devel

%description
The pysvn project's goal is to enable Tools to be written in Python that
use Subversion.

%prep
%setup -n pysvn-%version

%build
pushd Source
%__python3 setup.py configure \
    --apr-inc-dir=/usr/include/apr-1 \
    --apu-inc-dir=/usr/include/apu-1 \
    --norpath

%make_build
popd

%install
mkdir -p %buildroot%python3_sitelibdir
cp -r Source/pysvn %buildroot%python3_sitelibdir

%files
%python3_sitelibdir/pysvn

%changelog
* Thu Sep 16 2021 Stanislav Levin <slev@altlinux.org> 1.9.12-alt3
- Fixed FTBFS (removed pyutilib).

* Sat Nov 14 2020 Grigory Ustinov <grenka@altlinux.org> 1.9.12-alt2
- Build without python2 support. (Closes: #39286)

* Fri Jul 03 2020 Grigory Ustinov <grenka@altlinux.org> 1.9.12-alt1
- Build new version.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 1.9.11-alt1
- Build new version.
- Fix license.
- Fix url.

* Thu Aug 01 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.10-alt1
- Build new version.

* Wed Apr 17 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.9-alt1
- Build new version for python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.0-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Feb 10 2016 Denis Medvedev <nbr@altlinux.org> 1.8.0-alt1
- up version

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.8-alt1
- Version 1.7.8
- Added module for Python 3

* Wed Mar 06 2013 Andrey Cherepanov <cas@altlinux.org> 1.7.6-alt1
- New version 1.7.6
- Remove obsoleted patches

* Wed Mar 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt3.3
- Fixed build with subversion 1.7.8

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt3.2
- Removed RPATH

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.2-alt3.1
- Rebuild with Python-2.7

* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt3
- Rebuilt for debuginfo

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt2
- Rebuilt with python 2.6

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 1.5.2-alt1.1
- Rebuilt with python-2.5.

* Wed Jan 02 2008 Gennady Kovalev <gik@altlinux.ru> 1.5.2-alt1
- Initial build

