Name:    transmission-remote-gtk
Version: 1.7.1
Release: alt1

Summary: GTK remote control for the Transmission BitTorrent client

License: GPL-2.0
Group:   Networking/File transfer
URL:     https://github.com/transmission-remote-gtk/transmission-remote-gtk
VCS:     https://github.com/transmission-remote-gtk/transmission-remote-gtk

Source: %name-%version.tar

BuildRequires: meson
BuildRequires: libjson-glib-devel
BuildRequires: libgtk+3-devel
BuildRequires: libsoup3.0-devel
BuildRequires: libayatana-appindicator3-devel
# man's
BuildRequires: %_bindir/rst2man

%description
transmission-remote-gtk is a GTK client for remote management of the
Transmission BitTorrent client, using its HTTP RPC protocol.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS ChangeLog COPYING
%_bindir/%name
%_desktopdir/io.github.TransmissionRemoteGtk.desktop
%_datadir/metainfo/io.github.TransmissionRemoteGtk.appdata.xml
%_iconsdir/hicolor/*/apps/%name.*
%_man1dir/%name.1.*

%changelog
* Sun Mar 15 2026 Anton Midyukov <antohami@altlinux.org> 1.7.1-alt1
- New version 1.7.1.

* Sat Dec 27 2025 Anton Midyukov <antohami@altlinux.org> 1.7.0-alt1
- New version 1.7.0.

* Fri Nov 03 2023 Anton Midyukov <antohami@altlinux.org> 1.6.0-alt1
- Initial build
