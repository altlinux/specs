%define ver_major 3.10
%define api_ver 1.0
%define _libexecdir %_prefix/libexec

Name: gnome-online-miners
Version: %ver_major.0
Release: alt1

Summary: A set of miners for online content
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://git.gnome.org/browse/gnome-online-miners

Source: ftp://ftp.gnome.org/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.35.1
%define goa_ver 3.8.0
%define grilo_ver 0.2.6
%define gdata_ver 0.13.3
%define zapojit_ver 0.0.2
%define tracker_ver 0.16.0

Requires: grilo-plugins

BuildRequires: gnome-common
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgnome-online-accounts-devel >= %goa_ver
BuildPreReq: libgrilo-devel >= %grilo_ver
BuildPreReq: libgdata-devel >= %gdata_ver
BuildPreReq: libzapojit-devel >= %zapojit_ver
BuildPreReq: tracker-devel >= %tracker_ver

%description
GNOME Online Miners provides a set of crawlers that go through your
online content and index them locally in Tracker. It has miners for
Flickr, Google, SkyDrive and ownCloud.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libexecdir/gom-flickr-miner
%_libexecdir/gom-gdata-miner
%_libexecdir/gom-owncloud-miner
%_libexecdir/gom-zpj-miner
%dir %_libdir/%name
%_libdir/%name/libgom-%api_ver.so
%_datadir/dbus-1/services/org.gnome.OnlineMiners.Flickr.service
%_datadir/dbus-1/services/org.gnome.OnlineMiners.GData.service
%_datadir/dbus-1/services/org.gnome.OnlineMiners.Owncloud.service
%_datadir/dbus-1/services/org.gnome.OnlineMiners.Zpj.service
%doc AUTHORS NEWS README

%exclude %_libdir/%name/libgom-%api_ver.la
%exclude %_datadir/doc/%name

%changelog
* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Aug 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.90-alt1
- first build for people/gnome

