%define pyname pybluez
%define modulename PyBluez

%def_without python2
%def_with python3

Name: python-module-pybluez
Version: 0.22
Release: alt1
Summary: A Python module for the Bluez library
Group: Development/Python
License: GPLv2+
Url: http://code.google.com/p/pybluez/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: libbluez >= 4.0

Source: %url/files/%pyname-%version.tar.gz

BuildRequires: libbluez-devel
%if_with python2
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
PyBluez is an effort to create python wrappers around bluez to allow python
developers to use system bluetooth resources.

%setup_python_module %modulename

%package -n python3-module-pybluez
Summary: A Python module for the Bluez library
Group: Development/Python3

%description -n python3-module-pybluez
PyBluez is an effort to create python wrappers around bluez to allow python
developers to use system bluetooth resources.

%prep
%setup -n %pyname-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%if_with python2
%python_build
%endif

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if_with python2
%files -n python-module-pybluez
%doc README CHANGELOG COPYING
%python_sitelibdir/bluetooth
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/bluetooth/msbt*
%exclude %python_sitelibdir/bluetooth/widcomm*
%endif

%if_with python3
%files -n python3-module-pybluez
%doc README CHANGELOG COPYING
%python3_sitelibdir/bluetooth
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/bluetooth/msbt*
%exclude %python3_sitelibdir/bluetooth/widcomm*
%endif

%changelog
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

