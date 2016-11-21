%def_with python3

#add_findreq_skiplist %python_sitelibdir/pyudev/*

Name: python-module-pyudev
Version: 0.21.0
Release: alt1.1
%setup_python_module pyudev

Group: System/Libraries
Summary: Udev bindings for Python
Url: http://packages.python.org/pyudev/
License: LGPLv2.1+

BuildArch: noarch

Source: pyudev-%version.tar

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: libudev-devel python-devel python-module-distribute

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires:      python3-devel
#BuildRequires:      python3-module-distribute
%endif

%description
A Python binding to libudev, the hardware management library and service
found in modern linux systems.

%package -n python-module-pyudev-qtbase
Summary: Udev Base mixin class for Qt4,Qt5 support
Group: Development/Python
Requires: %name = %EVR
%description -n python-module-pyudev-qtbase
Udev Base mixin class for Qt4,Qt5 support

%package -n python-module-pyudev-pyqt4
Summary:            Udev PyQt4 bindings for Python
Group:              Development/Python
Requires: %name = %EVR python-module-pyudev-qtbase = %EVR
%description -n python-module-pyudev-pyqt4
A Python PyQt4 binding to libudev, the hardware management library and
service found in modern linux systems.

%package -n python-module-pyudev-pyqt5
Summary:            Udev PyQt5 bindings for Python
Group:              Development/Python
Requires: %name = %EVR python-module-pyudev-qtbase = %EVR
%description -n python-module-pyudev-pyqt5
A Python PyQt5 binding to libudev, the hardware management library and
service found in modern linux systems.

%package -n python-module-pyudev-pyside
Summary:            Udev PySide bindings for Python
Group:              Development/Python
Requires: %name = %EVR
%description -n python-module-pyudev-pyside
A Python PySide binding to libudev, the hardware management library and
service found in modern linux systems.

%package -n python-module-pyudev-glib
Summary:            Udev Glib bindings for Python
Group:              Development/Python
Requires: %name = %EVR
%description -n python-module-pyudev-glib
A Python Glib binding to libudev, the hardware management library and
service found in modern linux systems.

%package -n python-module-pyudev-wx
Summary:            Udev Wx bindings for Python
Group:              Development/Python
Requires: %name = %EVR
%description -n python-module-pyudev-wx
A Python Wx binding to libudev, the hardware management library and
service found in modern linux systems.

%if_with python3
%package -n python3-module-pyudev
Summary:            Udev bindings for Python
Group:              System/Libraries
%description -n python3-module-pyudev
A Python3 binding to libudev, the hardware management library and
service found in modern linux systems.

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

%endif

%prep
%setup -q -n pyudev-%version

%build
%python_build

%if_with python3
%python3_build
%endif

%install
%if_with python3
%python3_install
%endif

%python_install

%files
%doc CHANGES.rst COPYING README.rst
%python_sitelibdir/pyudev
%exclude %python_sitelibdir/pyudev/pyqt?.p*
%exclude %python_sitelibdir/pyudev/_qt_base.p*
%exclude %python_sitelibdir/pyudev/glib.p*
%exclude %python_sitelibdir/pyudev/pyside.p*
%exclude %python_sitelibdir/pyudev/wx.p*
%python_sitelibdir/pyudev-*

%files -n python-module-pyudev-qtbase
%python_sitelibdir/pyudev/_qt_base.p*

%files -n python-module-pyudev-pyqt4
%python_sitelibdir/pyudev/pyqt4.p*

%files -n python-module-pyudev-pyqt5
%python_sitelibdir/pyudev/pyqt5.p*

%files -n python-module-pyudev-glib
%python_sitelibdir/pyudev/glib.p*

%files -n python-module-pyudev-pyside
%python_sitelibdir/pyudev/pyside.p*

%files -n python-module-pyudev-wx
%python_sitelibdir/pyudev/wx.p*

%if_with python3
%files -n python3-module-pyudev
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

%files -n python3-module-pyudev-pyqt4
%python3_sitelibdir/pyudev/pyqt4.p*

%files -n python3-module-pyudev-pyqt5
%python3_sitelibdir/pyudev/pyqt5.p*

%files -n python3-module-pyudev-glib
%python3_sitelibdir/pyudev/glib.p*

%files -n python3-module-pyudev-pyside
%python3_sitelibdir/pyudev/pyside.p*

%files -n python3-module-pyudev-wx
%python3_sitelibdir/pyudev/wx.p*
%endif



%changelog
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
