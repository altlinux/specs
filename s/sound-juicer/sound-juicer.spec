%define ver_major 3.4

Name: sound-juicer
Version: %ver_major.0
Release: alt1
Summary: Clean and lean CD ripper
Group: Sound
License: GPLv2+
Url: http://live.gnome.org/SoundJuicer
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Requires: gst-plugins-base gst-plugins-good

Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildPreReq: gnome-common
BuildRequires: intltool desktop-file-utils gcc-c++
BuildRequires: gnome-doc-utils-xslt gnome-doc-utils
BuildRequires: glib2-devel >= 2.18
BuildRequires: libbrasero-devel >= 3.0.0
BuildRequires: libgtk+3-devel >= 2.90.0
BuildRequires: GConf libGConf-devel
BuildRequires: libgio-devel libdbus-glib-devel libdbus-devel
BuildRequires: libcanberra-devel libcanberra-gtk3-devel
BuildRequires: gstreamer-devel gst-plugins-devel gst-plugins-base gst-plugins-good gstreamer-utils
BuildRequires: libgnome-media-profiles-devel >= 3.0.0
BuildRequires: libmusicbrainz3-devel  >= 3.0.2 libdiscid-devel

%description
GStreamer-based CD ripping tool. Saves audio CDs to audio formats,
supported by GStreamer.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-schemas-install \
	--disable-scrollkeeper

%make_build

%install
%make_install install DESTDIR=%buildroot

%find_lang --with-gnome %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=DiscBurning \
	--add-category=GTK \
	%buildroot%_desktopdir/sound-juicer.desktop

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
    %gconf2_uninstall %name
fi

%files -f %name.lang
%_bindir/*
%_datadir/%name
%_datadir/applications/*
%_datadir/icons/*/*/*/*
%_man1dir/*
%config %_sysconfdir/gconf/schemas/*
%doc AUTHORS README NEWS

%changelog
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
