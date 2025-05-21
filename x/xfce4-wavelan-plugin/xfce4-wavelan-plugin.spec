Name: xfce4-wavelan-plugin
Version: 0.7.0
Release: alt1

Summary: This Xfce panel plugin is used to display stats from a wireless LAN interface
License: BSD-2-Clause
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/xfce4-wavelan-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): meson rpm-macros-meson >= 1.3.1-alt1
BuildRequires(pre): rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4util-devel libxfce4panel-gtk3-devel >= 4.16.0 libxfce4ui-gtk3-devel

Requires: xfce4-panel

%define _unpackaged_files_terminate_build 1

%description
Xfce4-wavelan-plugin displays the following information about a WaveLAN device:

Signal state (tells if a carrier signal was detected);
Signal quality (current quality of the carrier signal);
Network name (current SSID of the WaveLAN network).

%prep
%setup
%patch -p1

%build
%meson
%meson_build -v

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS THANKS NEWS COPYING
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Wed May 21 2025 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1
- Switched to meson build.
- Updated to 0.7.0.

* Mon Jan 13 2025 Mikhail Efremov <sem@altlinux.org> 0.6.4-alt1
- Initial build.
