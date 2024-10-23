%def_enable snapshot

%define ver_major 0.8
%define rdn_name app.drey.Warp

%define optflags_lto %nil

%def_enable qr
%def_enable check
%def_disable bootstrap

Name: warp
Version: %ver_major.0
Release: alt1

Summary: Fast and secure file transfer tool
License: GPL-3.0-or-later
Group: Networking/File transfer
Url: https://apps.gnome.org/Warp

Vcs: https://gitlab.gnome.org/World/warp.git

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

#error: failed to run custom build command for `ring v0.16.20`
ExcludeArch: ppc64le

%define glib_ver 2.78
%define gtk_ver 4.16
%define adwaita_ver 1.6

Requires: yelp
%{?_enable_qr:Requires: gst-plugins-bad1.0}

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: yelp-tools
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(dbus-1)
%{?_enable_qr:BuildRequires: pkgconfig(zbar) pkgconfig(gstreamer-plugins-bad-1.0)}
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils clippy}
BuildRequires: license-list-data

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
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

ln -s %_datadir/license-list-data vendor/license/license-list-data

%build
%meson \
    %{subst_enable_meson_feature qr qr-code-scanning}
%nil
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
#%dir %_datadir/%name/
# ~600M
#%_datadir/%name/licenses.json
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Wed Oct 23 2024 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Sat Sep 21 2024 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt2
- updated to v0.7.0-38-gcf65284

* Sat Apr 13 2024 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1.1
- explicitly enabled qr-code support (ALT #50014)

* Sun Mar 24 2024 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Tue Dec 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt1
- 0.6.2

* Fri Oct 13 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Fri Sep 29 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- updated to v0.6.0-3-g3ec6f21

* Wed Jun 21 2023 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- first build for Sisyphus


