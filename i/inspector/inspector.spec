%def_enable snapshot

%define _name inspector
%define ver_major 0.2
%define rdn_name io.github.nokse22.%_name

%def_disable check

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Graphical system information tool
License: GPL-3.0-or-later
Group: System/Kernel and hardware
Url: https://github.com/Nokse22/inspector

Vcs: https://github.com/Nokse22/inspector.git

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

%add_python3_path %_datadir/%name

%define adw_ver 1.5

Requires: typelib(Adw) = 1
Requires: dconf
Requires: coreutils lsblk /usr/bin/ip /usr/bin/lsmem
Requires: /usr/bin/lscpu /usr/bin/lspci /usr/bin/lsusb /usr/bin/lspci

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler /usr/bin/glib-compile-resources
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

%description
Inspector ia a Libadwaita wrapper for various cli commands.
The commands are already installed on any system usually.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%__meson_test

%files -f %name.lang
%attr(755,root,root) %_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/appdata/%rdn_name.appdata.xml
%doc README*

%changelog
* Sun Jul 28 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus (v0.2.0-3-g80e077b)


