%define _name org.gnome.sound-juicer
%define ver_major 3.18
%define gst_api_ver 1.0

Name: sound-juicer
Version: %ver_major.2
Release: alt1

Summary: Clean and lean CD ripper
Group: Sound
License: GPLv2+
Url: http://live.gnome.org/SoundJuicer

Requires: gst-plugins-base%gst_api_ver gst-plugins-good%gst_api_ver
Requires: iso-codes

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildPreReq: gcc-c++ gnome-common
BuildRequires: intltool yelp-tools desktop-file-utils libappstream-glib-devel
BuildRequires: libgio-devel >= 2.32
BuildRequires: libbrasero-devel >= 3.0.0
BuildRequires: libgtk+3-devel >= 2.90.0
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: libcanberra-devel libcanberra-gtk3-devel
BuildRequires: gstreamer%gst_api_ver-devel gst-plugins%gst_api_ver-devel
BuildRequires: gst-plugins-base%gst_api_ver gst-plugins-good%gst_api_ver gstreamer%gst_api_ver-utils
BuildRequires: libmusicbrainz5-devel  >= 5.1.0 libdiscid-devel iso-codes-devel

%description
GStreamer-based CD ripping tool. Saves audio CDs to audio formats,
supported by GStreamer.

%prep
%setup
subst 's/0\.10/1.0/' configure

%build
#export LIBS="$LIBS `pkg-config --libs libmusicbrainz5 libdiscid`"
%configure \
	--disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=DiscBurning \
	--add-category=GTK \
	%buildroot%_desktopdir/sound-juicer.desktop

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_datadir/applications/%name.desktop
%_datadir/icons/*/*/*/*
%_datadir/GConf/gsettings/%name.convert
%_datadir/glib-2.0/schemas/%_name.gschema.xml
%_man1dir/%name.1.*
%_datadir/appdata/%name.appdata.xml
%doc AUTHORS README NEWS

%changelog
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
