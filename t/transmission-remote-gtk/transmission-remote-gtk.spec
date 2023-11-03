Name:    transmission-remote-gtk
Version: 1.6.0
Release: alt1

Summary: GTK remote control for the Transmission BitTorrent client

License: GPL-2.0
Group:   Networking/File transfer
Url:     https://github.com/transmission-remote-gtk/transmission-remote-gtk

Source: %name-%version.tar

BuildRequires: meson
BuildRequires: libjson-glib-devel
BuildRequires: libgtk+3-devel
BuildRequires: libsoup3.0-devel
BuildRequires: libayatana-appindicator3-devel
BuildRequires: libGeoIP-devel
# docs
BuildRequires: perl-podlators

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
%_man1dir/%name.1*

%changelog
* Fri Nov 03 2023 Anton Midyukov <antohami@altlinux.org> 1.6.0-alt1
- Initial build
