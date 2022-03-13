%def_enable snapshot
%define _unpackaged_files_terminate_build 1

%define ver_major 3.38
%define gst_api_ver 1.0
%define xdg_name org.gnome.SoundJuicer

Name: sound-juicer
Version: %ver_major.0
Release: alt3

Summary: Clean and lean CD ripper
Group: Sound
License: GPL-2.0-or-later
Url: https://wiki.gnome.org/Apps/SoundJuicer

Requires: gst-plugins-base%gst_api_ver gst-plugins-good%gst_api_ver
Requires: iso-codes

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
Patch: %name-3.38.0-alt-help_build.patch

%define glib_ver 2.50
%define gtk_ver 3.22
%define musicbrainz_ver 5.1.0
%define diskid_ver 0.4.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++
BuildRequires: yelp-tools desktop-file-utils libappstream-glib-devel
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libbrasero-devel >= 3.0.0
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: libcanberra-devel libcanberra-gtk3-devel
BuildRequires: gst-plugins%gst_api_ver-devel %_bindir/gst-inspect-%gst_api_ver
BuildRequires: gst-plugins-base%gst_api_ver gst-plugins-good%gst_api_ver
BuildRequires: libmusicbrainz5-devel >= %musicbrainz_ver libdiscid-devel >= %diskid_ver iso-codes-devel

%description
GStreamer-based CD ripping tool. Saves audio CDs to audio formats,
supported by GStreamer.

%prep
%setup
%patch -p1 -b .help

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=DiscBurning \
	--add-category=GTK \
	%buildroot%_desktopdir/%xdg_name.desktop

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_datadir/applications/%xdg_name.desktop
%_datadir/icons/*/*/*/*
%_datadir/GConf/gsettings/%name.convert
%_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_datadir/dbus-1/services/%xdg_name.service
%_man1dir/%name.1.*
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc AUTHORS README* NEWS

%exclude %_datadir/doc/%name/

%changelog
* Sun Mar 13 2022 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt3
- updated to 3.38.0-27-g9f97ca1f (fixed build with meson-0.61)

* Wed Sep 08 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt2
- updated to 3.38.0-23-gf449f627
- fixed help build (ALT #40874)

* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0 (ported to Mesin build system)

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Nov 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Dec 01 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt2
- rebuilt against libmusicbrainz5.so.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Fri May 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.90-alt2
- fixed buildreqs

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.90-alt1
- 3.11.90

* Fri Dec 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.5.0-alt1
- 3.5.0

* Wed Mar 28 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.32.1-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for sound-juicer

* Fri May 27 2011 Alexey Shabalin <shaba@altlinux.ru> 2.32.1-alt1
- upstream snapshot

* Mon Oct 11 2010 Alexey Shabalin <shaba@altlinux.ru> 2.32.0-alt1
- 2.32.0

* Mon May 17 2010 Alexey Shabalin <shaba@altlinux.ru> 2.28.2-alt1
- 2.28.2

* Thu Nov 26 2009 Alexey Shabalin <shaba@altlinux.ru> 2.28.1-alt1
- 2.28.1

* Mon Nov 16 2009 Alexey Shabalin <shaba@altlinux.ru> 2.28.0-alt2
- update buildreq
- only one libmusicbrainz in BuildRequires
- add --disable-static
- add patches from fedora
- rebuild with new libcdio

* Sun Nov 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.28.0-alt1
- 2.28.0

* Fri Aug 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.26.1-alt1
- rebuild with new libcdio

* Mon Apr 13 2009 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.26.1-alt0.1
- 2.26.1

* Wed Mar 18 2009 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.26.0-alt1
- 2.26.0

* Tue Oct 14 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.24.0-alt2
- Replace gst-plugins-gnomevfs dependency with gst-plugins-gio

* Thu Oct 02 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.24.0-alt1
- 2.24.0

* Sat May 17 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.0-alt3
- Rebuild with new gstreamer build

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.22.0-alt2.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for sound-juicer

* Thu Mar 13 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.0-alt2
- correct build on x86_64

* Tue Mar 11 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.0-alt1
- 2.22.0

* Fri Oct 19 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.1-alt1
- 2.20.1

* Thu Sep 20 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.0-alt1
- 2.20.0

* Sun Jun 24 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.4-alt2
- Correct buildreq

* Tue May 08 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.4-alt1
- 2.16.4

* Wed Feb 21 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.3-alt1
- Add man page

* Wed Feb 21 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.3-alt0.1
- 2.16.3

* Mon Nov 27 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.2-alt0.1
- 2.16.2

* Wed Oct 11 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.1-alt0.1
- 2.16.1 (NMU)

* Tue Jun 06 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.4-alt0.1
- 2.14.4 (NMU)

* Tue Nov 29 2005 Vital Khilko <vk@altlinux.ru> 2.12.3-alt1
- 2.12.3

* Wed Oct 12 2005 Vital Khilko <vk@altlinux.ru> 2.12.2-alt1
- 2.12.2

* Fri Sep 09 2005 Vital Khilko <vk@altlinux.ru> 2.12.0-alt1
- new version released
- removed translated package descriptions

* Thu Aug 04 2005 Vital Khilko <vk@altlinux.ru> 2.11.90-alt1
- 2.11.90

* Sat Apr 02 2005 Vital Khilko <vk@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Sun Feb 06 2005 Vital Khilko <vk@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Thu Jan 13 2005 Vital Khilko <vk@altlinux.ru> 0.5.14-alt2
- rebuild with hal

* Fri Nov 05 2004 Vital Khilko <vk@altlinux.ru> 0.5.14-alt1
- new version released
- updated belarusian translation

* Fri Sep 03 2004 Vital Khilko <vk@altlinux.ru> 0.5.12-alt1
- new version released (thanks aris@ )

* Thu Apr 08 2004 Vital Khilko <vk@altlinux.ru> 0.5.10.1-alt1
- initial build for ALT Linux Sisyphus
