#%define rel -beta4
%define rel %nil
Name: audacious
Version: 4.3
Release: alt1

Summary: Media player which uses a skinned interface

License: GPL
Group: Sound
Url: http://audacious-media-player.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://distfiles.audacious-media-player.org/%name-%version%rel.tar

Patch: audacious-0.1.2-default-alsa.patch
Patch1: %name-as-needed.patch
#Patch2: %name-%version-lib.patch
Patch3: %name-2.5.0-alt-DSO.patch

# Typical environment for GNOME program
Requires(post,postun): desktop-file-utils
BuildPreReq: desktop-file-utils

BuildRequires: gcc-c++

BuildRequires: glib2-devel libgio-devel

BuildRequires: qt5-base-devel

BuildRequires: libgtk+2-devel

BuildRequires: libguess-devel >= 1.2

BuildRequires: libarchive-devel

Requires: %name-plugins

%description
Audacious is a media player forked from BMP (Beep Media Player) which uses a
skinned interface based on Winamp 2.x skins, and in turn based on XMMS.

%package -n lib%name
Summary: Library files for the audacious media player
Group: Development/Other

%description -n lib%name
Audacious is a media player forked from BMP (Beep Media Player) which uses a
skinned interface based on Winamp 2.x skins, and in turn based on XMMS.

Library file required to run audacious.


%package -n lib%name-devel
Summary: Development files for the audacious media player
Group: Development/Other
Requires: lib%name = %version
Provides: %name-devel
Obsoletes: %name-devel

%description -n lib%name-devel
Audacious is a media player forked from BMP (Beep Media Player) which uses a
skinned interface based on Winamp 2.x skins, and in turn based on XMMS.

Development files required to develop plugins for audacious.


%prep
%setup -n %name-%version%rel

%build
%configure \
    --with-buildstamp="ALT Linux package"  \
    --disable-rpath \
    --enable-libarchive \
    --disable-dependency-tracking \
%ifnarch x86_64
    --disable-sse2 \
%endif
    --enable-chardet

