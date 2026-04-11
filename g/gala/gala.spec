%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: gala
Version: 8.4.2
Release: alt2

Summary: Pantheon Window Manager
License: GPL-3.0-or-later AND LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/gala

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(atk-bridge-2.0)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: libmutter-devel
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: vapi(libcanberra)
BuildRequires: vapi(granite)
BuildRequires: /usr/bin/valadoc

Requires: dbus
Requires: dconf
Requires: mutter-gnome

%description
gala is a window & compositing manager based on libmutter. It manages the
various windows a user has open.
It takes care of behaviors such as moving windows around, window switching,
window overview, animating windows, maximization, multiple workspaces,
providing accessibility features like zoom, and more.

%package -n lib%name
Summary: Library to build plugins for Pantheon Window Manager
Group: System/Libraries

%description -n lib%name
%summary
gala is a window & compositing manager based on libmutter. It manages the
various windows a user has open.
It takes care of behaviors such as moving windows around, window switching,
window overview, animating windows, maximization, multiple workspaces,
providing accessibility features like zoom, and more.

This package contains the shared library used for gala.

%package -n lib%name-devel
Summary: Library to build plugins for Pantheon Window Manager (development files)
Group: Development/Other
Requires: lib%name = %{version}-%{release}

%description -n lib%name-devel
gala is a window & compositing manager based on libmutter. It manages the
various windows a user has open.
It takes care of behaviors such as moving windows around, window switching,
window overview, animating windows, maximization, multiple workspaces,
providing accessibility features like zoom, and more.

This package contains the development files used for gala.

%prep
%setup

%build
%meson \
       -Ddocumentation=true \
       -Dsystemd=true
%meson_build

%install
%meson_install

# prevent unmets
cp -pv vapi/libmutter.vapi %buildroot%_vapidir/
cp -pv vapi/libmutter.deps %buildroot%_vapidir/
cp -pv vapi/libmutter-18.vapi %buildroot%_vapidir/
cp -pv vapi/libmutter-18.deps %buildroot%_vapidir/
cp -pv vapi/xfixes-4.0.vapi  %buildroot%_vapidir/

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING HACKING README.md
%_sysconfdir/xdg/io.elementary.desktop.wm.shell
%_bindir/gala
%_bindir/gala-daemon
%_bindir/gala-daemon-gtk3
%_userunitdir/io.elementary.gala.target
%_userunitdir/io.elementary.gala@wayland.service
%_userunitdir/io.elementary.gala@x11.service
%dir %_libdir/gala
%dir %_libdir/gala/plugins
%_libdir/gala/plugins/libgala-pip.so
%_desktopdir/gala-multitaskingview.desktop
%_desktopdir/gala-other.desktop
%_desktopdir/gala-wayland.desktop
%_desktopdir/gala.desktop
%_datadir/glib-2.0/schemas/20_elementary.pantheon.wm.gschema.override
%_datadir/glib-2.0/schemas/org.pantheon.desktop.gala.gschema.xml
%_datadir/metainfo/gala.metainfo.xml
%exclude %_datadir/locale/zh_HANS/LC_MESSAGES/gala.mo
%exclude %_datadir/locale/zh_HANT/LC_MESSAGES/gala.mo

%files -n lib%name
%_libdir/libgala.so.0
%_libdir/libgala.so.0.0.0

%files -n lib%name-devel
%dir %_includedir/gala
%_includedir/gala/gala.h
%_libdir/libgala.so
%_pkgconfigdir/gala.pc
%_vapidir/gala.deps
%_vapidir/gala.vapi
%_vapidir/libmutter*.deps
%_vapidir/libmutter*.vapi
%_vapidir/xfixes-4.0.vapi

%changelog
* Sat Apr 11 2026 Nikolay Strelkov <snk@altlinux.org> 8.4.2-alt2
- Added mutter-gnome package to requires.

* Tue Apr 07 2026 Nikolay Strelkov <snk@altlinux.org> 8.4.2-alt1
- New version 8.4.2.
