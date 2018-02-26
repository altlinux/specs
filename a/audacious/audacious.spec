#%define rel -beta4
%define rel %nil
Name: audacious
Version: 2.5.0
Release: alt1.qa2

Summary: Media player which uses a skinned interface

License: GPL
Group: Sound
Url: http://audacious-media-player.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://distfiles.atheme.org/%name-%version%rel.tar

Patch: audacious-0.1.2-default-alsa.patch
Patch1: %name-as-needed.patch
#Patch2: %name-%version-lib.patch
Patch3: %name-2.5.0-alt-DSO.patch

# Typical environment for GNOME program
Requires(post,postun): desktop-file-utils
BuildPreReq: desktop-file-utils

%{?_with_gconf:BuildRequires: GConf2-devel}
%{?_with_vfs:BuildRequires: gnome-vfs2-devel}

# due
# verify-elf: ERROR: ./usr/lib/libaudid3tag.so.1.0.0: undefined symbol: _audvt
#set_verify_elf_method unresolved=relaxed

# manually removed: audacious
# Automatically added by buildreq on Mon Apr 18 2011
# optimized out: fontconfig fontconfig-devel glib2-devel libICE-devel libX11-devel libatk-devel libcairo-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libmowgli-devel libpango-devel pkg-config termutils xorg-xproto-devel
BuildRequires: gcc-c++ libSM-devel libdbus-glib-devel libgtk+2-devel libmcs-devel

BuildRequires: libgtk+2-devel >= 2.6

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
%setup -q -n %name-%version%rel
#%patch -p1 -b .default-alsa
#%patch2
%patch3 -p2
#bzip ChangeLog

%build
#__autoreconf -I m4
#__autoconf -I m4
%configure \
    --disable-rpath \
    %{?_with_gconf:--enable-gconf} \
    %{?_with_vfs:--enable-gnome-vfs} \
    --disable-dependency-tracking \
%ifnarch x86_64
    --disable-sse2 \
%endif
    --enable-chardet

# compile with midi support without see in /proc
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README
%_bindir/%name
%_bindir/audtool
%_desktopdir/*.desktop
%_datadir/%name/
%_iconsdir/hicolor/48x48/apps/audacious.png
%_iconsdir/hicolor/scalable/apps/audacious.svg
%_pixmapsdir/%name.png
%_pixmapsdir/%name.svg
%_man1dir/*

%files -n lib%name
%_libdir/libaudclient.so.*
#%_libdir/libaudid3tag.so.*
%_libdir/libaudtag.so.*
#%_libdir/libSAD.so.*
%_libdir/libaudcore.so.*
%_libdir/libaudgui.so.*

%files -n lib%name-devel
%_includedir/%name/
#%_includedir/libSAD/
%_includedir/libaudcore/
%_includedir/libaudgui/
#%_includedir/libaudtag/
%_pkgconfigdir/*.pc
%_libdir/*.so

%changelog
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

