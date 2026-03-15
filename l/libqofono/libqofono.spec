%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define _libexecdir %_prefix/libexec

Name: libqofono
Version: 0.128
Release: alt1

Summary: Qt 5 library for Ofono
License: LGPL-2.1
Group: System/Libraries
Url: https://github.com/sailfishos/libqofono

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml
BuildRequires(pre): rpm-macros-cmake

BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: cmake

%description
A library for accessing the ofono daemon, and a declarative plugin for
it. This allows accessing ofono in qtquick and friends.

This package contains the Qt5 build of the libqofono library.

%package -n %{name}-devel
Summary: Qt 5 library for Ofono (development files)
Group: Development/Other
Requires: %{name} = %{version}-%{release}

%description -n %{name}-devel
Shared library for accessing the ofono daemon, and a declarative plugin
for it. This allows accessing ofono in qtquick and friends.

This package contains the header files of the libqofono shared library.

%package examples
Summary: QtQuick/QML example application for %name
Group: Development/Other
Requires: %{name} = %{version}-%{release}

%description examples
Shared library for accessing the ofono daemon, and a declarative plugin
for it. This allows accessing ofono in qtquick and friends.

This package contains the ofonotest example application written in
QtQuick/QML.

%package tests
Summary: Qt 5 library for Ofono (unit tests)
Group: Development/Other
Requires: %{name} = %{version}-%{release}

%description tests
Shared library for accessing the ofono daemon, and a declarative plugin
for it. This allows accessing ofono in qtquick and friends.

This package contains the unit tests of the shared library. These
require ofono to be running. Before they can be run at build-time, more
upstream work is required. As an alternative, the executable unit tests
are provided for run-time.

%prep
%setup
%patch -p1
sed -i "s|/opt/tests|%_libexecdir|g" test/auto/tst_qofono/CMakeLists.txt test/auto/tests/CMakeLists.txt
sed -i "s|/opt/examples|%_datadir|g" ofonotest/CMakeLists.txt

%build
%cmake \
       -DQT_MAJOR_VERSION=5
%cmake_build

%install
%cmake_install

mv -v %buildroot%_datadir/libqofono-qt5/ofonotest %buildroot%_libexecdir/libqofono-qt5/

%files
%doc README TODO
%dir %_qt5_qmldir/QOfono
%_qt5_qmldir/QOfono/libQOfonoQtDeclarative.so
%_qt5_qmldir/QOfono/plugins.qmltypes
%_qt5_qmldir/QOfono/qmldir
%_libdir/libqofono-qt5.so.0*

%files -n %{name}-devel
%dir %_includedir/qofono-qt5
%_includedir/qofono-qt5/*.h
%dir %_includedir/qofono-qt5/dbus
%_includedir/qofono-qt5/dbus/*.xml
%_libdir/libqofono-qt5.so
%_libdir/pkgconfig/qofono-qt5.pc

%files examples
%_libexecdir/libqofono-qt5/ofonotest
%_datadir/libqofono-qt5/qml/ofonotest/main.qml/main.qml

%files tests
%exclude %_libexecdir/libqofono-qt5/ofonotest
%dir %_libexecdir/libqofono-qt5
%_libexecdir/libqofono-qt5/*

%changelog
* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 0.128-alt1
- new version 0.128 (with rpmrb script)

* Tue Jul 15 2025 Nikolay Strelkov <snk@altlinux.org> 0.124-alt1
- Initial build for Sisyphus
