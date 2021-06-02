Name: lxpanel-plugin-sensors
Version: 1.8
Release: alt1
Summary: A lxpanel plugin to monitor hardware sensors through lm-sensors.

Group: Graphical desktop/Other
License: GPL-2
Url: https://github.com/danamlund/sensors-lxpanel-plugin
Source0: %name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires: gcc glib2-devel libgtk+2-devel libsensors3-devel libmenu-cache-devel
BuildRequires: lxde-lxpanel-devel

Requires: lxde-lxpanel

%description
Monitor temperature/voltages/fan speeds in LXDE through lm-sensors

%prep
%setup
%patch -p1

%build
%make_build

%install
%make install DESTDIR=%buildroot

%files
%doc COPYING README
%_libdir/lxpanel/plugins/*

%changelog
* Wed Jun 02 2021 L.A. Kostis <lakostis@altlinux.ru> 1.8-alt1
- Initial build for ALTLinux.

