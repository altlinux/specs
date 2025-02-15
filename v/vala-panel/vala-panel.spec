%define _unpackaged_files_terminate_build 1

Name: vala-panel
Version: 24.05
Release: alt1

Summary: Desktop panel written in Vala and GTK+ 3
License: LGPLv3
Group: Graphical desktop/Other
Url: https://gitlab.com/vala-panel-project/vala-panel

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: meson
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildRequires: pkgconfig(libwnck-3.0)
BuildRequires: desktop-file-utils

%description
Vala Panel is a rewrite of SimplePanel. It is a GTK+ 3 desktop panel
written in Vala and based on ideas from LXPanel.

Vala Panel can be extended with plugins that provide application menus,
clock, tasklist, system tray, etc.

%package devel
Group: Development/Other
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
Vala Panel is a rewrite of SimplePanel. It is a GTK+ 3 desktop panel
written in Vala and based on ideas from LXPanel.

This package contains header files for building plugins or window
managers with vala-panel support.

%prep
%setup

%build
%meson \
       -Dwnck=enabled \
       -Dplatforms='wayland,x11'
%meson_build

%install
%meson_install

rm -rfv %{buildroot}%{_datadir}/vala-panel/doc

%find_lang %name

%files -f %name.lang
%doc README.md LICENSE
%config %_sysconfdir/xdg/vala-panel/
%_bindir/vala-*
%_libdir/libvalapanel.so.*
%dir %_libdir/vala-panel
%dir %_libdir/vala-panel/applets
%_libdir/vala-panel/applets/*.so
%_datadir/appdata/org.valapanel.application.appdata.xml
%_datadir/applications/org.valapanel.application.desktop
%_datadir/glib-2.0/schemas/*.xml
%_datadir/icons/hicolor/96x96/apps/vala-panel.png
%_datadir/icons/hicolor/scalable/apps/vala-panel.svg
%_man1dir/*
%dir %_datadir/vala-panel
%dir %_datadir/vala-panel/applets
%_datadir/vala-panel/applets/*.plugin
%dir %_datadir/vala-panel/images
%_datadir/vala-panel/images/background.png
%_libdir/girepository-1.0/ValaPanel-*.typelib

%files devel
%doc README.md LICENSE
%dir %_includedir/vala-panel
%_includedir/vala-panel/*.h
%_libdir/libvalapanel.so
%_libdir/pkgconfig/vala-panel.pc
%_datadir/vala/vapi/vala-panel.*
%_datadir/gir-1.0/ValaPanel-*.gir

%changelog
* Sat Feb 15 2025 Nikolay Strelkov <snk@altlinux.org> 24.05-alt1
- Initial build for Sisyphus
