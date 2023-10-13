%def_enable snapshot

%define ver_major 0.6
%define rdn_name app.drey.Warp

%define optflags_lto %nil

%def_disable bootstrap

Name: warp
Version: %ver_major.1
Release: alt1

Summary: Fast and secure file transfer tool
License: GPL-3.0
Group: Networking/File transfer
Url: https://gitlab.gnome.org/World/warp

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/warp.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

#error: failed to run custom build command for `ring v0.16.20`
ExcludeArch: ppc64le

%define glib_ver 2.66
%define gtk_ver 4.10
%define adwaita_ver 1.4

Requires: yelp

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: yelp-tools
BuildRequires: /usr/bin/appstream-util desktop-file-utils
#BuildRequires: /usr/bin/appstreamcli
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(dbus-1)

%description
Warp allows you to securely send files to each other via the internet or
local network by exchanging a word-based code.

The best transfer method will be determined using the Magic
Wormhole (https://github.com/magic-wormhole/magic-wormhole#magic-wormhole)
protocol which includes local network transfer if possible. File
transfers are encrypted.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Fri Oct 13 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Fri Sep 29 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- updated to v0.6.0-3-g3ec6f21

* Wed Jun 21 2023 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- first build for Sisyphus


