%define ver_major 3.20
%define api_ver 1.0
%define _libexecdir %_prefix/libexec
%def_enable facebook
%def_enable flickr
%def_enable google
%def_enable media_server
%def_enable owncloud
%def_enable windows_live

Name: gnome-online-miners
Version: %ver_major.1
Release: alt1

Summary: A set of miners for online content
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://git.gnome.org/browse/gnome-online-miners

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.35.1
%define goa_ver 3.11.5
%define grilo_ver 0.3
%define gdata_ver 0.13.3
%define zapojit_ver 0.0.2
%define tracker_ver 0.17.1
%define gfbgraph_ver 0.2.2

%{?_enable_flickr:Requires: grilo-plugins >= %grilo_ver}

BuildRequires: gnome-common
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgnome-online-accounts-devel >= %goa_ver
BuildPreReq: tracker-devel >= %tracker_ver
%{?_enable_google:BuildPreReq: libgdata-devel >= %gdata_ver}
%{?_enable_flickr:BuildPreReq: libgrilo-devel >= %grilo_ver}
%{?_enable_facebook:BuildPreReq: libgfbgraph-devel >= %gfbgraph_ver}
%{?_enable_windows_live:BuildPreReq: libzapojit-devel >= %zapojit_ver}

%description
GNOME Online Miners provides a set of crawlers that go through your
online content and index them locally in Tracker. It has miners for
Flickr, Google, SkyDrive and ownCloud.

%prep
%setup

%build
%autoreconf
%configure --disable-static \
	%{subst_enable facebook} \
	%{subst_enable flickr} \
	%{subst_enable google} \
	%{?_enable_media_server:--enable-media-server} \
	%{subst_enable owncloud} \
	%{?_enable_windows_live:--enable-windows-live}
%make_build

%install
%makeinstall_std

%files
%_libexecdir/gom-facebook-miner
%_libexecdir/gom-flickr-miner
%_libexecdir/gom-gdata-miner
%_libexecdir/gom-media-server-miner
%_libexecdir/gom-owncloud-miner
%_libexecdir/gom-zpj-miner
%dir %_libdir/%name
%_libdir/%name/libgom-%api_ver.so
%_datadir/dbus-1/services/org.gnome.OnlineMiners.Facebook.service
%_datadir/dbus-1/services/org.gnome.OnlineMiners.Flickr.service
%_datadir/dbus-1/services/org.gnome.OnlineMiners.GData.service
%_datadir/dbus-1/services/org.gnome.OnlineMiners.MediaServer.service
%_datadir/dbus-1/services/org.gnome.OnlineMiners.Owncloud.service
%_datadir/dbus-1/services/org.gnome.OnlineMiners.Zpj.service
%doc AUTHORS NEWS README

%exclude %_libdir/%name/libgom-%api_ver.la
%exclude %_datadir/doc/%name

%changelog
* Fri Sep 02 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Sat Sep 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt4
- rebuilt for gnome-3.18

* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt3
- rebuilt against libgrilo-0.2.so.10

* Sun Aug 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt2
- rebuilt against libgdata.so.22

* Thu May 07 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Mon Dec 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Wed Sep 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Fri Aug 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt2
- rebuilt against libgdata.so.19

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Jan 20 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Fri Nov 22 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Aug 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.90-alt1
- first build for people/gnome

