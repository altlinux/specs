%define _libexecdir %_prefix/libexec
%define ver_major 3.15
%define _name org.gnome.BatteryBench

Name: gnome-battery-bench
Version: %ver_major.4
Release: alt1

Summary: Measure power usage in defined scenarios
Group: Monitoring
License: GPLv2+
Url: https://wiki.gnome.org/Projects/BatteryLife

#Source: http://people.freedesktop.org/~hughsient/releases/%name-%version.tar.xz
Source: %name-%version.tar

Requires: powertop polkit

%define gtk_ver 3.14.0

BuildRequires: gnome-common intltool asciidoc-a2x xmlto yelp-tools
BuildRequires: libgtk+3-devel >= %gtk_ver libjson-glib-devel
BuildRequires: libevdev-devel libpolkit-devel libXi-devel libXtst-devel

%description
This application is designed for measuring power usage. It does it by
recording the reported battery statistics as it replays recorded event
logs, and then using that to estimate power consumption and total
battery lifetime.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/gbb
%_libexecdir/%name-helper
%_sysconfdir/dbus-1/system.d/%_name.Helper.conf
%_desktopdir/%_name.desktop
%_datadir/%name/
%_datadir/dbus-1/services/%_name.service
%_datadir/dbus-1/system-services/%_name.Helper.service
%_datadir/polkit-1/actions/%_name.Helper.policy
#%_datadir/appdata/%_name.appdata.xml
%_man1dir/gbb.1.*
%doc README

%changelog
* Thu Jan 29 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.4-alt1
- 3.15.4

* Tue Jan 20 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.0-alt1
- first preview for Sisyphus



