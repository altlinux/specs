Name: xmorph
Version: 20060817
Release: alt3
Packager: Fr. Br. George <george@altlinux.ru>

Summary: An X Window System tool for creating morphed images
License: GPL
Group: Graphics
Requires: libmorph = %version-%release
Url: http://sourceforge.net/projects/xmorph/
Source0: xmorph_%version.tar.bz2
Source1: xmorph-icons.tar.bz2
Source2: xmorph.desktop

Patch1: xmorph-dirinfo.patch
Patch2: xmorph-gcc_warnings.patch
Patch3: xmorph-gcc43.patch

%def_disable static

# Automatically added by buildreq on Fri Jan 20 2012
# optimized out: fontconfig fontconfig-devel glib2-devel libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel pkg-config xorg-xproto-devel
BuildRequires: chrpath gcc-c++ imake libXaw-devel libXext-devel libfftw3-devel libgtk+2-devel xorg-bitmaps xorg-cf-files

%package -n libmorph
Summary: Internal library required for xmorph/gtkmorph
Group: Graphics

%package -n libmorph-devel
Summary: Headers  required for xmorph/gtkmorph development
Requires: libmorph = %version-%release
Group: Graphics

%package -n libmorph-devel-static
Summary: Static libraries required for xmorph/gtkmorph development
Requires: libmorph-devel = %version-%release
Group: Graphics

%description
Xmorph is a digital image warping (aka morphing) program.  Xmorph
provides the tools needed and comprehensible instructions for you to
create morphs: changing one image into another.  Xmorph runs under the
X Window System.

%description -n libmorph
Internal library for xmorph and gtkmorph.

%description -n libmorph-devel
Development headers  for xmorph and gtkmorph.

%description -n libmorph-devel-static
Development static libs for xmorph and gtkmorph.

%prep
%setup -q -n %name-%version
%patch1
%patch2
%patch3 -p1
tar xvf %SOURCE1

%build
%configure %{subst_enable static} --disable-rpath
%make_build
chrpath -d */.libs/*morph

%install
%makeinstall

#mdk menu
mkdir -p %buildroot%_desktopdir %buildroot%_niconsdir %buildroot%_miconsdir %buildroot%_liconsdir
install mini/%name.xpm %buildroot%_miconsdir
install %name.xpm %buildroot%_niconsdir/
install large/%name.xpm %buildroot%_liconsdir
install %SOURCE2 %buildroot%_desktopdir
install morph/morph %buildroot%_bindir/morph
%find_lang  %name

%files -f %name.lang
%doc AUTHORS README HISTORY NEWS
%_datadir/%name
%_bindir/*
%_mandir/*/*
%_infodir/*
%_miconsdir/*.xpm
%_liconsdir/*.xpm
%_niconsdir/*.xpm
%_desktopdir/*

%files -n libmorph
%_libdir/*.so.*

%files -n libmorph-devel
%_libdir/*.so
%_includedir/*

%if_enabled static
%files -n libmorph-devel-static
%_libdir/*.a
%endif #static

%changelog
* Fri Jan 20 2012 Fr. Br. George <george@altlinux.ru> 20060817-alt3
- Fix build
- NoX11 binary

* Sat Nov 21 2009 Repocop Q. A. Robot <repocop@altlinux.org> 20060817-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libmorph
  * postun_ldconfig for libmorph
  * pixmap-in-deprecated-location for xmorph
  * obsolete-call-in-post-install-info for xmorph
  * update_menus for xmorph
  * postclean-05-filetriggers for spec file

* Tue Oct 28 2008 Fr. Br. George <george@altlinux.ru> 20060817-alt2
- GCC4.3 build fix
- Desktop file add

* Thu Dec 14 2006 Fr. Br. George <george@altlinux.ru> 20060817-alt1
- New version
- Sync with SUSE patches

* Mon Dec 19 2005 Fr. Br. George <george@altlinux.ru> 20040717-alt1
- new version

* Fri Aug 10 2001 AEN <aen@logic.ru> 20010220-alt1
- new version
- sync with MDK
- static package

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation
* Mon Dec 11 2000 Egil Moeller <redhog@mandrakesoft.com> 2000.03.03-7mdk
- Defined GIMP_ENABLE_COMPAT_CRUFT as a cludge not to have to have to
  upport all of this sh*t code to the new gimplib (Without it, it does
  not compile anymore) (It will break again anyway, with gimplib 1.2,
  but I hope, I hope, that the xmorph author fixes this until then)...

* Mon Oct 02 2000 Daouda Lo <daouda@mandrakesoft.com> 2000.03.03-6mdk
- icons should be transparents!
- macrozifications

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 2000.03.03-5mdk
- automatically added BuildRequires

* Wed May 03 2000 dam's <damien@mandrakesoft.com> 2000.03.03-4mdk
- Corrected icones.

* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 2000.03.03-3mdk
- Convert gif icon to xpm.

* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 2000.03.03-2mdk
- Added menu entry.

* Tue Mar 28 2000 dam's <damien@mandrakesoft.com> 2000.03.03-1mdk
- Update to 2000mar03

* Fri Nov 12 1999 dam's <damien@mandrakesoft.com>
- Mandrake release

* Thu May 06 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 7)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
