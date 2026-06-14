%define _unpackaged_files_terminate_build 1

%def_with check

Name: libayatana-appindicator-glib
Version: 2.0.3
Release: alt1

Summary: Ayatana Application Indicators (Glib-2.0-only reimplementation)
License: GPL-3.0
Group: System/Libraries
Url: https://github.com/AyatanaIndicators/libayatana-appindicator-glib

Source: %name-%version.tar

BuildRequires(pre): cmake

BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(vapigen)
BuildRequires: gobject-introspection-devel
BuildRequires: gi-docgen

%if_with check
BuildRequires: ayatana-cmake-modules
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: dbus-test-runner
%endif

%description
A library and indicator to take menus from applications and place them in
the panel.

%package devel
Summary: Ayatana Application Indicators (header files, Glib-2.0-only reimplementation)
Group: Development/C
Requires: %name = %{version}-%{release}

%description devel
A library and indicator to take menus from applications and place them in
the panel.

This package contains files that are needed to build applications.

%package doc
Summary: Ayatana Application Indicators (Glib-2.0-only reimplementation, doc files)
Group: Documentation
BuildArch: noarch

%description doc
A library and indicator to take menus from applications and place them in
the panel.

This package contains developer documentation.

%prep
%setup

%build
%cmake \
%if_with check
       -DENABLE_TESTS=ON
%else
       -DENABLE_TESTS=OFF
%endif

%cmake_build

%install
%cmake_install

%check
%ctest -j1 -VV

%files
%doc AUTHORS COPYING README.md
%_libdir/libayatana-appindicator-glib.so.2*
%_libdir/girepository-1.0/AyatanaAppIndicatorGlib-2.0.typelib

%files devel
%dir %_includedir/libayatana-appindicator-glib/
%_includedir/libayatana-appindicator-glib/ayatana-appindicator-enum-types.h
%_includedir/libayatana-appindicator-glib/ayatana-appindicator.h
%_libdir/libayatana-appindicator-glib.so
%_libdir/pkgconfig/ayatana-appindicator-glib.pc
%_datadir/gir-1.0/AyatanaAppIndicatorGlib-2.0.gir
%_datadir/vala/vapi/ayatana-appindicator-glib.deps
%_datadir/vala/vapi/ayatana-appindicator-glib.vapi

%files doc
%_datadir/doc/libayatana-appindicator-glib-dev/

%changelog
* Sun Jun 14 2026 Nikolay Strelkov <snk@altlinux.org> 2.0.3-alt1
- Initial build for Sisyphus
