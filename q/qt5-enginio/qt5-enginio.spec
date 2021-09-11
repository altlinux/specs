%define qt_module qtenginio
%def_disable bootstrap

Name: qt5-enginio
Summary: Qt5 - Enginio component
Version: 1.6.2
Release: alt3

# See LICENSE.GPL LICENSE.LGPL LGPL_EXCEPTION.txt, for details
# See also http://doc.qt.io/qt-5/licensing.html
License: LGPLv2 with exceptions or GPLv3 with exceptions
Group: System/Libraries
Url: http://www.qt.io

Source: %name-%version.tar
Patch: qt5-qtenginio_linkedlist.patch

Requires: %name-common = %EVR

# filter qml provides
%global __provides_exclude_from ^%_qt5_archdatadir/qml/.*\\.so$

BuildRequires: qt5-base-devel >= 5.6
BuildRequires: qt5-declarative-devel
%if_disabled bootstrap
BuildRequires: qt5-tools
%endif

%description
Client library for accessing Enginio service from Qt and QML code.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name = %EVR
Requires: qt5-base-devel
%description devel
%summary.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt5-base-common
%description common
Common package for %name

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%prep
%setup
%patch -p1

# this code is trash, "nodiscard" should be at the beginning, not the end 
sed -i "/Q_REQUIRED_RESULT;\{0,1\}$/{s|Q_REQUIRED_RESULT||;s|^|Q_REQUIRED_RESULT|}" \
  src/enginio_{client,plugin}/enginio*.h tests/auto/common/common.h

%build
%qmake_qt5
%make_build
%if_disabled bootstrap
export QT_HASH_SEED=0
%make docs
%endif

%install
%makeinstall_std INSTALL_ROOT=%buildroot
%if_disabled bootstrap
%makeinstall_std install_docs INSTALL_ROOT=%buildroot
%endif

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %buildroot%_qt5_libdir
for prl_file in libEng*.prl ; do
%__subst "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
if [ -f "$(basename ${prl_file} .prl).so" ]; then
rm -fv "$(basename ${prl_file} .prl).la"
%__subst "/^QMAKE_PRL_LIBS/d" ${prl_file}
fi
done
popd

%files
%doc LICENSE* LGPL_EXCEPTION.txt
%_qt5_libdir/libEnginio.so.1*
%_qt5_archdatadir/qml/Enginio/

%files common

%files devel
%_qt5_headerdir/Enginio/
%_qt5_libdir/libEnginio.so
%_qt5_libdir/libEnginio.prl
%dir %_qt5_libdir/cmake/Qt5Enginio/
%_qt5_libdir/cmake/Qt5Enginio/Qt5EnginioConfig*.cmake
%_qt5_libdir/pkgconfig/Enginio.pc
%_qt5_archdatadir/mkspecs/modules/qt_lib_enginio*.pri

%files doc
%if_disabled bootstrap
%_qt5_docdir/*
%endif
%_qt5_examplesdir/*

%changelog
* Sat Sep 11 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.6.2-alt3
- Fixed incorrect placement of "nodiscard"

* Mon Aug 31 2020 Anton Midyukov <antohami@altlinux.org> 1.6.2-alt2
- Fix build with qt5 5.15

* Sun Aug 25 2019 Anton Midyukov <antohami@altlinux.org> 1.6.2-alt1
- initial build for ALT Sisyphus
