%define _name geoclue
%define api_ver 2.0
%define _libexecdir %_prefix/libexec

%def_enable server

Name: %{_name}2
Version: 1.99.4
Release: alt1

Summary: The Geoinformation Service
Group: System/Libraries
License: LGPLv2
Url: http://geoclue.freedesktop.org/

Source: http://people.freedesktop.org/~hadess/%_name-%version.tar.xz

BuildRequires: intltool yelp-tools libgio-devel >= 2.32.4 
BuildRequires: libjson-glib-devel libsoup-devel
%{?_enable_server:BuildRequires: libGeoIP-devel}
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

%prep
%setup -q -n %_name-%version

subst 's/\(libsoup\) /\1-2.4 /' src/%_name-%api_ver.pc.in

%build
%autoreconf
%configure --disable-static \
	%{?_enable_server:--enable-geoip-server=yes}
%make_build

%install
%makeinstall_std

%check
#%%make check

%files
%_bindir/geoip-lookup
%_bindir/geoip-update
%_libexecdir/%_name
%_sysconfdir/dbus-1/system.d/org.freedesktop.GeoClue2.conf
%_datadir/dbus-1/system-services/org.freedesktop.GeoClue2.service
%_datadir/%_name-%api_ver/%_name-interface.xml
%doc README NEWS

%files devel
%_libdir/pkgconfig/%_name-%api_ver.pc

%changelog
* Tue Sep 17 2013 Yuri N. Sedunov <aris@altlinux.org> 1.99.4-alt1
- 1.99.4

* Sun Sep 01 2013 Yuri N. Sedunov <aris@altlinux.org> 1.99.2-alt1
- first build for Sisyphus

