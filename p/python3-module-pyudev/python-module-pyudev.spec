# wait for new wx
%def_without wx
%def_without qt4
%def_without pyside

Name: python3-module-pyudev
Version: 0.22.0
Release: alt1

Group: System/Libraries
Summary: Udev bindings for Python
Url: http://packages.python.org/pyudev/
License: LGPLv2.1+

BuildArch: noarch

Source: pyudev-%version.tar

BuildRequires(pre): rpm-build-python3

%description
A Python binding to libudev, the hardware management library and service
found in modern linux systems.

%package -n python3-module-pyudev-qtbase
Summary: Udev Base mixin class for Qt4,Qt5 support
Group: Development/Python
Requires: python3-module-pyudev = %EVR
%description -n python3-module-pyudev-qtbase
Udev Base mixin class for Qt4,Qt5 support

%package -n python3-module-pyudev-pyqt5
Summary:            Udev PyQt5 bindings for Python
Group:              Development/Python
Requires: python3-module-pyudev = %EVR python3-module-pyudev-qtbase = %EVR
%description -n python3-module-pyudev-pyqt5
A Python PyQt5 binding to libudev, the hardware management library and
service found in modern linux systems.

%package -n python3-module-pyudev-pyqt4
Summary:            Udev PyQt4 bindings for Python
Group:              Development/Python3
Requires: python3-module-pyudev = %EVR python3-module-pyudev-qtbase = %EVR
%description -n python3-module-pyudev-pyqt4
A Python3 PyQt4 binding to libudev, the hardware management library and
service found in modern linux systems.

%package -n python3-module-pyudev-pyside
Summary:            Udev PySide bindings for Python
Group:              Development/Python
Requires: python3-module-pyudev = %EVR
%description -n python3-module-pyudev-pyside
A Python PySide binding to libudev, the hardware management library and
service found in modern linux systems.

%package -n python3-module-pyudev-glib
Summary:            Udev Glib bindings for Python
Group:              Development/Python
Requires: python3-module-pyudev = %EVR
%description -n python3-module-pyudev-glib
A Python Glib binding to libudev, the hardware management library and
service found in modern linux systems.

%package -n python3-module-pyudev-wx
Summary:            Udev Wx bindings for Python
Group:              Development/Python
Requires: python3-module-pyudev = %EVR
%description -n python3-module-pyudev-wx
A Python Wx binding to libudev, the hardware management library and
service found in modern linux systems.

%prep
%setup -n pyudev-%version

%build
%python3_build

%install
%python3_install

%files
%doc CHANGES.rst COPYING README.rst
%python3_sitelibdir/pyudev
%exclude %python3_sitelibdir/pyudev/pyqt?.p*
%exclude %python3_sitelibdir/pyudev/_qt_base.p*
%exclude %python3_sitelibdir/pyudev/glib.p*
%exclude %python3_sitelibdir/pyudev/pyside.p*
%exclude %python3_sitelibdir/pyudev/wx.p*
%python3_sitelibdir/pyudev-*

%files -n python3-module-pyudev-qtbase
%python3_sitelibdir/pyudev/_qt_base.p*

%if_with qt4
%files -n python3-module-pyudev-pyqt4
%python3_sitelibdir/pyudev/pyqt4.p*
%endif

%files -n python3-module-pyudev-pyqt5
%python3_sitelibdir/pyudev/pyqt5.p*

%files -n python3-module-pyudev-glib
%python3_sitelibdir/pyudev/glib.p*

%if_with pyside
%files -n python3-module-pyudev-pyside
%python3_sitelibdir/pyudev/pyside.p*
%endif

%if_with wx
%files -n python3-module-pyudev-wx
%python3_sitelibdir/pyudev/wx.p*
%endif

%changelog
* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22.0-alt1
- 0.22.0

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.21.0-alt4
- Drop python2 support.

* Mon Jun 07 2021 Sergey V Turchin <zerg@altlinux.org> 0.21.0-alt3
- disable build of qt4 and pyside modules

* Fri Feb 07 2020 Vitaly Lipatov <lav@altlinux.ru> 0.21.0-alt2
- NMU: disable build python2 modules
- disable wx subpackage (need new wx module)

* Mon Nov 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 0.21.0-alt1.1
- split bindings

* Wed Nov 02 2016 Sergey V Turchin <zerg@altlinux.org> 0.21.0-alt1
- new version (ALT#32700)
- split PyQt parts

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.16.1-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.16.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.16.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Jul 17 2014 Andrey Cherepanov <cas@altlinux.org> 0.16.1-alt1
- New version
- Package with Python3 too

* Wed Feb 15 2012 Sergey V Turchin <zerg@altlinux.org> 0.14-alt0.M60P.1
- built for M60P

* Tue Feb 14 2012 Sergey V Turchin <zerg@altlinux.org> 0.14-alt1
- initial build
