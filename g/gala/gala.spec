%define _name gala
%define rdn_name org.pantheon.desktop.%_name
%define xdg_name io.elementary.desktop.wm
%define service_name io.elementary.gala

Name: %_name
Version: 8.1.0
Release: alt1

Summary: Pantheon Window Manager
Group: Graphical desktop/Other
License: GPL-3.0-or-later
Url: https://launchpad.net/%name

Vcs: https://github.com/elementary/gala.git

Source: %name-%version.tar

%define glib_ver 2.74
%define mutter_api_ver 15

Requires: dconf

BuildRequires(pre): rpm-macros-meson rpm-build-vala rpm-build-xdg
BuildRequires: meson vala-tools
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(libmutter-%mutter_api_ver)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(atk-bridge-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: vapi(granite)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: vapi(libcanberra)
BuildRequires: pkgconfig(systemd)

%description
Gala is a window compositing manager based on libmutter and designed by
elementary for use with Pantheon.

%package -n lib%name
Summary: Shared library for Gala
Group: System/Libraries

%description -n lib%name
This package contains shared library needed to run Gala.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package contains headers and development libraries for lib%name

%package -n lib%name-vala
Summary: Vala language bindings for the Gala library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %EVR

%description -n lib%name-vala
This package provides Vala language bindings for the Gala library.


%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

## install libmutter.{vapi,deps}, xfixes-4.0.vapi to resolve dependencies
install -p -m644 vapi/libmutter{,-%mutter_api_ver}.{vapi,deps} %buildroot%_vapidir/
install -p -m644 vapi/xfixes-4.0.vapi  %buildroot%_vapidir/

%find_lang %name

%files -f %name.lang
%_xdgconfigdir/%xdg_name.shell
%_bindir/%name-daemon
%_bindir/%name-daemon-gtk3
%_bindir/%name
%_userunitdir/%service_name.target
%_userunitdir/%{service_name}@wayland.service
%_userunitdir/%{service_name}@x11.service
%_desktopdir/%name.desktop
%_desktopdir/%name-other.desktop
%_desktopdir/%name-multitaskingview.desktop
%_desktopdir/%name-wayland.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/glib-2.0/schemas/20_elementary.pantheon.wm.gschema.override
%_datadir/metainfo/%name.metainfo.xml
%doc README* HACKING

%files -n lib%name
%_libdir/lib%name.so.*
%dir %_libdir/%name/
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/lib%name-pip.so

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%files -n lib%name-vala
%_vapidir/%name.deps
%_vapidir/%name.vapi
%_vapidir/libmutter*.deps
%_vapidir/libmutter*.vapi
%_vapidir/xfixes-4.0.vapi


%changelog
* Mon Jan 13 2025 Yuri N. Sedunov <aris@altlinux.org> 8.1.0-alt1
- 8.1.0-4-g56d8cafe

* Sun Dec 08 2024 Yuri N. Sedunov <aris@altlinux.org> 8.0.4-alt0.5
- 8.0.4-15-g4f38089f

* Fri Mar 24 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt0.2
- rebuilt with new mutter library

* Wed Mar 30 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt0.1
- 0.3.0 (rev.512)
- built against libplank.so.1

* Thu Sep 24 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt0.3
- rebuilt against libgnome-desktop-3.so.12

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt0.2
- new -vala subpackage

* Fri Sep 11 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt0.1
- 0.2.0_r479

* Mon Nov 25 2013 Igor Zubkov <icesik@altlinux.org> 0.1-alt1.r363
- build for Sisyphus

