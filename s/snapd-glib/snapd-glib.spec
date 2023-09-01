
%def_enable soup2

%if_enabled soup2
%define api %nil
%define sffx %nil
%else
%define api 2
%define sffx -%{api}
%endif
%define sover 1
%define libsnapd_qt libsnapd-qt%{sffx}%{sover}
%define libsnapd_glib libsnapd-glib%{sffx}%{sover}
Name: snapd-glib
Version: 1.64
Release: alt1

Group: System/Libraries
Summary: Library providing a GLib interface to snapd
License: LGPL-2.0-or-later
Url: https://github.com/snapcore/%name

Source: snapd-glib-%version.tar
Patch1: alt-opt-soup2.patch

BuildRequires: gtk-doc
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gobject-introspection-devel
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
%if_enabled soup2
BuildRequires: pkgconfig(libsoup-2.4)
%else
BuildRequires: pkgconfig(libsoup-3.0)
%endif
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
%if_enabled soup2
%patch1 -p1
%endif

%build
%meson
%meson_build

%install
%meson_install

%files -n %libsnapd_glib
%doc NEWS COPYING*
%_libdir/libsnapd-glib%{sffx}.so.%sover
%_libdir/libsnapd-glib%{sffx}.so.*
%_libdir/girepository-1.0/Snapd*.typelib

%files devel
%doc %_datadir/gtk-doc/html/snapd-glib/
%_includedir/snapd-glib%{sffx}/
%_libdir/libsnapd-glib%{sffx}.so
%_libdir/pkgconfig/snapd-glib%{sffx}.pc
%_datadir/vala/vapi/snapd-glib%{sffx}.*
%_datadir/gir-1.0/Snapd*.gir

#%files tests
#%_libexecdir/installed-tests/snapd-glib/*-glib
#%_datadir/installed-tests/snapd-glib/*-glib.test

%files -n %libsnapd_qt
%_libdir/libsnapd-qt%{sffx}.so.%sover
%_libdir/libsnapd-qt%{sffx}.so.*

%files -n qt5-qml-snapd
%_qt5_qmldir/Snapd%{api}/

%files -n snapd-qt-devel
%_includedir/snapd-qt%{sffx}/
%_libdir/libsnapd-qt%{sffx}.so
%_libdir/pkgconfig/snapd-qt%{sffx}.pc
%_libdir/cmake/Snapd%{api}/

#%files -n snapd-qt-tests
#%_libexecdir/installed-tests/snapd-glib/*-qt
#%_datadir/installed-tests/snapd-glib/*-qt.test

%changelog
* Thu Aug 31 2023 Sergey V Turchin <zerg@altlinux.org> 1.64-alt1
- new version (closes: 47349)

* Fri Jun 03 2022 Sergey V Turchin <zerg@altlinux.org> 1.60-alt1
- new version

* Wed Dec 08 2021 Sergey V Turchin <zerg@altlinux.org> 1.58-alt1
- initial build
