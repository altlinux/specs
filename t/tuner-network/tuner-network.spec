%define _pluginsdir %_libdir/tuner/plugins
%define xdg_name ru.ximperlinux.tuner.Network

Name: tuner-network
Version: 0.1.0
Release: alt1
License: GPL-3.0

Summary: Network, Wi-Fi and VPN settings

Group: Graphical desktop/Other

Url: https://gitlab.eterfund.ru/ximperlinux/tuner-network
Vcs: https://gitlab.eterfund.ru/ximperlinux/tuner-network.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: vala

BuildRequires: blueprint-compiler

BuildRequires: pkgconfig(tuner-1)
BuildRequires: gir(Tuner)

BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(libnma-gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(gio-unix-2.0)

Requires: tuner
Requires: NetworkManager-daemon
Requires: gsettings-desktop-schemas-data

%description
Plugin for Tuner that adds wired network, Wi-Fi, VPN and proxy settings.
Connections are managed through NetworkManager independently of the
desktop shell.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_pluginsdir/libnetwork.so
%_pluginsdir/network.plugin
%_datadir/metainfo/%xdg_name.metainfo.xml

%changelog
* Wed Oct 07 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.1.0-alt1
- Initial build
