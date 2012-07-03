Name: gnome-libs
Version: 1.4.2
Release: alt11

Summary: Main GNOME libraries
License: LGPL
Group: System/Libraries
Url: http://www.gnome.org/
Packager: Yury Aliaev <mutabor@altlinux.ru>

Source: ftp://ftp.gnome.org/pub/GNOME/stable/sources/%name/%name-%version.tar.bz2
Source1: conv_deskfiles.pl

%def_disable static
%define preferdb --enable-prefer-db1

# Red Hat patches
Patch1: RH-%name-rhsnddefs.patch
# rawhide - Enable setting canvas into a "bghack" mode with gtk_object_set_data
Patch2: %name-1.2.13-bghack.patch
# allow reading UTF-8 encoded .desktop
Patch3: %name-1.4.2-utf8menu.patch

# Mandrake patches
# (fc) search icons first in /usr/share/icons/large, normal and small
Patch5:	%name-1.4.2-iconspath.patch
# (fc) 1.2.13-2mdk fix bug 3730 (nautilus should not draw desktop when called as help browser)
Patch7: %name-1.2.13-nautilus.patch
# (fc) 1.4.1.2-10mdk fix missing prototypes
Patch18: %name-1.4.1.3-prototypes.patch
# (fc) 1.4.1.4-2mdk fix font size in gtk-xmhtml
Patch19: %name-1.4.1.4-fonts.patch
# (fc) 1.4.1.4-3mdk fix parsing of escape sequence (beep when launching vim) (Debian)
#Patch20: %name-1.4.1.4-zvtescape.patch
# (fc) 1.4.1.4-3mdk fix numeric keypad switching (fix keypad in vim) (Debian)
Patch21: %name-1.4.1.4-keypad.patch
# (pablo) 1.4.1.4-4mdk patch to have gnome-terminal switch automatically
# to utf-8 mode if the locale is utf-8
Patch22: http://noa.tm/utf-8/patches/%name-zvt-utf8-autodetect.patch
# (fc) 1.4.1.7-2mdk don't add -L/usr/lib to ldflags
#Patch23: %name-1.4.1.7-libdir.patch
# (fc) 1.4.2-1mdk remove -I/usr/include from cflags
Patch24: %name-1.4.2-includedir.patch

# ALT patches
# fix cyrillic font specifications
Patch30: %name-1.4.2-alt-fonts.patch
# add belarussian translation and gtkrc
Patch31: %name-1.4.2-be.patch
# correct font in the about dialog
Patch32: %name-1.4.2-gtkrc.patch
Patch33: %name-1.2.8-ypcat.patch
Patch34: %name-1.4.2-autoconf2.5x.patch
# filter out -I/usr/include from output of gnome-config --cflags
Patch35: %name-1.4.2-gnome-config-cflags.patch
Patch36: %name-%version-configure_in-libs-alt.patch
Patch37: %name-%version-makefile_am-libs-alt.patch
Patch38: %name-%version-gcc41fix-alt.patch

Requires: gtk+ >= 1.2.8, ORBit, imlib, pulseaudio-daemon, alsa-plugins-pulse

%set_automake_version 1.4
%set_autoconf_version 2.13
%set_libtool_version 1.5
# Automatically added by buildreq on Wed Oct 08 2008
# Hand-edited by mutabor on the same date
BuildRequires: esound-devel gtk-doc imake imlib-devel libXpm-devel libXt-devel libdb1-devel xorg-cf-files
BuildRequires: docbook-dtds docbook-style-dsssl esound-devel gtk+-devel gtk-doc imlib-devel indent libaudiofile-devel libdb1-devel libjpeg-devel libpng-devel libtiff-devel libungif-devel openjade sgml-common xpm-devel zlib-devel
BuildRequires: libwrap-devel
BuildRequires: ORBit-devel >= 0.5.17-alt3

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System.  The %name package
includes libraries that are needed to run GNOME.

%package devel
Summary: Include files for GNOME application development
Group: Development/GNOME and GTK+
Icon: %name-devel.xpm
Requires: %name = %version-%release
Requires: esound-devel gtk+-devel imlib-devel libaudiofile-devel libdb1-devel libjpeg-devel libORBit-devel  libpng-devel libtiff-devel libungif-devel xpm-devel zlib-devel

%description devel
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The %name-devel package
includes the libraries and include files that you will need to develop
GNOME applications.

You should install the %name-devel package if you would like to
develop GNOME applications. You don't need to install %name-devel
if you just want to use the GNOME desktop environment.

%if_enabled static
%package devel-static
Summary: Static libraries for GNOME application development
Group: Development/GNOME and GTK+
Requires: %name-devel = %version-%release
Requires: libdb1-devel-static libORBit-devel-static libpng-devel-static XFree86-static-libs zlib-devel-static

%description devel-static
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The %name-devel package
includes the libraries and include files that you will need to develop
GNOME applications.

You should install the %name-devel-static package if you would like to
develop statically linked GNOME applications. You don't need to install
%name-devel-static if you just want to use the GNOME desktop environment.
%endif	# enabled static

%prep
%setup -q

