%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.wingpanel

Name: wingpanel
Version: 8.0.4
Release: alt1.git.8bc5eeb

Summary: Stylish top panel that holds indicators and spawns an application launcher
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/wingpanel

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gdk-wayland-3.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(granite-7)
BuildRequires: libmutter-devel
BuildRequires: pkgconfig(gala)
BuildRequires: vapi(granite)
BuildRequires: pkgconfig(gtk4-wayland)

%description
A replacement for the traditional GNOME Panel, designed to be a lightweight
container for system/application indicators and notification icons.
Designed by elementary Project.

%package -n lib%name
Summary: Shared library for Wingpanel
Group: System/Libraries

%description -n lib%name
A replacement for the traditional GNOME Panel, designed to be a lightweight
container for system/application indicators and notification icons.
Designed by elementary Project.

This package contains the shared library used for wingpanel.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%{name} = %version-%release

%description -n lib%name-devel
A replacement for the traditional GNOME Panel, designed to be a lightweight
container for system/application indicators and notification icons.
Designed by elementary Project.

This package contains the development files used for wingpanel.

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

%files -f %appname.lang
%doc CONTRIBUTING.md COPYING README.md
%_bindir/%appname
%_libdir/gala/plugins/libwingpanel-interface.so
%_desktopdir/%{appname}.desktop
%_datadir/glib-2.0/schemas/*.wingpanel.gschema.xml
%_iconsdir/hicolor/*/apps/%{appname}*.svg
%_datadir/metainfo/%{appname}.metainfo.xml

%files -n lib%name
%_libdir/lib%{name}-9.so.8
%_libdir/lib%{name}-9.so.8.0.*

%files -n lib%name-devel
%dir %_includedir/%{name}-9
%_includedir/%{name}-9/%{name}-9.h
%_libdir/lib%{name}-9.so
%_pkgconfigdir/%{name}-9.pc
%_vapidir/%{name}-9.deps
%_vapidir/%{name}-9.vapi

%changelog
* Tue Apr 07 2026 Nikolay Strelkov <snk@altlinux.org> 8.0.4-alt1.git.8bc5eeb
- Initial build for Sisyphus
