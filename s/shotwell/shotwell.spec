Name: shotwell
Version: 0.12.3
Release: alt1
Summary: digital photo organizer designed for the GNOME desktop environment

Group: Graphics
License: LGPL
Url: http://www.yorba.org/shotwell/

# Cloned from git://yorba.org/shotwell
Source: %name-%version.tar

BuildRequires: gstreamer-devel gst-plugins-devel libGConf-devel libdconf-devel libdbus-glib-devel libgee-devel libgexiv2-devel libgphoto2-devel libgudev-devel libjson-glib-devel libraw-devel libsqlite3-devel libstdc++-devel libunique3-devel libwebkitgtk3-devel vala librest-devel

Requires: dconf

%description
Shotwell is a digital photo organizer designed for the GNOME desktop
environment.  It allows you to import photos from disk or camera,
organize them in various ways, view them in full-window or fullscreen
mode, and export them to share with others.

%prep
%setup -q

%build
./configure --disable-icon-update --prefix=%_prefix --lib=%_lib
%make_build

%install
%makeinstall_std
%find_lang --output=%name.lang %name %name-extras

%files -f %name.lang
%_bindir/%name
%_bindir/%name-video-thumbnailer
%_libdir/%name
%_desktopdir/%{name}*
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name
%_datadir/gnome/help/shotwell
%_datadir/GConf/gsettings/*
%_datadir/glib-2.0/schemas/*
%doc AUTHORS COPYING NEWS README THANKS

%changelog
* Wed Jun 13 2012 Vladimir Lettiev <crux@altlinux.ru> 0.12.3-alt1
- 0.12.3
- build with new shared libraw

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.12.2-alt1
- 0.12.2

* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Wed Jan 25 2012 Vladimir Lettiev <crux@altlinux.ru> 0.11.99-alt2
- git snapshot d867f19

* Thu Nov 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11.99-alt1
- git snapshot c1f9e00

* Wed Oct 19 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11.5-alt1
- 0.11.5

* Fri Oct 14 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11.4-alt1
- 0.11.4

* Wed Oct 12 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11.3-alt1
- 0.11.3

* Fri Oct 07 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11.2-alt1
- 0.11.2
- Source cloned from upstream git
- No longer need to install or compile GConf schemas (b3d5985d)

* Wed Sep 07 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.11.0-alt2
- Dependance on dconf added.

* Wed Aug 24 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.11.0-alt1
- New version 0.11.0
- shotwell-plugins-mk.patch deleted

* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.10.1-alt1
- New version 0.10.1
- Fixed plugins linking
- Dropped shotwell-0.9.1-vala.patch

* Thu May 05 2011 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt3
- fixed build with vala-0.10.4 (4c74b5c)

* Fri Feb 18 2011 Vladimir Lettiev <crux@altlinux.ru> 0.8.1-alt2
- Rebuilt with libraw 0.13.1

* Wed Jan 12 2011 Vladimir Lettiev <crux@altlinux.ru> 0.8.1-alt1
- New version 0.8.1

* Fri Dec 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.8.0-alt1
- New version 0.8.0
- Updated buildrequires

* Fri Dec 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.7.2-alt2
- Rebuilt with libraw 0.11.3

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.7.2-alt1
- New version 0.7.2

* Tue Jul 27 2010 Vladimir Lettiev <crux@altlinux.ru> 0.6.1-alt1
- New version 0.6.1

* Thu Jun 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.5.2-alt1
- New version 0.5.2

* Wed Mar 17 2010 Vladimir Lettiev <crux@altlinux.ru> 0.5.0-alt1
- new version 0.5.0

* Tue Mar 16 2010 Vladimir Lettiev <crux@altlinux.ru> 0.4.3-alt1
- initial build

