Name: xfce4-wavelan-plugin
Version: 0.6.4
Release: alt1

Summary: This Xfce panel plugin is used to display stats from a wireless LAN interface
License: BSD-2-Clause
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/xfce4-wavelan-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4panel-gtk3-devel >= 4.16.0 libxfce4ui-gtk3-devel

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
%xfce4reconf
%configure \
	--enable-debug=minimal
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS THANKS NEWS COPYING
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Mon Jan 13 2025 Mikhail Efremov <sem@altlinux.org> 0.6.4-alt1
- Initial build.