# Applying RH patches.
%patch1 -p1 -b .rhsnddefs
%patch2 -p1 -b .bghack
%patch3 -p1 -b .utf8

# Applying Mandrake patches.
%patch5 -p1 -b .icons
%patch7 -p1 -b .nodesktop
%patch18 -p1 -b .prototypes
%patch19 -p1 -b .fonts
#%patch20 -p1 -b .zvtescape
%patch21 -p1 -b .keypad
%patch22 -p1 -b .zvtutf8
#%patch23 -p1 -b .libdir
%patch24 -p1 -b .includedir

# Applying ALT patches.
%patch30 -p1 -b .alt-fonts
%patch31 -p1 -b .belo
%patch32 -p1 -b .gtkrc
%patch33 -p1 -b .ypcat
%patch35 -p1 -b .gcflags

perl -pi -e 's/az /az be /g' configure.in
perl -pi -e 's/gtkrc\.el/gtkrc\.be gtkrc\.el/g' libgnomeui/Makefile.am

ac_version=`%__autoconf --version | awk '{print $NF; exit}'`
ac_version_major="${ac_version%%.*}"
ac_version_minor="${ac_version#*.}"
if [ "$ac_version_major" -gt 2 -o \
     "$ac_version_major" -eq 2 -a "$ac_version_minor" -ge 50 ]; then
%patch34 -p1
fi

%patch36 -p1 -b .libs
%patch37 -p1 -b .libs
%patch38 -p1 -b .gcc41

%build
#needed by patches 24 & 37 and Makefile.am edit
automake
#needed by patches 22 & 23, configure.in edit,
# and the autoconf 2.5x fixes (patch 34)
autoconf
pushd libart_lgpl
autoconf
popd
libtoolize --copy --force

DOCDIR=$RPM_BUILD_ROOT%_docdir %configure \
%if_enabled static
    --enable-static \
%else
    --disable-static \
%endif
    --with-kde-datadir=%_datadir %preferdb --disable-alsa --disable-gtk-doc
%make_build
%if_with test
%make check
%endif

%install
%makeinstall

cp %{SOURCE1} $RPM_BUILD_ROOT%_bindir

%find_lang %name

