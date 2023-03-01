%define pyname pybluez
%define modulename PyBluez

Name: python3-module-pybluez
Version: 0.23
Release: alt1
Summary: A Python module for the Bluez library
Group: Development/Python3
License: GPLv2+
Url: http://code.google.com/p/pybluez/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: libbluez >= 4.0

Source: %url/files/%pyname-%version.tar.gz
Patch: pybluez-py310.patch

BuildRequires: libbluez-devel
BuildRequires(pre): rpm-build-python3

# needs only for macos
%add_python3_req_skip lightblue

%description
PyBluez is an effort to create python wrappers around bluez to allow python
developers to use system bluetooth resources.

%prep
%setup -n %pyname-%version
%patch -p0
sed -i '/2to3/d' setup.py

%build
%add_optflags -fno-strict-aliasing
%python3_build

%install
%python3_install

%files
%doc README.md CHANGELOG COPYING
%python3_sitelibdir/bluetooth
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/bluetooth/msbt*
%exclude %python3_sitelibdir/bluetooth/widcomm*

%changelog
* Sun Jan 15 2023 Grigory Ustinov <grenka@altlinux.org> 0.23-alt1
- Build new version for python3.11.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 0.22-alt2
- Drop python2 support.

* Wed Apr 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- (NMU) new version
- dropped python2

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.20-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.20-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20-alt1
- Version 0.20
- Added module for Python 3

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.16-alt2.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.16-alt2.1.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16-alt2.1
- Rebuilt for debuginfo

* Mon Nov 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.16-alt2
- fixed build dependencies

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16-alt1.1
- Rebuilt with python 2.6

* Thu Apr 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.16-alt1
- 0.16

* Tue Sep 02 2008 L.A. Kostis <lakostis@altlinux.ru> 0.15-alt1
- 0.15.
- update URL.
- don't pack M$ Windows depended files.

* Sun Jan 07 2007 L.A. Kostis <lakostis@altlinux.ru> 0.9.2-alt1
- 0.9.2.

* Sun Jan 07 2007 L.A. Kostis <lakostis@altlinux.ru> 0.8-alt1.1
- test build without ugly kludge.

* Fri Sep 08 2006 L.A. Kostis <lakostis@altlinux.ru> 0.8-alt1
- 0.8.
- fix build w/ new libbluez.
- add ugly kludge for proper build w/ gear (rpm-build-python sux).

* Sat Apr 22 2006 LAKostis <lakostis at altlinux.ru> 0.6.1-alt0.1
- First build for Sisyphus.

