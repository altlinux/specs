Name: xosd
Version: 2.2.14
Release: alt6

Summary: X On Screen Display, displays XMMS status information
License: GPL
Group: Sound
Url: http://sourceforge.net/projects/libxosd/
Packager: Evgenii Terechkov <evg@altlinux.ru>

Source: %name-%version.tar
Patch2: %name-2.2.14-alt-aclocal-quoting.patch

# Automatically added by buildreq on Thu Nov 08 2007 (-bi)
BuildRequires: gcc-c++ gdk-pixbuf-devel imake libXinerama-devel libXt-devel libxmms-devel xorg-cf-files libXext-devel

%description
This is a X On Screen Display library, modules and utilities.

%package -n lib%name
Group: System/Libraries
Summary: Library for displaying information in an OSD

%package -n lib%name-devel
Group: Development/C
Summary: Header files for developing programs using libxosd
Requires: lib%name = %version-%release

%package -n lib%name-devel-static
Group: Development/C
Summary: Development libraries for static linking using libxosd
Requires: lib%name-devel = %version-%release

%package -n xmms-osd
Group: Sound
Summary: X On Screen Display utilities
Requires: lib%name = %version-%release
Requires: xmms
Provides: xmms-xosd = %version-%release
Obsoletes: xmms-xosd

%package -n %name-utils
Group: Graphics
Summary: X On Screen Display, displays any information using libxosd
Requires: lib%name = %version-%release
Obsoletes: %name-utils

%description -n lib%name
This package contains the shared library of xosd, it is requires by programs
that display it's output in a TV set's on screen display fashion.

%description -n lib%name-devel
This package contains the header files you need to develop programs based on
libxosd that display it's output in a TV set's on screen display fashion.

%description -n lib%name-devel-static
This package contains the development libraries for static linking
necessary to develop %name application.

This package contains the header files you need to develop programs based on
libxosd that display it's output in a TV set's on screen display fashion.

%description -n xmms-osd
This package contains an xmms plugin to display various things whenever they
change (volume, track, paused/shuffle/repeat,...) in a TV set's on screen
display fashion.

%description -n %name-utils
This package contains an osd_cat.

%prep
%setup
%patch2 -p1

%build
%configure --enable-new-plugin --disable-beep_media_player_plugin
%make_build

%install
make install DESTDIR=%buildroot

