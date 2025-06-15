%define _unpackaged_files_terminate_build 1

Name:		viking
Version:	1.10
Release:	alt1

Summary:	GPS data editor, analyzer and viewer

Group:		Sciences/Geosciences
License:	GPL-2.0-or-later
URL:		https://sourceforge.net/projects/viking/
VCS:        https://github.com/viking-gps/viking

Source:	%{name}-%{version}.tar

BuildRequires: intltool
BuildRequires: gtk-doc
BuildRequires: xxd
BuildRequires: libexpat-devel
BuildRequires: libcurl-devel
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libgeoclue-2.0)
BuildRequires: pkgconfig(gexiv2)
BuildRequires: yelp-tools
BuildRequires: libgps-devel
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(libmagic)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libzip)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(nettle)
BuildRequires: libnova-devel

Requires: gpsbabel

%description
Viking aims to be easy to use, yet powerful in accomplishing a wide
variety of GPS related tasks. It uses a hierarchical layering system
to organize GPS data, maps, and other layer types with spatial data,
such as coordinate lines.

Some of the things you can use Viking for are:

* Uploading and downloading waypoints, tracks to/from GPS.
* Realtime GPS tracking and track recording.
* Import and export of gpx files.
* Preparing tracks and waypoints for trips using maps from services
such as OpenStreetmap and Terraserver. You only need to upload the data
to your GPS before you leave. The maps together with your tracks
and waypoints can also be printed and used during the trip.
* After trips, tracks and waypoints from GPS can be downloaded,
stored, managed and reused in later trips.
* Analyzing OHV and hiking trips, understanding where you went and
how far you were from something.
* Making waypoints and tracks to follow to easily get someplace
you've never been before or don't have GPS data for but Terraserver
maps exist for it.
* Making maps with coordinate lines.
* Analyzing speed at different places, adding waypoints where you forgot
to mark one but did slow down or stop.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
           --disable-mapnik \
           --disable-zip
%make

%install
%makeinstall

%find_lang %name

%check
make check

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO doc/
%_bindir/%name
%_datadir/applications/%{name}.desktop
%_datadir/icons/hicolor/48x48/apps/%{name}.png
%exclude %_datadir/icons/hicolor/icon-theme.cache
%_man1dir/%{name}.1*
%_datadir/%name
%dir %_datadir/help/C/%name/
%_datadir/help/C/%name/*

%changelog
* Sun Jun 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.10-alt1
- Actual gtk3-based version

* Sat Jan 18 2020 Sergey Y. Afonin <asy@altlinux.org> 1.7.0-alt3
- gps api 9 support (gpsd 3.20, patch from Debian)
- built with libzip-devel
- enabled geocaches

* Tue Dec 24 2019 Sergey Y. Afonin <asy@altlinux.org> 1.7.0-alt2
- packed localization (ALT #37674)
- updated License to SPDX syntax, changed to GPL-2.0-or-later
- added %%check section

* Thu Oct 17 2019 Anton Midyukov <antohami@altlinux.org> 1.7.0-alt1
- 1.7.0

* Mon Jun 01 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Thu Jul 21 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.1-alt2
- build fixed

* Tue Jun 21 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.1-alt1
- new version

* Wed Mar 23 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1-alt1
- new version
- build fixed

* Wed Jun 09 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.93-alt1
- new version

* Mon Jun 01 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.8-alt1
- new version
- unworking Google maps removed

* Thu Oct 02 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.6-alt1
- new version

* Fri Apr 11 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.4-alt1
- first build for Sisyphus

* Thu Feb 21 2008 Michael A. Peters <mpeters@mac.com> - 0.9.3.20080220-1
- change License field from GPL to GPLv2
- BR gpsd-devel
- BR gettext perl(XML::Parser) - needed for intltool
- use find_land macro to package mo files

* Sun Sep  4 2007 Guilhem Bonnefille <guilhem.bonnefille> - 0.9.2-1
- Update to upstream version 0.9.2.

* Sun Sep  2 2007 Guilhem Bonnefille <guilhem.bonnefille> - 0.9.1-1
- Update to upstream version 0.9.1.

* Fri Jul 13 2007 Guilhem Bonnefille <guilhem.bonnefille> - 0.9-1
- Update to upstream version 0.9.

* Thu May 18 2007 Quy Tonthat <qtonthat@gmail.com>
- Added curl-devel to BuildRequires list.

* Thu May 15 2007 Guilhem Bonnefille <guilhem.bonnefille> - 0.1.3-1
- Update to upstream version 0.1.3.

* Wed Feb 14 2007 Michael A. Peters <mpeters@mac.com> - 0.1.2-1
- Initial Fedora style spec file.
