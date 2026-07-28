Name: lxpanel-plugin-sensors
Version: 1.9
Release: alt1
Summary: A lxpanel plugin to monitor hardware sensors through lm-sensors.

Group: Graphical desktop/Other
License: GPL-2
Url: https://github.com/danamlund/sensors-lxpanel-plugin
Source0: %name-%version.tar.gz
Patch0: %name-%version-%release.patch
Patch1: alt-optflags.patch

BuildRequires: gcc glib2-devel libgtk+2-devel libsensors3-devel libmenu-cache-devel
BuildRequires: lxde-lxpanel-devel

Requires: lxde-lxpanel

%description
Monitor temperature/voltages/fan speeds in LXDE through lm-sensors

%prep
%setup
%autopatch -p1

%build
OPTFLAGS="%optflags" %make_build

%install
%make install DESTDIR=%buildroot

%files
%doc COPYING README
%_libdir/lxpanel/plugins/*

%changelog
* Tue Jul 28 2026 L.A. Kostis <lakostis@altlinux.ru> 1.9-alt1
- 1.9.
- Enable debuginfo.

* Wed Jun 02 2021 L.A. Kostis <lakostis@altlinux.ru> 1.8-alt1
- Initial build for ALTLinux.

