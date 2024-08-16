%define commit 976cd7cb78b41ffdd5f79c56cd5a7dc358359f1f
%define commit_short %(echo %commit | head -c 6)

%define rdn_name org.gnome.NetworkDisplays

%def_enable check

Name: gnome-network-displays
Version: 0.93.0
Release: alt0.git%{commit_short}.1

Summary: Miracast streaming GUI
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/GNOME/gnome-network-displays

Vcs: https://gitlab.gnome.org/GNOME/gnome-network-displays.git

Source0: %name.tar
#Patch0: %name-%version-%release.patch

#Patch0001: 0001-Add-Russian-localization.patch
#Patch0002: 0002-Localize-application-name.patch

%define nm_ver 1.15.1
%define gst_ver 1.14

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libportal-gtk4)
BuildRequires: pkgconfig(libnm) >= %nm_ver
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(gstreamer-rtsp-server-1.0) > %gst_ver
BuildRequires: pkgconfig(avahi-client)
BuildRequires: pkgconfig(avahi-gobject)
BuildRequires: pkgconfig(libprotobuf-c)
BuildRequires: pkgconfig(json-glib-1.0)
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli}

%description
Miracast streaming GUI.
Choose a wireless display and stream your desktop to it.

%prep
%setup -q -n %name
#%%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
#%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/scalable/apps/%rdn_name.svg
%_iconsdir/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%_datadir/metainfo/%rdn_name.appdata.xml
%_prefix/lib/firewalld/zones/P2P-WiFi-Display.xml
%doc README.md COPYING

%changelog
* Fri Aug 16 2024 Yuri N. Sedunov <aris@altlinux.org> 0.93.0-alt0.git976cd7.1
- updated to 0.93.0-10-g976cd7c (ALT #49118)

* Tue Mar 22 2022 Mikhail Novosyolov <mikhailnov@altlinux.org> 0.90.5-alt0.git589d97.1
- Initial build of git master snapshot, commit 589d979f33b
- Added Russian localization, PRed to upstream:
  https://gitlab.gnome.org/GNOME/gnome-network-displays/-/merge_requests/162
