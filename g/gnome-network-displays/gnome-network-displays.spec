%define commit 589d979f33b4873f9e5a5234e505566b420efdfe
%define commit_short %(echo %commit | head -c 6)

Name: gnome-network-displays
Summary: Miracast streaming GUI
License: GPL-3.0
Group: Graphical desktop/GNOME
Version: 0.90.5
Release: alt0.git%{commit_short}.1
Url: https://gitlab.gnome.org/GNOME/gnome-network-displays
Source0: %name.tar
Patch0001: 0001-Add-Russian-localization.patch
Patch0002: 0002-Localize-application-name.patch

BuildRequires: gettext-devel
BuildRequires: meson
BuildRequires: gcc
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libnm) >= 1.15.1
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(gstreamer-rtsp-server-1.0)

%description
Miracast streaming GUI.
Choose a wireless display and stream your desktop to it.

%prep
%setup -q -n %name
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc README.md COPYING
%_bindir/gnome-network-displays
%_datadir/applications/org.gnome.NetworkDisplays.desktop
%_datadir/glib-2.0/schemas/org.gnome.NetworkDisplays.gschema.xml
%_datadir/icons/hicolor/scalable/apps/org.gnome.NetworkDisplays.svg
%_datadir/icons/hicolor/symbolic/apps/org.gnome.NetworkDisplays-symbolic.svg
%_datadir/metainfo/org.gnome.NetworkDisplays.appdata.xml
%_prefix/lib/firewalld/zones/P2P-WiFi-Display.xml

%changelog
* Tue Mar 22 2022 Mikhail Novosyolov <mikhailnov@altlinux.org> 0.90.5-alt0.git589d97.1
- Initial build of git master snapshot, commit 589d979f33b
- Added Russian localization, PRed to upstream:
  https://gitlab.gnome.org/GNOME/gnome-network-displays/-/merge_requests/162
