%define _name geoclue
%define ver_major 2.1
%define api_ver 2.0
%define _libexecdir %_prefix/libexec

%def_enable server
%def_enable gtk_doc

Name: %{_name}2
Version: %ver_major.6
Release: alt1

Summary: The Geoinformation Service
Group: System/Libraries
License: LGPLv2
Url: http://geoclue.freedesktop.org/

Source: http://www.freedesktop.org/software/%_name/releases/%ver_major/%_name-%version.tar.xz
Patch: geoclue-2.1.2-alt-demo.patch

%define glib_ver 2.34
%define nm_ver 0.9.9.0
%define mm_ver 1.0
%define geoip_ver 1.5.1

BuildRequires: intltool yelp-tools gtk-doc libgio-devel >= %glib_ver
BuildRequires: libjson-glib-devel libsoup-devel
BuildRequires: libnm-glib-devel >= %nm_ver libmm-glib-devel >= %mm_ver
BuildRequires: libxml2-devel libnotify-devel systemd-devel
%{?_enable_server:BuildRequires: libGeoIP-devel >= %geoip_ver}
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
%setup -q -n %_name-%version
#%%patch
rm -f demo/*.desktop.in
#subst 's/\(libsoup\) /\1-2.4 /' src/%_name-%api_ver.pc.in

%build
%autoreconf
%configure --disable-static \
	%{?_enable_server:--enable-geoip-server=yes} \
	--with-dbus-service-user=%_name \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
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
    -c 'User for GeoClue service' %_name >/dev/null || :

%files
%_bindir/geoip-lookup
%_bindir/geoip-update
%_libexecdir/%_name
%_sysconfdir/dbus-1/system.d/org.freedesktop.GeoClue2.conf
%_sysconfdir/dbus-1/system.d/org.freedesktop.GeoClue2.Agent.conf
%_datadir/dbus-1/system-services/org.freedesktop.GeoClue2.service
%_datadir/%_name-%api_ver/%_name-interface.xml
%_datadir/%_name-%api_ver/geoclue-agent-interface.xml
%systemd_unitdir/%_name.service
%config %_sysconfdir/%_name/%_name.conf
%attr(1770, %_name, %_name) %dir %_localstatedir/%_name
%doc README NEWS

%files devel
%_libdir/pkgconfig/%_name-%api_ver.pc

%files devel-doc
%_datadir/gtk-doc/html/%_name/

%files demo
%_libexecdir/%_name-%api_ver/demos/
%_datadir/applications/*.desktop


%changelog
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