%files -n lib%name
%_libdir/*.so.*
%doc ChangeLog README AUTHORS TODO

%files -n lib%name-devel
%_bindir/%name-config
#%_libdir/*.la
%_includedir/%name.h
%_datadir/aclocal/lib%name.m4
%_man1dir/%{name}*
%_man3dir/%{name}*
%_libdir/lib%name.so

%files -n lib%name-devel-static
%_libdir/*.a

%files -n xmms-osd
%xmms_generaldir/*
%dir %_datadir/%name
%_datadir/%name/*.png

%files -n %name-utils
%_bindir/osd_cat
%_man1dir/osd_cat.1*

%changelog
* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 2.2.14-alt6
- Rebuilt for debuginfo
- Packaged %_datadir/%name directory

* Wed Dec  1 2010 Terechkov Evgenii <evg@altlinux.org> 2.2.14-alt5
- Rebuilt for soname set-versions

* Sun Dec  7 2008 Terechkov Evgenii <evg@altlinux.ru> 2.2.14-alt4
- Buildrequires updated
- Update spec to new filetriggers system

* Sun Oct  7 2007 Terechkov Evgenii <evg@altlinux.ru> 2.2.14-alt3
- Xmms plugin resurrected

* Sun Aug  5 2007 Terechkov Evgenii <evg@altlinux.ru> 2.2.14-alt2
- Quoting in libxosd.m4 fixed (#12471) - Patch2
- Patch1 removed (wont applied long ago, anyway)
- Minor spec cleanup

* Tue May 15 2007 Terechkov Evgenii <evg@altlinux.ru> 2.2.14-alt1
- 2.2.14
- Minor spec cleanup
- Xmms plugin removed

* Tue Oct 05 2004 Nazar Yurpeak  <phoenix@altlinux.org> 2.2.12-alt2
- Updated BuildRequires

* Mon Sep 27 2004 Nazar Yurpeak  <phoenix@altlinux.org> 2.2.12-alt1
- New version

* Mon Sep 06 2004 Nazar Yurpeak  <phoenix@altlinux.org> 2.2.10-alt1
- New version

* Tue Jul 06 2004 Nazar Yurpeak  <phoenix@altlinux.org> 2.2.8-alt1
- New version

* Thu May 27 2004 Nazar Yurpeak  <phoenix@altlinux.org> 2.2.7-alt1
- New version

* Wed Jan 21 2004 Nazar Yurpeak  <phoenix@altlinux.org> 2.2.5-alt2
- removed *.la
- rebuild

* Tue Oct 07 2003 Nazar Yurpeak  <phoenix@altlinux.org> 2.2.5-alt1
- 2.2.5

* Thu Jul 03 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt3
- Rebuilt in new environment.
- Minor specfile cleanup.

* Mon Jun 30 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.2.2-alt2
- remove osd_cat to xosd-utils (thanks for Zerg <zerg@altlinux.ru>)

* Mon Jun 30 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Tue Jun 25 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.2.1-alt4
- remove xosd-xonfig to libxosd-devel (thanks for Zerg <zerg@altlinux.ru>)

* Sat May 31 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.2.1-alt3
- rebuild with new XFree86

* Fri May 23 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.2.1-alt2
- updated Requires

* Wed Apr 23 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Mon Apr 15 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.2.0-alt1
- 2.2.0
- fixed spec
* Mon Mar 24 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.1.3-alt3
- fexed spec

* Thu Mar 20 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.1.3-alt2
- fixed spec
- added libxosd-devel-static (thanks for Zerg <zerg@altlinux.ru>)

* Tue Mar 18 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Mon Mar 03 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.1.2-alt1
- new version

* Fri Jan 17 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.0.2-alt1
- new version

* Wed Nov 14 2002 Nazar Yurpeak <phoenix@altlinux.ru> 2.0.1-alt1
- new version
- spec cleanup

* Sun Nov 10 2002 Nazar Yurpeak <phoenix@altlinux.ru> 2.0.0-alt1
- new version
- fixed rpath

* Wed Feb 06 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.7.0-alt3
- Specfile cleanup.
- Recent fix cleanup.

* Wed Jan 30 2002 Igor Muratov <migor@altlinux.ru> 0.7.0-alt2
- fix by Sergey Pinaev <dfo@antex.ru>
	- don't crash when can't make XFontSet
	- display non-latin1 characters

* Wed Nov 28 2001 Igor Muratov <migor@altlinux.ru> 0.7.0-alt1
- First build for ALT.

* Wed Aug 29 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.7.0-3mdk
- fixes from Götz Waschk <waschk@linux-mandrake.com> :
	- split library package to fix rpmlint errors
	- added osd_cat to devel package
	- patched for new libtool

* Wed Apr 18 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.7.0-2mdk
- fixes from Götz Waschk <waschk@linux-mandrake.com>

* Mon Apr 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.7.0-1mdk
- updated and fixed by Götz Waschk <waschk@linux-mandrake.com> :
	- 0.7.0
	- added manpage
	- more macros

* Mon Mar 19 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.6.1-3mdk
- Add xosd.h.

* Thu Mar 01 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.6.1-2mdk
- fix buildrequires

* Tue Jan 16 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.6.1-1mdk
- updated by Götz Waschk <waschk@linux-mandrake.com> :
	- 0.6.1
	- recreated Makefile patch

* Mon Jan 15 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.5.0-1mdk
- used srpm from Götz Waschk <waschk@linux-mandrake.com> :
	- 0.5.0
	- removed patch
	- fixed installation
	- added call of ldconfig in post and postun

* Sat Jan 06 2001 David BAUDENS <baudens@mandrakesoft.com> 0.3.0-2mdk
- Adjust BuildRequires to new lib policy
- Spec clean up

* Thu Nov 23 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.0-1mdk
- used, once again, great srpm from  Götz Waschk <waschk@linux-mandrake.com> :
	- initial Mandrake package
	- fixed Makefile
