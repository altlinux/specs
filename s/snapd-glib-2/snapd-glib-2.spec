%define _libexecdir %_prefix/libexec

%define _name snapd-glib
%define api_ver 2
%define sover 1
%define libsnapd_glib lib%_name-%api_ver
%define libsnapd_qt libsnapd-qt-%api_ver

%def_enable docs
%def_enable vala
%def_enable qt
%def_enable qml
%def_disable check

Name: snapd-glib-%api_ver
Version: 1.65
Release: alt1.1

Group: System/Libraries
Summary: Library providing a GLib interface to snapd (API 2)
License: LGPL-2.0-or-later
Url: https://github.com/snapcore/snapd-glib

Vcs: https://github.com/snapcore/snapd-glib.git
Source: https://github.com/snapcore/%_name/releases/download/%version/%_name-%version.tar.xz
# 3b46e014bd
Patch10: snapd-glib-1.65-up-Notice_header.patch

BuildRequires(pre): rpm-macros-meson rpm-build-gir %{?_enable_vala:rpm-build-vala} %{?_enable_qt:rpm-macros-qt6}
BuildRequires: meson gcc-c++
BuildRequires: gobject-introspection-devel
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libsoup-3.0)
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_docs:BuildRequires: gtk-doc}
%{?_enable_qt:
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Network)}
%{?_enable_qml:BuildRequires: pkgconfig(Qt6Qml)}

%description
%name is a libsoup-3.0 based library that provides an interface to
communicate with snapd for GLib based applications.

%package -n %libsnapd_glib
Summary: Library providing a Glib interface to snapd (API 2)
Group: System/Libraries

%description -n %libsnapd_glib
snapd-glib is a libsoup-3.0 based library that provides an interface to
communicate with snapd for Glib based applications.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %libsnapd_glib = %EVR

%description devel
This package provides the files for developing applications
that use %name to communicate with snapd.

%package -n %libsnapd_qt
Summary: Library providing a Qt6 interface to snapd (API 2)
Group: System/Libraries
Requires: %libsnapd_glib = %EVR

%description -n %libsnapd_qt
snapd-qt is a library that provides an interface to communicate
with snapd for Qt based applications.

%package -n qt6-qml-snapd-%api_ver
Summary: Library providing a Qt6 QML interface to snapd (API 2)
Group: System/Libraries
Requires: %libsnapd_qt = %EVR

%description -n qt6-qml-snapd-%api_ver
snapd-qt-qml is a library that provides an interface to communicate
with snapd for Qt QML based applications.

%package -n snapd-qt-%api_ver-devel
Summary: Development files for snapd-qt
Group: Development/KDE and QT
Requires: %libsnapd_qt = %EVR
Requires: %name-devel = %EVR

%description -n snapd-qt-%api_ver-devel
This package provides the files for developing applications
that use snapd-qt to communicate with snapd (API 2).

%package tests
Summary: Installed tests for %name
Group: Development/Other
Requires: %libsnapd_glib = %EVR

%description tests
This package provides the files for running the test programs
for %name to verify the functionality of %name.

%package -n snapd-qt-%api_ver-tests
Summary: Installed tests for snapd-qt
Group: Development/KDE and QT
Requires: %libsnapd_qt = %EVR

%description -n snapd-qt-%api_ver-tests
This package provides the files for running the test programs
for snapd-qt to verify the functionality of snapd-qt.

%prep
%setup -n %_name-%version
%patch10 -p1

%build
%meson \
    %{?_disable_docs:-Ddocs=false} \
    %{?_disable_vala:-Dvala-bindings=false} \
    %{?_disable_qt:-Dqt-bindings=false} \
    %{?_disable_qml:-Dqml-bindings=false}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files -n %libsnapd_glib
%_libdir/lib%_name-%api_ver.so.%{sover}*
%_typelibdir/Snapd-%api_ver.typelib
%doc NEWS README*

%files devel
%_includedir/%_name-%api_ver/
%_libdir/lib%_name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%_girdir/Snapd-%api_ver.gir
%_vapidir/%_name-%api_ver.*
%{?_enable_docs:%doc %_datadir/gtk-doc/html/%_name/}

%files tests
%_libexecdir/installed-tests/%_name-%api_ver/*-glib
%_datadir/installed-tests/%_name-%api_ver/*-glib.test

%if_enabled qt
%files -n %libsnapd_qt
%_libdir/libsnapd-qt-%api_ver.so.%{sover}*

%if_enabled qml
%files -n qt6-qml-snapd-%api_ver
%_qt6_qmldir/Snapd%api_ver/
%endif

%files -n snapd-qt-%api_ver-devel
%_includedir/snapd-qt-%api_ver/
%_libdir/libsnapd-qt-%api_ver.so
%_pkgconfigdir/snapd-qt-%api_ver.pc
%_libdir/cmake/Snapd%api_ver/

%files -n snapd-qt-%api_ver-tests
%_libexecdir/installed-tests/%_name-%api_ver/*-qt6
%_datadir/installed-tests/%_name-%api_ver/*-qt6.test
%endif

%changelog
* Thu Jul 11 2024 Yuri N. Sedunov <aris@altlinux.org> 1.65-alt1.1
- applied upstream fix "snapd-qt/meson.build: Install Notice header" (ALT #50876)

* Wed Apr 10 2024 Yuri N. Sedunov <aris@altlinux.org> 1.65-alt1
- 1.65 (ported to qt6)

* Sat Sep 09 2023 Yuri N. Sedunov <aris@altlinux.org> 1.64-alt1
- first build for Sisyphus

