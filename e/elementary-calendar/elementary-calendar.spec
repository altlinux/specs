%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.calendar

%def_without check

Name: elementary-calendar
Version: 8.0.0
Release: alt1

Summary: Desktop calendar app designed for elementary OS
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/calendar

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(libedataserver-1.2)
BuildRequires: pkgconfig(geocode-glib-2.0)
BuildRequires: pkgconfig(champlain-0.12)
BuildRequires: pkgconfig(champlain-gtk-0.12)
BuildRequires: pkgconfig(folks)
BuildRequires: pkgconfig(libgeoclue-2.0)
BuildRequires: pkgconfig(libportal)
BuildRequires: pkgconfig(libportal-gtk3)
BuildRequires: vapi(libedataserverui-1.2)
BuildRequires: vapi(granite)
BuildRequires: vapi(folks)

Requires: lib%{name} = %{version}-%{release}

%description
A slim, lightweight calendar app that syncs and manages multiple calendars
in one place.

It features an easy to use yet powerful user interface, provides a daemon
to notify the user about upcoming events and supports synchronization with
most online services.

%package -n lib%{name}
Summary: Library for %name
Group: System/Libraries

%description -n lib%name
%summary

This package contains the shared library used for %name.

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/Other

Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
%summary

This package contains the development files used for %name.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc COPYING README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml
%_libdir/io.elementary.calendar/plugins/CalDAV/libcaldav.so
%_libdir/io.elementary.calendar/plugins/Google/libgoogle.so
%_libdir/io.elementary.calendar/plugins/Web/libweb.so

%files -n lib%{name}
%_libdir/libelementary-calendar.so.0
%_libdir/libelementary-calendar.so.0.1

%files -n lib%{name}-devel
%_libdir/libelementary-calendar.so
%dir %_includedir/elementary-calendar
%_includedir/elementary-calendar/elementary-calendar.h
%_pkgconfigdir/elementary-calendar.pc
%exclude %_vapidir/elementary-calendar.deps
%exclude %_vapidir/elementary-calendar.vapi

%changelog
* Sat Sep 20 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.0-alt1
- Initial build for Sisyphus
