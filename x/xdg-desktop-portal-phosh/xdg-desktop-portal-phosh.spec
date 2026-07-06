%define _unpackaged_files_terminate_build 1
%def_enable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 0.56
%define beta %nil
%define pfs_ver 0.1.1

%define _name phosh
# phrosh portal
%define _name1 phrosh
%define name1 xdg-desktop-portal-%_name1

%def_enable check

%def_disable bootstrap

Name: xdg-desktop-portal-%_name
Version: %ver_major.1
Release: alt1%beta

Summary: Phosh Desktop Portal
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://gitlab.gnome.org/World/Phosh/xdg-desktop-portal-phosh

Vcs: https://gitlab.gnome.org/World/Phosh/xdg-desktop-portal-phosh.git

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/Phosh/xdg-desktop-portal-phosh/-/archive/v%version/%name-v%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: pfs-%pfs_ver.tar
Source2: %name-%version%beta-cargo.tar

%define xdg_desktop_portal_ver 1.19.1
%define adw_ver 1.6
%define gsds_ver 47

Requires: xdg-desktop-portal >= %xdg_desktop_portal_ver
Requires: libphosh-file-selector >= %pfs_ver

BuildRequires(pre): rpm-macros-meson rpm-build-systemd
BuildRequires: meson rust-cargo /usr/bin/rst2man
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(libpfs-0) >= %pfs_ver
BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(xdg-desktop-portal) >= %xdg_desktop_portal_ver
BuildRequires: gsettings-desktop-schemas-devel >= %gsds_ver

%description
A backend implementation for xdg-desktop-portal that is using
GTK/GNOME/Phosh to provide interfaces that aren't provided by the GTK
portal.

%prep
%setup -n %name-%{?_disable_snapshot:v}%version%beta -a1 %{?_disable_bootstrap:-a2}
cp -r pfs-%pfs_ver subprojects/pfs
%{?_enable_bootstrap:
[ -d .cargo ] || mkdir .cargo
cargo vendor --no-delete -s subprojects/pfs/Cargo.toml \
| sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version%beta-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %name phosh-mobile-portal

%check
%__meson_test

%files -f %name.lang
%_bindir/ptcli
%_libexecdir/%name
%_libexecdir/%_name-thumbnailer
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.%_name.service
%_datadir/xdg-desktop-portal/portals/%_name.portal
%_userunitdir/%name.service
%_userunitdir/%_name-thumbnailer.service
%_datadir/dbus-1/interfaces/mobi.%_name.Thumbnailer.xml
%_datadir/dbus-1/services/mobi.%_name.Thumbnailer.service
%_man1dir/ptcli.1*
%_man8dir/%_name-thumbnailer.8*

%_libexecdir/%name1
%_desktopdir/%name1.desktop
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.%_name1.service
%_datadir/xdg-desktop-portal/portals/%_name1.portal
%_userunitdir/%name1.service

%doc NEWS README*

%exclude %_datadir/glib-2.0/schemas/mobi.phosh.FileSelector.gschema.xml
%exclude %_datadir/locale/*/*/pfs.mo

%changelog
* Mon Jul 06 2026 Yuri N. Sedunov <aris@altlinux.org> 0.56.1-alt1
- 0.56.1

* Fri Jul 03 2026 Yuri N. Sedunov <aris@altlinux.org> 0.56.0-alt1
- 0.56.0

* Sun May 17 2026 Yuri N. Sedunov <aris@altlinux.org> 0.55.0-alt1
- 0.55.0

* Thu May 14 2026 Yuri N. Sedunov <aris@altlinux.org> 0.54.0-alt1
- 0.54.0

* Sun Feb 15 2026 Yuri N. Sedunov <aris@altlinux.org> 0.53.0-alt1
- 0.53.0

* Sat Jan 03 2026 Yuri N. Sedunov <aris@altlinux.org> 0.52.0-alt1
- 0.52.0

* Sun Nov 16 2025 Yuri N. Sedunov <aris@altlinux.org> 0.51.0-alt1
- 0.51.0

* Sun Oct 05 2025 Yuri N. Sedunov <aris@altlinux.org> 0.50.0-alt1
- 0.50.0

* Fri Aug 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.49.0-alt1
- 0.49.0

* Mon Jun 30 2025 Yuri N. Sedunov <aris@altlinux.org> 0.48.0-alt1
- 0.48.0

* Thu Jun 26 2025 Yuri N. Sedunov <aris@altlinux.org> 0.48-alt0.9.rc2
- 0.48_rc2

* Sun May 18 2025 Yuri N. Sedunov <aris@altlinux.org> 0.47.0-alt1
- 0.47.0

* Tue Apr 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.46.0-alt1
- first build for Sisyphus