# TODO: pick up gnome-doc and mkstub tools and their manuals

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README
%_libdir/libgnome*.so.*
%_libdir/libgnorba*.so.*
%_libdir/libzvt*.so.*
%_libdir/libart*.so.*
%_libdir/libgtkxmhtml*.so.*
%_bindir/dns-helper
%_bindir/gconfigger
%_bindir/gnome-bug
%_bindir/gnome-dump-metadata
%_bindir/gnome-gen-mimedb
%_bindir/gnome-moz-remote
%_bindir/gnome-name-service
%_bindir/gnome_segv
%_bindir/goad-browser
%_bindir/loadshlib
%_bindir/new-object
#%attr(2711,root,utmp) %_sbindir/gnome-pty-helper
%_sbindir/gnome-pty-helper
%_datadir/idl/*
%_datadir/pixmaps/*
%config(noreplace) %_datadir/gtkrc*
%_datadir/mime-info/*
%_datadir/type-convert/type.convert
%config(noreplace) %_sysconfdir/*
%_man1dir/*
%_man5dir/*

%files devel
%doc devel-docs/README*
%doc devel-docs/*.txt
%doc devel-docs/ChangeLog
%_bindir/*-config
%_bindir/conv_deskfiles.pl
%_libdir/lib*.so
#%_libdir/lib*.la
%_libdir/*.sh
%_libdir/%name
%_includedir/*
%_datadir/aclocal/*
%_datadir/gnome/help/*
%_datadir/gnome/html/*
%_datadir/gtk-doc/html/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif	# enabled static

%changelog
* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt11
- Rebuilt with new libjpeg

* Thu Oct 14 2010 Sergey V Turchin <zerg@altlinux.org> 1.4.2-alt10
- fix requires (ALT#24300)

* Fri Aug 21 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.2-alt9
- Fixed build in new build environment.

* Wed Oct 8 2008 Yury Aliaev <mutabor@altlinux.org> 1.4.2-alt8
- updated build dependencies

* Wed May 17 2006 Yury Aliaev <mutabor@altlinux.org> 1.4.2-alt7
- fixed build with --as-needed ld option and gcc-4.1

* Sat May 22 2004 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt6
- rebuild without docs, without db2 references

* Sat Jan 03 2004 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt5
- use autoconf 2.13, add require for autoconf_2.13
- rebuild without *.la files

* Sat Oct 04 2003 Dmitry V. Levin <ldv@altlinux.org> 1.4.2-alt4
- Updated build dependencies.

* Tue Feb 11 2003 Stanislav Ievlev <inger@altlinux.ru> 1.4.2-alt3.1
- removed suid on gnome-pty-helper (ldv request)
  we must have only one /sbin/utempter sgid
- made check only with test

* Sat Feb 08 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2-alt3
- Fixed stupid typo in the build script
- Fixed build under automake-1.{6,7}

* Thu Sep 26 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2-alt2
- filter -I/usr/include out the output of gnome-config --cflags

* Sat Sep 14 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2-alt1
- 1.4.2
- Synced patches with 1.4.2-1mdk
- Disabled static by default
- Saner font rc patches
- Patch for autoconf 2.5x
- Eliminated unnecessary doc duplication
- Listed *.la files in -devel
- Moved manuals to the main package
  (sorry, too lazy to leave -config manuals in -devel)
- Listed libart documentation in /usr/share/gtk-doc
- /usr/share/{idl,mime-info,pixmaps} directories belong not in this package
- make check

* Wed Mar 13 2002 AEN <aen@logic.ru> 1.4.1.4-alt3
- new conv_deskfiles.pl

* Tue Mar 12 2002 AEN <aen@logic.ru> 1.4.1.4-alt2
- utf8menu patch

* Tue Jan 29 2002 AEN <aen@logic.ru> 1.4.1.4-alt1
- new version

* Mon Jan 21 2002 AEN <aen@logic.ru> 1.4.1.3-alt1
- patches 2, 29, 31, 32 removed

* Wed Jan 09 2002 AEN <aen@logic.ru> 1.4.1.2.90-alt2
- remove wrong dependences

* Sun Dec 29 2001 AEN <aen@logic.ru> 1.4.1.2.90-alt1
- sources from CVS

* Thu Dec 27 2001 AEN <aen@logic.ru> 1.4.1.2-alt3
- patch 8 added
- patch 14 removed

* Fri Nov 09 2001 AEN <aen@logic.ru> 1.4.1.2-alt2
- pango-devel requirements removed

* Thu Oct 11 2001 AEN <aen@logic.ru> 1.4.1.2-alt1
- new version

* Thu Sep 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4.1.1-alt3
- Updated package dependencies.

* Thu Sep 06 2001 AEN <aen@logic.ru> 1.4.1.1-alt1
- new release

* Thu May 24 2001 AEN <aen@logic.ru> 1.2.13-alt2
- terminal patch from Aleksey Morozov

* Mon Mar 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.2.11-ipl4mdk
- Moved static libraries to devel-static subpackage.

* Tue Mar 13 2001 AEN <aen@logic.ru> 1.2.11-ipl3mdk
- rebuild in release environment

* Tue Feb 1 2001 AEN <aen@logic.ru>
- rebuild with oaf 0.6.1

* Sat Jan 27 2001 Dmitry V. Levin <ldv@fandra.org> 1.2.11-ipl1mdk
- 1.2.11

* Mon Jan 22 2001 Dmitry V. Levin <ldv@fandra.org> 1.2.9-ipl1mdk
- 1.2.9
- Updated IPL patches.

* Sat Jan 06 2001 Dmitry V. Levin <ldv@fandra.org> 1.2.8-ipl3mdk
- Specfile cleanup.
- Automatically added BuildRequires.
- Rebuild with db1.
- Patched gnome-bug to avoid false dependencies.

* Sun Nov 27 2000 AEN <aen@logic.ru>
- sync with RE
- be & fonts patches

* Tue Oct 24 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.8-1mdk
- Release 1.2.8

* Wed Oct 18 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.6-1mdk
- Release 1.2.6
- don't apply merged patches (3 & 6)
- Regenerate patch 4

* Thu Oct  5 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-8mdk
- Provides main gnome directories (close bug #614)

* Tue Sep 19 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-7mdk
- Change search for icons for new KDE2 paths

* Tue Sep 12 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-6mdk
- Merge fixes from RedHat for gnome-terminal (set background, delete key)

* Mon Sep 11 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-5mdk
- Search icons in /usr/share/icons subdirectories first

* Thu Aug 24 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-4mdk
- enhance support for xalf (start application notifier)
- add noreplace for config file

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.2.4-3mdk
- automatically added BuildRequires

* Thu Aug  3 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-2mdk
- Don't install gtkrc file (was breaking some gtk themes)

* Tue Jul 25 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-1mdk
- release 1.2.4 (from Helix)

* Tue Jul 25 2000 dam's <damien@mandrakesoft.com> 1.2.3-4mdk
- added disable-alsa.

* Fri Jul 21 2000 dam's <damien@mandrakesoft.com> 1.2.3-3mdk
- BM + macrozification.

* Tue Jul 18 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.3-2mdk
- added patch to support fontsets in scores and wizards windows

* Wed Jun 21 2000 dam's <damien@mandrakesoft.com> 1.2.3-1mdk
- updated to 1.2.3

* Tue Jun 20 2000 dam's <damien@mandrakesoft.com> 1.2.1-3mdk
- Rebuild due to bad provides.

* Tue Jun 20 2000 dam's <damien@mandrakesoft.com> 1.2.1-2mdk
- Rebuild due to bad provides.

* Fri Jun  9 2000 dam's <damien@mandrakesoft.com> 1.2.1-1mdk
- update from helix release.

* Thu Apr 06 2000 Daouda Lo <daouda@mandrakesoft.com> 1.0.58-1mdk
- build release 1.0.58

* Fri Mar 31 2000 Daouda Lo <daouda@mandrakesoft.com> 1.0.56-1mdk
- from Helix stuffs
- build release 1.0.56

