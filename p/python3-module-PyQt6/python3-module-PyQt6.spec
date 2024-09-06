# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

# TODO: quick3d
%define oname PyQt6

%def_with dbus
%def_with webkit

# Note: check Qt subst below
#define qtver %(rpm -q --qf '%%{VERSION}' libqt6-core | sed -e 's|\\.|_|g')

Name: python3-module-%oname
Version: 6.7.1
Release: alt1

Summary: Python 3 bindings for Qt 6
License: GPLv3
Group: Development/Python3

Url: https://www.riverbankcomputing.co.uk/software/pyqt
# Source-url: %__pypi_url %oname
Source: %name-%version.tar
Patch1: alt-decrease-abi-req.patch
Patch2: alt-touint128.patch

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3 >= 0.1.9.2-alt1

BuildRequires: python3-devel

BuildRequires: python3-module-sip6 >= 6.4
BuildRequires: python3-module-sip6 < 7
BuildRequires: python3-module-PyQt-builder >= 1.9
BuildRequires: python3-module-PyQt-builder < 2
#BuildRequires: python3-module-PyQt6-sip

%if_with dbus
BuildRequires: python3-module-dbus
BuildRequires: libdbus-devel
BuildRequires: python3-module-dbus-devel
%endif

BuildRequires: qt6-connectivity-devel qt6-multimedia-devel qt6-sensors-devel
BuildRequires: qt6-serialport-devel qt6-speech-devel
BuildRequires: qt6-svg-devel qt6-tools-devel qt6-websockets-devel
BuildRequires: qt6-declarative-devel qt6-webchannel-devel

#if_with dbus
# https://bugzilla.altlinux.org/show_bug.cgi?id=33873
%py3_provides dbus.mainloop.PyQt6
#endif

Requires: python3-module-PyQt6-sip

%description
Python 3 bindings for the Qt C++ class library. Also includes a PyQt6 backend
code generator for Qt Designer.

%package -n python3-module-%oname-devel
Summary: Sip files for python3-module-%oname
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-%oname-devel
Python 3 bindings for the Qt C++ class library. Also includes a PyQt6 backend
code generator for Qt Designer.

%package examples
Summary: PyQt6 examples
Group: Development/Python3
BuildArch: noarch
Requires: %name = %EVR

%description examples
This package contains PyQt6 examples.

%package webkit
Summary: PyQt6 obsoleted webkit
Group: Development/Python3
Requires: %name = %EVR

%description webkit
This package contains PyQt6 webkit bindings.

%package doc
Summary: PyQt6 docs
Group: Development/Python3
BuildArch: noarch
Requires: %name = %EVR

%description doc
This package contains PyQt6 docs.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
sip-build \
    --no-make \
    --qt-shared \
    --confirm-license \
    --qmake %_qt6_qmake \
    --api-dir=%_qt6_datadir/qsci/api/python \
    --verbose \
    --dbus=%_includedir/dbus-1.0/ \
    --qmake-setting 'QMAKE_CXXFLAGS_RELEASE=%{optflags} -DQT_NO_INT128' \
    --pep484-pyi

%make_build -C build

%install
%makeinstall_std -C build INSTALL_ROOT=%buildroot

#files doc
#doc doc/*
#doc NEWS README

#files examples
#doc examples

%files
%doc NEWS README*
%python3_sitelibdir/PyQt6/
%python3_sitelibdir/PyQt6-%version.dist-info/
%exclude %python3_sitelibdir/PyQt6/bindings/
%exclude %python3_sitelibdir/PyQt6/lupdate/
%_libdir/qt6/plugins/PyQt6/
%if_with dbus
%python3_sitelibdir/dbus/mainloop/pyqt6.abi3.so
%endif

%files devel
%_bindir/pylupdate6
#_bindir/pyrcc6
%_bindir/pyuic6
%dir %_qt6_datadir/
%_qt6_datadir/qsci/
%_libdir/qt6/plugins/designer/libpyqt6.so
%python3_sitelibdir/PyQt6/bindings/
%python3_sitelibdir/PyQt6/lupdate/
#python3_sitelibdir/PyQt6/pyrcc*
#python3_sitelibdir/PyQt6/__pycache__/lupdate*
#python3_sitelibdir/PyQt6/__pycache__/pyrcc*

%changelog
* Fri Aug 23 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version (6.7.1)

* Sat Mar 02 2024 Vitaly Lipatov <lav@altlinux.ru> 6.6.1-alt2
- add BR: qt6-webchannel-devel

* Sat Dec 09 2023 Anton Midyukov <antohami@altlinux.org> 6.6.1-alt1
- new version (6.6.1) with rpmgs script

* Mon Nov 13 2023 Anton Midyukov <antohami@altlinux.org> 6.6.0-alt1
- new version (6.6.0) with rpmgs script

* Wed Aug 16 2023 Michael Shigorin <mike@altlinux.org> 6.5.0-alt3
- add missing BR: qt6-declarative-devel

* Tue Apr 25 2023 Anton Midyukov <antohami@altlinux.org> 6.5.0-alt2
- Add missing provides dbus.mainloop.pyqt6

* Mon Apr 24 2023 Anton Midyukov <antohami@altlinux.org> 6.5.0-alt1
- initial build
