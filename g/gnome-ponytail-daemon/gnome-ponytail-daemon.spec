Name: gnome-ponytail-daemon
Version: 0.0.11
Release: alt1.git9dd3bda

Summary: Helper daemon for dogtail on GNOME Wayland

License: GPL-2.0-or-later
Group: Development/Tools
Url: https://gitlab.gnome.org/ofourdan/gnome-ponytail-daemon

# Source-url: https://gitlab.gnome.org/ofourdan/gnome-ponytail-daemon/-/archive/9dd3bda1816de216219232b8f6baec9f2d423ec6/gnome-ponytail-daemon-9dd3bda1816de216219232b8f6baec9f2d423ec6.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libei-1.0) pkgconfig(xkbcommon)
BuildRequires: pkgconfig(systemd)

%description
GNOME Ponytail Daemon is a sort of bridge for dogtail for GNOME on Wayland.
It uses the Mutter RemoteDesktop and ScreenCast D-Bus APIs to emulate
pointer and keyboard input and to look up windows, so that dogtail
can drive applications in a Wayland session.

%package -n python3-module-ponytail
Summary: Python module for gnome-ponytail-daemon
Group: Development/Python3
BuildArch: noarch
Requires: %name = %EVR

%description -n python3-module-ponytail
Python module for D-Bus interactions with gnome-ponytail-daemon interfaces.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%_libexecdir/gnome-ponytail-daemon
%_userunitdir/gnome-ponytail-daemon.service
%_datadir/dbus-1/services/org.gnome.Ponytail.service

%files -n python3-module-ponytail
%doc examples/*.py
%python3_sitelibdir_noarch/ponytail/

%changelog
* Wed Oct 07 2026 Vitaly Lipatov <lav@altlinux.ru> 0.0.11-alt1.git9dd3bda
- initial build for Sisyphus (git snapshot 9dd3bda after 0.0.11)

