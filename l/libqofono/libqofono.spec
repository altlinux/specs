%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define _libexecdir %_prefix/libexec

Name: libqofono
Version: 0.124
Release: alt1

Summary: Qt 5 library for Ofono
License: LGPL-2.1
Group: System/Libraries
Url: https://github.com/sailfishos/libqofono

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: pkgconfig(Qt5Qml)

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

%build
%qmake_qt5 \
           libqofono.pro \
           CONFIG+=nostrip \
           QMAKE_CXXFLAGS="%optflags"
%make_build

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

mkdir -p %buildroot%_libdir/qt5/mkspecs/features
mv -v %buildroot/usr/share/qt5/share/qt5/mkspecs/features/qofono-qt5.prf %buildroot%_libdir/qt5/mkspecs/features

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
%_libdir/libqofono-qt5.prl
%_libdir/libqofono-qt5.so
%_libdir/pkgconfig/qofono-qt5.pc
%_libdir/qt5/mkspecs/features/qofono-qt5.prf

%files examples
%_datadir/libqofono-qt5/qml/ofonotest/main.qml/main.qml

%files tests
%dir %_libexecdir/libqofono-qt5
%_libexecdir/libqofono-qt5/*

%changelog
* Tue Jul 15 2025 Nikolay Strelkov <snk@altlinux.org> 0.124-alt1
- Initial build for Sisyphus
