
%add_findpackage_path %_K3bindir

Name: gwenview
Version: 1.4.2
Release: alt16
Summary: Simple image viewer for KDE.
License: GPL
Group: Graphics
URL: http://gwenview.sourceforge.net

Packager: Afanasov Dmitry <ender@altlinux.org>

Requires: lib%name = %version-%release kipi-plugins

Source0: %name-%version.tar
Source2: cursors.tar

Patch1: gwenview-1.4.2-alt-link.patch
Patch2: gwenview-1.4.2-automake.patch
Patch3: gwenview-1.4.2-exiv2.patch
Patch4: gwenview-1.4.2-fix-autoconf-2.64.patch

BuildRequires: fontconfig gcc-c++ kdelibs-devel libXcursor-devel libXext-devel
BuildRequires: libXt-devel libexiv2-devel libjpeg-devel libkipi-devel libmng-devel
BuildRequires: libpng-devel qt3-designer xml-utils shared-mime-info

%description
Gwenview is an image viewer for KDE.

It features a folder tree window and a file list window to provide easy
navigation in your file hierarchy.  Image loading is done by the Qt library,
so it supports all image formats your Qt installation supports.

%package -n lib%name
Summary: Library associated with %name
Group: System/Libraries

%description -n lib%name
This package contains shared libraries used by %name

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%make -f admin/Makefile.common cvs ||:

%build
%add_optflags -I%_includedir/tqtinterface -I%_K3includedir
%K3configure \
        --disable-gcc-hidden-visibility \
        --enable-final
%make_build

%install
%K3install

tar xf %SOURCE2 -C %buildroot%_K3apps/%name

%K3find_lang --with-kde %name

%files -f %name.lang
%_K3bindir/%name
%_K3lib/*.so
%_K3apps/konqueror/servicemenus/*
%_K3apps/%name
%_K3apps/gvdirpart
%_K3apps/gvimagepart
%_K3apps/kconf_update/*
%_K3xdg_apps/%name.desktop
%_K3srv/*.desktop
%_K3cfg/*.kcfg
%_K3iconsdir/crystalsvg/*/apps/gvdirpart.*
%_kde3_iconsdir/hicolor/*/apps/gvdirpart.*
%_kde3_iconsdir/hicolor/*/apps/%name.*
#%_man1dir/*

%files -n lib%name
%_libdir/*.so*
%_libdir/libkdeinit_gwenview.so

%changelog
* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 1.4.2-alt16
- rebuilt with new exiv2

* Wed Feb 23 2011 Sergey V Turchin <zerg@altlinux.org> 1.4.2-alt15
- move to alternate place
- don't package manpage

* Wed Jun 02 2010 Afanasov Dmitry <ender@altlinux.org> 1.4.2-alt13
- rebuild with exiv2-0.20

* Tue Jan 05 2010 Afanasov Dmitry <ender@altlinux.org> 1.4.2-alt12
- rebuild with exiv2-0.19.x
- add patch to fix build with autoconf-2.64

* Thu Jul 23 2009 Afanasov Dmitry <ender@altlinux.org> 1.4.2-alt11
- apply patch to fix build with exiv2-0.18.x

* Wed Jul 22 2009 Afanasov Dmitry <ender@altlinux.org> 1.4.2-alt10
- rebuild with exiv2-0.18.x (second try)

* Wed Jul 22 2009 Afanasov Dmitry <ender@altlinux.org> 1.4.2-alt9
- rebuild with exiv2-0.18.x

* Tue Jun 23 2009 Afanasov Dmitry <ender@altlinux.org> 1.4.2-alt8
- rebuild with libpng12-1.2.37-alt2

* Fri Jun 05 2009 Afanasov Dmitry <ender@altlinux.org> 1.4.2-alt7
- fix build with automake 1.11
- pack as tar
- new packager

* Sun Dec 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.2-alt6
- fixed unable to open BMP's with 1bpp

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.2-alt5
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Sun Oct 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.2-alt4
- fixed build

* Mon Apr 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.2-alt3
- fixed exec in gimp.desktop (close #15350)

* Sat Apr 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.2-alt2
- rebuild with libexiv2.so.2

* Wed Sep 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Fri Dec 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.4.1-alt2
- build with --enable-final

* Mon Nov 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Mon Sep 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Thu Aug 24 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.3.93-alt1
- 1.3.93

* Sun Jul 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.3.92b-alt1
- 1.3.92b

* Sun Jun 25 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.3.91-alt1
- 1.3.91

* Tue Jan 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.3.1-alt2
- move to freedesktop menu

* Wed Dec 14 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Mon Sep 12 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Mon Aug 22 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.2.92-alt1
- 1.2.92

* Sun Jul 17 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.2.91-alt1
- 1.2.91

* Sun Jul 17 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt3
- fixed BuildRequires

* Mon Apr 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt2
- 1.2.0

* Sun Mar 20 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1.pre4
- 1.2.0pre4

* Sun Feb 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1.pre3
- 1.2.0pre3

* Mon Feb 14 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1.pre2
- 1.2.0pre2

* Mon Jan 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1.pre1
- 1.2.0pre1

* Tue Jan 11 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.1.8-alt1
- 1.1.8

* Mon Dec 20 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Fri Oct 29 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Sat Sep 25 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.1.5-alt2
- update drag cursors

* Tue Sep 21 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Wed Aug 25 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.1.4-alt1
- 1.1.4 

* Sat Mar 13 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- initial release
