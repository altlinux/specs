%def_disable snapshot

%define ver_major 2026.3
%define rdn_name io.github.giantpinkrobots.varia

%def_enable check

Name: varia
Version: %ver_major.27
Release: alt1

Summary: Quick and efficient download manager
License: MPL-2.0
Group: Networking/WWW
Url: https://github.com/giantpinkrobots/varia

Vcs: https://github.com/giantpinkrobots/varia.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Patch1: %name-2026.3.27-alt-fix-icons-install.patch

%define adw_ver 1.6

Requires: /usr/bin/aria2p /usr/bin/aria2c
Requires: python3-module-pygobject3
Requires: typelib(Adw) = 1 libadwaita >= %adw_ver
Requires: yt-dlp
%ifnarch %ix86
Requires: deno
%endif
Requires: ffmpeg
Requires: p7zip
Requires: dconf

#BuildArch: noarch
ExclusiveArch: x86_64 aarch64

%add_python3_path %_datadir/%name

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir rpm-build-xdg
BuildRequires: meson yelp-tools
BuildRequires: pkgconfig(libadwaita-1)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

%description
Varia is a simple download manager that conforms to the latest
Libadwaita design guidelines, integrating nicely with GNOME. It utilizes
aria2 and yt-dlp to handle regular files, torrents and video/audio
stream downloads.


%prep
%setup
%patch1 -b .icons

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name

%check
%__meson_test

%files -f %name.lang
%attr(0755,root,root) %_bindir/%name
%_bindir/%name-py.py
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/*/*.svg
%_iconsdir/apps/io.github.giantpinkrobots.bootqt.png
%_xdgmimedir/packages/%rdn_name.mime.xml
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Fri May 01 2026 Yuri N. Sedunov <aris@altlinux.org> 2026.3.27-alt1
- 2026.3.27

* Fri Jan 09 2026 Yuri N. Sedunov <aris@altlinux.org> 2026.1.5-alt1
- 2026.1.5

* Wed Oct 15 2025 Yuri N. Sedunov <aris@altlinux.org> 2025.10.14-alt1
- 2025.10.14

* Sat Jul 19 2025 Yuri N. Sedunov <aris@altlinux.org> 2025.7.19-alt1
- 2025.7.19

* Thu May 15 2025 Yuri N. Sedunov <aris@altlinux.org> 2025.5.14-alt1
- 2025.5.14

* Wed Apr 23 2025 Yuri N. Sedunov <aris@altlinux.org> 2025.4.22-alt1
- 2025.4.22

* Fri Apr 04 2025 Yuri N. Sedunov <aris@altlinux.org> 2025.4.3-alt1
- 2025.4.3

* Sat Jan 25 2025 Yuri N. Sedunov <aris@altlinux.org> 2025.1.24-alt1
- 2025.1.24

* Fri Nov 08 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.11.7-alt1
- updated to v2024.11.7-1

* Wed May 08 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.5.7-alt1
- 2024.5.7

* Wed Mar 20 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.3.20-alt1
- 2024.3.20

* Tue Mar 05 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.2.29.2-alt1
- 2024.2.29-2

* Wed Feb 14 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.2.6-alt1
- first build for Sisyphus (v2024.2.6-5-g6fb6073)