%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS
%_bindir/%name
%_bindir/audtool
%_desktopdir/*.desktop
%_datadir/%name/
%_iconsdir/hicolor/48x48/apps/audacious.png
%_iconsdir/hicolor/scalable/apps/audacious.svg
%_man1dir/*

%files -n lib%name
#_libdir/libaudclient.so.*
#%_libdir/libaudid3tag.so.*
%_libdir/libaudtag.so.*
#%_libdir/libSAD.so.*
%_libdir/libaudcore.so.*
%_libdir/libaudqt.so.*
%_libdir/libaudgui.so.*

%files -n lib%name-devel
%_includedir/%name/
#%_includedir/libSAD/
%_includedir/libaudcore/
%_includedir/libaudqt/
%_includedir/libaudgui/
%_pkgconfigdir/*.pc
%_libdir/*.so

%changelog
* Wed Mar 08 2023 Vitaly Lipatov <lav@altlinux.ru> 4.3-alt1
- new version 4.3 (with rpmrb script)

* Mon Dec 19 2022 Vitaly Lipatov <lav@altlinux.ru> 4.2-alt1
- new version 4.2 (with rpmrb script)

* Thu Feb 25 2021 Vitaly Lipatov <lav@altlinux.ru> 4.1-alt1
- new version 4.1 (with rpmrb script)
- enable build with libarchive

* Sat Aug 01 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0.5-alt1
- new version 4.0.5 (with rpmrb script)

* Sat Jun 06 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0.4-alt1
- new version 4.0.4 (with rpmrb script)

* Tue May 05 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0.3-alt1
- new version 4.0.3 (with rpmrb script)

* Sun Mar 29 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0-alt1
- new version 4.0 (with rpmrb script)
- upstream switched to Qt5

* Wed Dec 26 2018 Vitaly Lipatov <lav@altlinux.ru> 3.10.1-alt1
- new version 3.10.1 (with rpmrb script)

* Thu Aug 30 2018 Vitaly Lipatov <lav@altlinux.ru> 3.10-alt1
- new version 3.10 (with rpmrb script)

* Sun Aug 27 2017 Vitaly Lipatov <lav@altlinux.ru> 3.9-alt1
- new version 3.9 (with rpmrb script) (ALT bug 33816)

* Thu Jan 26 2017 Vitaly Lipatov <lav@altlinux.ru> 3.8.2-alt1
- new version 3.8.2 (with rpmrb script)

* Sat Dec 31 2016 Vitaly Lipatov <lav@altlinux.ru> 3.8.1-alt1
- new version 3.8.1 (with rpmrb script)

* Sun Oct 02 2016 Vitaly Lipatov <lav@altlinux.ru> 3.8-alt1
- new version 3.8 (with rpmrb script)

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 3.7.2-alt1
- new version 3.7.2 (with rpmrb script)

* Sat Jan 02 2016 Vitaly Lipatov <lav@altlinux.ru> 3.7.1-alt1
- new version 3.7.1 (with rpmrb script)

* Sun Jul 12 2015 Vitaly Lipatov <lav@altlinux.ru> 3.6.2-alt1
- new version 3.6.2 (with rpmrb script)

* Wed May 06 2015 Vitaly Lipatov <lav@altlinux.ru> 3.6.1-alt1
- new version 3.6.1 (with rpmrb script)

* Mon Dec 08 2014 Vitaly Lipatov <lav@altlinux.ru> 3.5.2-alt1
- new version 3.5.2 (with rpmrb script)

* Tue Sep 02 2014 Vitaly Lipatov <lav@altlinux.ru> 3.5.1-alt1
- new version 3.5.1 (with rpmrb script)

* Tue May 06 2014 Vitaly Lipatov <lav@altlinux.ru> 3.5-alt1
- new version 3.5 (with rpmrb script)

* Mon Feb 17 2014 Vitaly Lipatov <lav@altlinux.ru> 3.4.3-alt1
- new version 3.4.3 (with rpmrb script)

* Sat Oct 12 2013 Vitaly Lipatov <lav@altlinux.ru> 3.4.1-alt1
- new version 3.4.1 (with rpmrb script)

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 3.4-alt1
- new version 3.4 (with rpmrb script)

* Sun Jun 02 2013 Andrey Cherepanov <cas@altlinux.org> 3.3.4-alt1
- new version 3.3.4

* Sun Dec 09 2012 Vitaly Lipatov <lav@altlinux.ru> 3.3.2-alt1
- new version 3.3.2 (with rpmrb script)

* Sun Aug 05 2012 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt1
- new version 3.3 (with rpmrb script)
- update buildreqs

* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.qa2
- Fixed build

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.5.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-obsolete-buildreq for audacious

* Mon Apr 18 2011 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- new version (2.5.0) import in git (ALT bug #25456)

* Sat Nov 27 2010 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sat Dec 05 2009 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- new version (2.2)
- update buildreqs

* Fri Jul 10 2009 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt1
- new version 2.1 (with rpmrb script)

* Sun May 17 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version 2.0.1 (with rpmrb script)

* Fri Mar 06 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt4
- enable sse2 on x86_64

* Sun Mar 01 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt3
- build with --disable-sse2

* Sun Jul 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt2
- rebuild with new libmowgli

* Sat May 31 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version 1.5.1 (with rpmrb script)

* Wed Apr 23 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Sun Feb 24 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.6-alt1
- new version 1.4.6 (with rpmrb script)

* Mon Dec 31 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.5-alt1
- new version 1.4.5 (with rpmrb script)

* Wed Dec 05 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.4-alt1
- new version 1.4.4 (with rpmrb script)

* Wed Nov 28 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- new version 1.4.2 (with rpmrb script)

* Wed Nov 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- release 1.4.0

* Wed Oct 31 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt0.1beta4
- new version (1.4.0 beta4)
- drop patches (mainstreamed)

* Sat Oct 27 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt0.1beta2
- new version (1.4.0 beta2)
- enable update/clean menus
- update buildreqs
- fix libaudid3

* Wed Apr 18 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt2
- add libaudid3tag.so  provides (fix bug #11561)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt1
- new version 1.3.2 (with rpmrb script)

* Tue Apr 03 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version 1.3.1 (with rpmrb script)

* Wed Mar 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0
- update buildreq

* Sat Jan 06 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- build without GConf2, ImageMagick build requires
- use installed icon, do not convert it
- cleanup spec, use --disable-dependency-tracking for speedup
- build with --enable-chardet (librcd using)

* Mon Dec 11 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt0.1
- new version 1.2.2 (with rpmrb script)

* Fri Nov 17 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- split to libaudacious, rename devel to libaudacious-devel
- add require for audacious-plugins

* Thu Nov 16 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt0.1
- new version 1.2.1 (need install audacious-plugins)

* Sun Oct 15 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt0.1
- new version (1.2.0)

* Sun Oct 15 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt0.1rc3
- new version (1.2.0)

* Wed Sep 20 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt0.1
- new version 1.1.2
- add amidi-plug backends packing

* Thu Aug 03 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt0.1
- new version 1.1.1 (with rpmrb script)

* Tue May 02 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt0.1
- new version (1.0.0)

* Sun Mar 26 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt0.1
- new version 0.2.3
- fixes for build with ld --as-needed

* Mon Feb 06 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt0.1
- new version
- cleanup spec, remove COPYING

* Wed Jan 04 2006 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt0.1
- initial build for ALT Linux Sisyphus

* Tue Dec 20 2005 Matthias Saou <http://freshrpms.net/> 0.1.2-1
- Initial RPM release.
- Can't seem to get libsamplerate nor sndfile enabled.
- Disable GConf and VFS by default, since nothing seems to work otherwise.

