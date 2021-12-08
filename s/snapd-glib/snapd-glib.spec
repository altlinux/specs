
%define sover 1
%define libsnapd_qt libsnapd-qt%sover
%define libsnapd_glib libsnapd-glib%sover
Name: snapd-glib
Version: 1.58
Release: alt1

Group: System/Libraries
Summary: Library providing a GLib interface to snapd
License: LGPL-2.0-or-later
Url: https://github.com/snapcore/%name

Source: snapd-glib-%version.tar

BuildRequires: gtk-doc
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gobject-introspection-devel
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: /usr/bin/vapigen

%description
%name is a library that provides an interface to communicate
with snapd for GLib based applications.

%package devel
Group: Development/Other
Summary: Development files for %name
%description devel
This package provides the files for developing applications
that use %name to communicate with snapd.

#%package tests
#Summary: Installed tests for %name
#%description tests
#This package provides the files for running the test programs
#for %name to verify the functionality of %name.

%package -n %libsnapd_qt
Group: System/Libraries
Summary: Library providing a Qt5 interface to snapd
%description -n %libsnapd_qt
snapd-qt is a library that provides an interface to communicate
with snapd for Qt based applications.

%package -n %libsnapd_glib
Group: System/Libraries
Summary: Library providing a Glib interface to snapd
%description -n %libsnapd_glib
snapd-qt is a library that provides an interface to communicate
with snapd for Glib based applications.

%package -n qt5-qml-snapd
Group: System/Libraries
Summary: Library providing a Qt5 QML interface to snapd
%description -n qt5-qml-snapd
snapd-qt-qml is a library that provides an interface to communicate
with snapd for Qt QML based applications.

%package -n snapd-qt-devel
Group: Development/Other
Summary: Development files for snapd-qt
#Requires: %name-devel
%description -n snapd-qt-devel
This package provides the files for developing applications
that use snapd-qt to communicate with snapd.

#%package -n snapd-qt-tests
#Summary: Installed tests for snapd-qt
#%description -n snapd-qt-tests
#This package provides the files for running the test programs
#for snapd-qt to verify the functionality of snapd-qt.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files -n %libsnapd_glib
%doc NEWS COPYING*
%_libdir/libsnapd-glib.so.%sover
%_libdir/libsnapd-glib.so.*
%_libdir/girepository-1.0/Snapd-1.typelib

%files devel
%doc %_datadir/gtk-doc/html/snapd-glib/
%_includedir/snapd-glib/
%_libdir/libsnapd-glib.so
%_libdir/pkgconfig/snapd-glib.pc
%_datadir/vala/vapi/snapd-glib.*
%_datadir/gir-1.0/Snapd-1.gir

#%files tests
#%_libexecdir/installed-tests/snapd-glib/*-glib
#%_datadir/installed-tests/snapd-glib/*-glib.test

%files -n %libsnapd_qt
%_libdir/libsnapd-qt.so.%sover
%_libdir/libsnapd-qt.so.*

%files -n qt5-qml-snapd
%_qt5_qmldir/Snapd/

%files -n snapd-qt-devel
%_includedir/snapd-qt
%_libdir/libsnapd-qt.so
%_libdir/pkgconfig/snapd-qt.pc
%_libdir/cmake/Snapd/

#%files -n snapd-qt-tests
#%_libexecdir/installed-tests/snapd-glib/*-qt
#%_datadir/installed-tests/snapd-glib/*-qt.test

%changelog
* Wed Dec 08 2021 Sergey V Turchin <zerg@altlinux.org> 1.58-alt1
- initial build
