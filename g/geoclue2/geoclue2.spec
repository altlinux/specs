%define _name geoclue
%define ver_major 2.3
%define api_ver 2.0
%define _libexecdir %_prefix/libexec

%def_disable gtk_doc

Name: %{_name}2
Version: %ver_major.0
Release: alt1

Summary: The Geoinformation Service
Group: System/Libraries
License: LGPLv2
Url: http://geoclue.freedesktop.org/

Source: http://www.freedesktop.org/software/%_name/releases/%ver_major/%_name-%version.tar.xz

%define glib_ver 2.34
%define mm_ver 1.0
%define geoip_ver 1.5.1
%define soup_ver 2.42

BuildRequires: intltool yelp-tools gtk-doc libgio-devel >= %glib_ver
BuildRequires: libjson-glib-devel libsoup-devel >= %soup_ver libmm-glib-devel >= %mm_ver
BuildRequires: libdbus-devel libavahi-glib-devel libnotify-devel systemd-devel
# for check
BuildRequires: /proc dbus-tools-gui

%description
GeoClue is a D-Bus geoinformation service. The goal of the Geoclue
project is to make creating location-aware applications as simple as
possible.

%package devel
Summary: Development package for GeoClue
Group: Development/C
Requires: %name = %version-%release

%description devel
Files for development with GeoClue.

%package devel-doc
Summary: Developer documentation for GeoClue
Group: Development/C
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
Developer documentation for GeoClue.

%package demo
Summary: Demo programs for GeoClue
Group: Development/C
Requires: %name = %version-%release

%description demo
This package contains demo programs for GeoClue.


%prep
%setup -n %_name-%version
rm -f demo/*.desktop.in


%build
%autoreconf
%configure --disable-static \
	--with-dbus-service-user=%_name \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{?_enable_network_manager:--enable-network-manager} \
	--with-dbus-service-user=%_name \
	--enable-demo-agent
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_localstatedir/%_name

%check
# https://bugs.freedesktop.org/show_bug.cgi?id=68395
#%make check

%pre
%_sbindir/groupadd -r -f %_name
%_sbindir/useradd -r -g %_name -d %_localstatedir/%_name -s /dev/null \
    -c 'User for GeoClue service' %_name >/dev/null 2>&1 ||:

%files
%_libexecdir/%_name
%_sysconfdir/dbus-1/system.d/org.freedesktop.GeoClue2.conf
%_sysconfdir/dbus-1/system.d/org.freedesktop.GeoClue2.Agent.conf
%_datadir/dbus-1/system-services/org.freedesktop.GeoClue2.service
%_datadir/dbus-1/interfaces/org.freedesktop.GeoClue2.Agent.xml
%_datadir/dbus-1/interfaces/org.freedesktop.GeoClue2.xml
%systemd_unitdir/%_name.service
%config %_sysconfdir/%_name/%_name.conf
%attr(1770, %_name, %_name) %dir %_localstatedir/%_name
%doc README NEWS

%files devel
%_libdir/pkgconfig/%_name-%api_ver.pc

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name/
%endif

%files demo
%_libexecdir/%_name-%api_ver/demos/
%_datadir/applications/*.desktop


%changelog
* Sat Sep 19 2015 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sun Apr 26 2015 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Fri Jan 09 2015 Yuri N. Sedunov <aris@altlinux.org> 2.1.10-alt1
- 2.1.10

* Fri Jun 20 2014 Yuri N. Sedunov <aris@altlinux.org> 2.1.9-alt1
- 2.1.9

* Mon Apr 21 2014 Yuri N. Sedunov <aris@altlinux.org> 2.1.8-alt1
- 2.1.8

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 2.1.7-alt1
- 2.1.7

* Fri Mar 07 2014 Yuri N. Sedunov <aris@altlinux.org> 2.1.6-alt1
- 2.1.6

* Fri Dec 13 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt2
- create new geoclue group and user in %%pre

* Wed Oct 09 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0
- new -devel-doc subpackage

* Tue Sep 17 2013 Yuri N. Sedunov <aris@altlinux.org> 1.99.4-alt1
- 1.99.4

* Sun Sep 01 2013 Yuri N. Sedunov <aris@altlinux.org> 1.99.2-alt1
- first build for Sisyphus

