%def_enable snapshot
%define ver_major 3.7
%define rdn_name io.gitlab.adhami3310.Impression

%def_disable bootstrap
%def_enable check

Name: impression
Version: %ver_major.0
Release: alt1

Summary: Impression is a tool to create bootable drives
License: GPL-3.0-or-later
Group: System/Configuration/Other
Url: https://gitlab.com/adhami3310/Impression

Vcs: https://gitlab.com/adhami3310/Impression.git

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define gtk_ver 4.10
%define adwaita_ver 1.5

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver gir(Adw)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(dbus-1)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

%description
A tool to write images to portable drives like flash drives or memory
cards.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
cat << _EOF_\
> %buildroot/%_datadir/glib-2.0/schemas/%rdn_name.gschema.override
[io.gitlab.adhami3310.Impression]
downloadable-distros=[('altlinux.org', nothing, false)]
_EOF_

%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/glib-2.0/schemas/%rdn_name.gschema.override
%_datadir/dbus-1/services/%rdn_name.service
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc PRESS* README*

%changelog
* Mon Apr 13 2026 Yuri N. Sedunov <aris@altlinux.org> 3.7.0-alt1
- v3.7.0-1-g6aed634

* Tue Jan 13 2026 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Wed Dec 31 2025 Yuri N. Sedunov <aris@altlinux.org> 3.5.6-alt1
- 3.5.6

* Fri Dec 05 2025 Yuri N. Sedunov <aris@altlinux.org> 3.5.5-alt1
- 3.5.5

* Sat Nov 15 2025 Yuri N. Sedunov <aris@altlinux.org> 3.5.4-alt1
- 3.5.4

* Mon Oct 27 2025 Yuri N. Sedunov <aris@altlinux.org> 3.5.3-alt1
- 3.5.3
- removed useless add-alt-to-list.patch
  and set "downloadable-distros" via dconf instead

* Tue Sep 02 2025 Yuri N. Sedunov <aris@altlinux.org> 3.5.1-alt1
- 3.5.1

* Sun Jul 27 2025 Yuri N. Sedunov <aris@altlinux.org> 3.5.0-alt1
- 3.5.0

* Wed Apr 16 2025 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Jan 28 2025 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt2
- qualimock@:
  rewrite osinfo-db parser to support multiple distro variants for one OS version
  add ALT Linux to GOOD_DISTROS list

* Sat Sep 21 2024 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1
- 3.3.0

* Tue Apr 16 2024 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu Mar 14 2024 Yuri N. Sedunov <aris@altlinux.org> 3.1.0-alt1
- 3.1.0

* Mon Feb 19 2024 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt2
- updated to v3.0.1-15-ge78b301

* Tue Nov 07 2023 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Nov 06 2023 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt1
- 3.0

* Mon Sep 11 2023 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt1
- first build for Sisyphus (v2.1-15-g8840b25)


